#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 05:30:25 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuInterview.py

"""
from PyQt5 import QtWidgets #, QtCore, QtGui
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
        self.newInterview = InterviewHandler.InterviewHandler(self.ui)
        
        self.newInterview.configFile =self.configFile
        self.newInterview.configFilePath = self.configFilePath
        #self.newInterview.generateInterviewForm()
        
        #self.newInterview.InterviewForm.hide()
        self.newInterview.InterviewForm.close()
        self.newInterview.newInterviewSubmited = False
        self.newInterview.newInterviewFormShowed = False
        self.newInterview.newInterviewCanceled = False
        self.INTERVIEW_SETUP_MODE = False
        
    def loadDefaultInterviewConfig(self):
        try:
            path = os.path.join(self.configFilePath,self.configFile)
            if self.ui.DEBUG_MODE:
                print("loading E1: ",path)
            with open(path,"r") as fp:
                self.config = json.load(fp)
        except Exception:
            if self.ui.DEBUG_MODE:
                sys.stderr("No such configuration fie \""+self.configFile+"\"")
            #sys.exit(1)
            return 0
        return 1
    
    def saveTempInterviewConfig(self):
        try:
            path = os.path.join("temp_config",os.path.split(self.configFile)[1])
            if self.ui.DEBUG_MODE:
                print("Saving to : ",path)
            with open(path,"w") as fp:
                json.dump(self.config,fp,indent=4)
        except Exception as eWrite:
            if self.ui.DEBUG_MODE:
                sys.stderr.write("Unable to write to temp interview config")
                sys.stderr.write(str(eWrite))
            sys.exit(3)
    
    def loadTempInterviewConfig(self):
        try:
            path = os.path.join("temp_config",self.configFile)
            if self.ui.DEBUG_MODE:
                print("loading T1: ",path)
            with open(path,"r") as fp:
                self.config = json.load(fp)
        except Exception:
            if self.ui.DEBUG_MODE:
                sys.stderr("No such configuration fie \""+self.configFile+"\"")
            #sys.exit(1)
            return 0
        return 1
    
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
        if self.ui.DEBUG_MODE:
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
        if self.ui.DEBUG_MODE:
            print("Responder Name  : ", self.config["NAME_OF_RESPONDER"])
            print("Company Name    : ", self.config["COMPANY_NAME"])
            print("Interviewer Name: ", self.config["INTERVIEWED_BY"])
            print("Date            : ", self.config["DATE_OF_INTERVIEW"])
        self.NewInterviewForm.close()
        if self.INTERVIEW_SETUP_MODE:
            try:
                with open(os.path.join(self.FreshConfigFilePath,self.FreshConfigFile),"w") as fp:
                    json.dump(self.config, fp, indent=4)
                    if self.ui.DEBUG_MODE:
                        print("Interview Account Setup Successful") #TOEDIT notify via GUI
                        self._showSetupSuccessDialog("Account Setup Success", "Interview Account Setup Successful")
            except Exception as eSetup:
                if self.ui.DEBUG_MODE:
                    sys.stderr.write("Unable to setup interview")
                    sys.stderr.write(str(eSetup))
        else:
            self.startInterview()
    def _showSetupSuccessDialog(self,title, message):
       msg = QtWidgets.QMessageBox()
       msg.setIcon(QtWidgets.QMessageBox.Information)
    
       msg.setText(message)
       #msg.setInformativeText("This is additional information")
       msg.setWindowTitle(title)
       #msg.setDetailedText("The details are as follows:")
       msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
       #msg.buttonClicked.connect(self._msgbtn)
    	
       retval = msg.exec_()
       #if self.ui.DEBUG_MODE:
       #    print("value of pressed message box button:", retval)
	
    #def _msgbtn(i):
    #   print("Button pressed is:",i)
    
    def startInterview(self):
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
    
    def Resume_Interview_Handler(self):
        try:
            self.ui.lastActiveWidget.close()
        except Exception as eClear:
            if self.ui.DEBUG_MODE:
                print("Unable to clear window central widget")
                sys.stderr.write(str(eClear))
            sys.exit(12)
        self.loadTempInterviewConfig()
        self.startInterview()
    
    def New_Interview_Handler(self):
        try:
            self.ui.lastActiveWidget.close()
        except Exception as eClear:
            if self.ui.DEBUG_MODE:
                print("Unable to clear window central widget")
                sys.stderr.write(str(eClear))
            sys.exit(10)
        if self.ui.DEBUG_MODE:
            print("New Interview Handler Callback")
        if self.loadDefaultInterviewConfig():        
            #if not self.newInterview.newInterviewFormShowed and not self.newInterview.newInterviewSubmited:
            self.newInterview = InterviewHandler.InterviewHandler(self.ui)
            
            self.newInterview.configFile =self.configFile
            self.newInterview.configFilePath = self.configFilePath
            self.newInterview.generateInterviewForm()
            
            self.NewInterviewForm = QtWidgets.QWidget(self.ui.centralwidget)
            self.ui.lastActiveWidget = self.NewInterviewForm
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
            return 0
        #else:
        #    if self.ui.DEBUG_MODE:
        #        print("Form already showed")
        #    return 0
    
    def Open_Interview_File_Handler(self):
        if self.ui.DEBUG_MODE:
            print("Open Interview File Callback")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, d = QtWidgets.QFileDialog.getOpenFileNames(self.ui.centralwidget,"QFileDialog.getSaveFileName()","","WAT Interview (*.json);;All Files (*)", options=options)
        #file_name = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget, 'Save File')
        if len(fileName):
            #self.newInterview.closeInterview()
            path, filename = os.path.split(fileName[0])
            self.configFilePath = path
            self.configFile = filename
            try:
                self.NewInterviewForm.close()
                self.newInterview.closeInterview()
            except Exception:
                if self.ui.DEBUG_MODE:
                    print("No interview obj yet")
            if self.New_Interview_Handler():    
                #self.newInterview.setInterveiwConfiguration(self.config)
                self.configFile = copy.copy(self.FreshConfigFile)
                self.NI_FORM.submitDetails.click()
            else:
                if self.ui.DEBUG_MODE:
                    print("Invalid interview file to open")
        
    def Save_Current_Interview_File_Handler(self):
        if self.ui.DEBUG_MODE:
            print("Save Current Interview File Callback")
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, d = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget,"QFileDialog.getSaveFileName()","","WAT Interview (*.json);;All Files (*)", options=options)
        #file_name = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget, 'Save File')
        if self.ui.DEBUG_MODE:
            print(fileName)
        try:
            if fileName!="":
                if fileName[-4:]=="json":
                    if self.loadTempInterviewConfig():
                        with open(fileName, "w") as fp:
                            json.dump(self.config,fp,indent=4)
                            if self.ui.DEBUG_MODE:
                                print("File : ",fileName)
                                print("Saved")
                else:
                    if self.ui.DEBUG_MODE:
                        print("Invalid File name of format")
            else:
                if self.ui.DEBUG_MODE:
                    print("Unable to save file")
        except Exception as eSave:
            if self.ui.DEBUG_MODE:
                sys.stderr.write("Unable to save")
                sys.stderr.write(str(eSave))
    
    def Open_Generated_Report_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Open Generated Report Handler callback")
    
    def Save_Generated_Report_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Save Generated Report Handler callback")
    
    def Export_Generated_Report_To_PDF_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Export Generated Report TO PDF Handler callback")
            
    def Exit_Handler(self):
        if self.ui.DEBUG_MODE:
            print("Exit Callback")
        self.ui.MainWindow.close()

