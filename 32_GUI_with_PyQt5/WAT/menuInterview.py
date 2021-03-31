#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 05:30:25 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuInterview.py

"""
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sys
import time
import os
import copy

import NewInterview
import InterviewHandler


class menuInterview_Handler(object):
    def __init__(self, ui, configFile="interview.json"):
        self.ui = ui
        self.configFile = configFile
        self.configFilePath = "config"
        self.FreshConfigFile = copy.copy(self.configFile)
        self.FreshConfigFilePath = copy.copy(self.configFilePath)
        self.loadDefaultInterviewConfig()
        self.ui.actionNew_Interview.triggered.connect(self.FreshNewInterview)
        self.ui.actionOpen_Interview_File.triggered.connect(self.Open_Interview_File_Handler)
        self.ui.actionSave_Current_Interview_File.triggered.connect(self.Save_Current_Interview_File_Handler)
        self.ui.actionExit.triggered.connect(self.Exit_Handler)
        self.newInterview = InterviewHandler.InterviewHandler(self.ui)
        
        self.newInterview.configFile =self.configFile
        self.newInterview.configFilePath = self.configFilePath
        #self.newInterview.generateInterviewForm()
        
        #self.newInterview.InterviewForm.hide()
        self.newInterview.InterviewForm.close()
        self.newInterview.newInterviewSubmited = False
        self.newInterview.newInterviewFormShowed = False
        self.newInterview.newInterviewCanceled = False
        
    def loadDefaultInterviewConfig(self):
        try:
            path = os.path.join(self.configFilePath,self.configFile)
            print("loading : ",path)
            with open(path,"r") as fp:
                self.config = json.load(fp)
        except Exception:
            sys.stderr("No such configuration fie \""+self.configFile+"\"")
            #sys.exit(1)
            return 0
        return 1
    
    def saveTempInterviewConfig(self):
        try:
            path = os.path.join("temp_config",os.path.split(self.configFile)[1])
            print("Saving to : ",path)
            with open(path,"w") as fp:
                json.dump(self.config,fp,indent=4)
        except Exception as eWrite:
            sys.stderr.write("Unable to write to temp interview config")
            sys.stderr.write(eWrite)
            sys.exit(3)
    
    def setDefaultInterviewFields(self):
        self.NI_FORM.responderName.setText(self.config["NAME_OF_RESPONDER"])
        self.NI_FORM.companyName.setText(self.config["COMPANY_NAME"])
        self.NI_FORM.interviewerName.setText(self.config["INTERVIEWED_BY"])
        if self.config["NUMBER_OF_WORDS_IN_TEST"]==20:
            self.NI_FORM.wordsSelected20.click()
        elif self.config["NUMBER_OF_WORDS_IN_TEST"]==100:
            self.NI_FORM.wordsSelected100.click()
        else:
            self.NI_FORM.wordsSelected50.click()
        #NI.dateEdited.setDate()
        
        
    
    def onCancelNewInterviewForm(self):
        self.NewInterviewForm.close()
        #self.ui.mainCanvas.close()
        self.newInterview.newInterviewFormShowed = False
        self.newInterview.newInterviewCanceled = True
        self.newInterview.newInterviewSubmited = False
        print("interview Canceled")
    
    def onSubmitNewInterviewForm(self):
        #self.loadDefaultInterviewConfig()
        self.config["NAME_OF_RESPONDER"] = self.NI_FORM.responderName.text()
        self.config["COMPANY_NAME"] = self.NI_FORM.companyName.text()
        self.config["INTERVIEWED_BY"] = self.NI_FORM.interviewerName.text()
        self.config["DATE_OF_INTERVIEW"] = self.NI_FORM.dateEdited.text()
        self.config["TIME_STAMP"] = time.time()
        if self.NI_FORM.wordsSelected20.isChecked():
            self.config["NUMBER_OF_WORDS_IN_TEST"] = 20
        elif self.NI_FORM.wordsSelected50.isChecked():
            self.config["NUMBER_OF_WORDS_IN_TEST"] = 50
        elif self.NI_FORM.wordsSelected100.isChecked():
            self.config["NUMBER_OF_WORDS_IN_TEST"] = 100
        #print(self.config)
        self.saveTempInterviewConfig()
        print("Responder Name  : ", self.config["NAME_OF_RESPONDER"])
        print("Company Name    : ", self.config["COMPANY_NAME"])
        print("Interviewer Name: ", self.config["INTERVIEWED_BY"])
        print("Date            : ", self.config["DATE_OF_INTERVIEW"])
        self.NewInterviewForm.close()
        self.startInterview()
    
    def startInterview(self): #TODO
        self.newInterview.closeInterview()
        self.newInterview = InterviewHandler.InterviewHandler(self.ui)
        self.newInterview.setInterveiwConfiguration(self.config)
        self.newInterview.newInterviewSubmited = True
        self.newInterview.newInterviewFormShowed = False
        self.newInterview.newInterviewCanceled = False
        self.newInterview.showInterviewPanel()
    
    def FreshNewInterview(self):
        self.configFile = copy.copy(self.FreshConfigFile)
        self.configFilePath = copy.copy(self.FreshConfigFilePath)
        self.New_Interview_Handler()
    
    def New_Interview_Handler(self): #TODO
        print("New Interview Handler Callback")
        if self.loadDefaultInterviewConfig():
            pass
        else:
            return 0
        
        if not self.newInterview.newInterviewFormShowed and not self.newInterview.newInterviewSubmited:
            self.newInterview = InterviewHandler.InterviewHandler(self.ui)
            
            self.newInterview.configFile =self.configFile
            self.newInterview.configFilePath = self.configFilePath
            self.newInterview.generateInterviewForm()
            
            self.NewInterviewForm = QtWidgets.QWidget(self.ui.centralwidget)
            self.NI_FORM = NewInterview.Ui_Form()
            self.NI_FORM.setupUi(self.NewInterviewForm)
            self.ui.mainCanvas = self.NewInterviewForm
            self.NI_FORM.cancelInput.clicked.connect(self.onCancelNewInterviewForm)
            self.NI_FORM.submitDetails.clicked.connect(self.onSubmitNewInterviewForm)
            self.NI_FORM.enableEdit.setChecked(True)
            self.setDefaultInterviewFields()
            self.newInterview.newInterviewFormShowed = True
            self.newInterview.newInterviewSubmited = True
            self.NewInterviewForm.show()
            return 1
        else:
            print("Form already showed")
            return 0
    
    def Open_Interview_File_Handler(self): #TODO
        print("Open Interview File Callback")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, d = QtWidgets.QFileDialog.getOpenFileNames(self.ui.centralwidget,"QFileDialog.getSaveFileName()","","WAT Interview (*.json);;All Files (*)", options=options)
        #file_name = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget, 'Save File')
        if len(fileName):
            #self.newInterview.closeInterview()
            path, filename = os.path.split(fileName[0])
            print("Path: ",path)
            print("File: ",filename)
            #self.newInterview.closeInterview()
            self.configFilePath = path
            self.configFile = filename
            try:
                self.NewInterviewForm.close()
                self.newInterview.closeInterview()
            except Exception:
                print("No interview obj yet")
            if self.New_Interview_Handler():    
                #self.newInterview.setInterveiwConfiguration(self.config)
                self.NI_FORM.submitDetails.click()
            else: #TODO
                print("Invalid interview file to open")
        
    def Save_Current_Interview_File_Handler(self):
        print("Save Current Interview File Callback")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, d = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget,"QFileDialog.getSaveFileName()","","WAT Interview (*.json);;All Files (*)", options=options)
        #file_name = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget, 'Save File')
        print(type(fileName))
        print(type(d))
    
    def Exit_Handler(self):
        print("Exit Callback")
        self.ui.MainWindow.close()

