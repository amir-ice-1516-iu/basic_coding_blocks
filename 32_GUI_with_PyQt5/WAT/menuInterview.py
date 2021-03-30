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

import NewInterview
import InterviewHandler


class menuInterview_Handler(object):
    def __init__(self, ui, configFile="config/interview.json"):
        self.ui = ui
        self.configFile = configFile
        self.loadDefaultInterviewConfig()
        self.ui.actionNew_Interview.triggered.connect(self.New_Interview_Handler)
        self.newInterviewFormShowed = False
        self.newInterviewCanceled = False
        self.newInterviewSubmited = False
    
    def loadDefaultInterviewConfig(self):
        try:
            with open(self.configFile,"r") as fp:
                self.config = json.load(fp)
        except Exception:
            sys.stderr("No such configuration fie \""+self.configFile+"\"")
            sys.exit(1)
    
    def saveTempInterviewConfig(self):
        try:
            with open("temp_"+self.configFile,"w") as fp:
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
        self.newInterviewFormShowed = False
        self.newInterviewCanceled = True
        self.newInterviewSubmited = False
        print("interview Canceled")
    
    def onSubmitNewInterviewForm(self):
        self.config["NAME_OF_RESPONDER"] = self.NI_FORM.responderName.text()
        self.config["COMPANY_NAME"] = self.NI_FORM.companyName.text()
        self.config["INTERVIEWED_BY"] = self.NI_FORM.interviewerName.text()
        self.config["DATE_OF_INTERVIEW"] = self.NI_FORM.dateEdited.text()
        self.config["TIME_STAMP"] = time.time()
        self.saveTempInterviewConfig()
        print("Responder Name  : ", self.config["NAME_OF_RESPONDER"])
        print("Company Name    : ", self.config["COMPANY_NAME"])
        print("Interviewer Name: ", self.config["INTERVIEWED_BY"])
        print("Date            : ", self.config["DATE_OF_INTERVIEW"])
        self.newInterviewSubmited = True
        self.newInterviewFormShowed = False
        self.newInterviewCanceled = False
        self.newInterview = InterviewHandler.InterviewHandler(self.ui)
        self.newInterview.setInterveiwConfiguration(self.config)
        self.NewInterviewForm.hide()
        self.newInterview.showInterviewPanel()
        
    
    def New_Interview_Handler(self): #TODO
        print("New Interview Handler Callback")
        if not self.newInterviewFormShowed:
            self.NewInterviewForm = QtWidgets.QWidget(self.ui.centralwidget)
            self.NI_FORM = NewInterview.Ui_Form()
            self.NI_FORM.setupUi(self.NewInterviewForm)
            self.ui.mainCanvas = self.NewInterviewForm
            self.NI_FORM.cancelInput.clicked.connect(self.onCancelNewInterviewForm)
            self.NI_FORM.submitDetails.clicked.connect(self.onSubmitNewInterviewForm)
            self.ui.mainCanvas.show()
            self.NI_FORM.enableEdit.setChecked(True)
            self.setDefaultInterviewFields()
            self.newInterviewFormShowed = True
        else:
            print("Form already showed")
    
    def Open_Interview_File_Handler(self): #TODO
        print("Open Interview File Callback")
    
    def Save_Current_Interview_File_Handler(self): #TODO
        print("Save Current Interview File Callback")
    
    def Exit_Handler(self): #TODO
        print("Exit Callback")
        self.ui.close()

