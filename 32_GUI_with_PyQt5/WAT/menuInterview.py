#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 05:30:25 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuInterview.py

"""
from PyQt5 import QtCore, QtGui, QtWidgets
import NewInterview
import InterviewHandler as IH
import json
import sys


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
    
    def setDefaultInterviewFields(self, NI):
        NI.responderName.setText(self.config["NAME_OF_RESPONDER"])
        NI.companyName.setText(self.config["COMPANY_NAME"])
        NI.interviewerName.setText(self.config["INTERVIEWED_BY"])
        if self.config["NUMBER_OF_WORDS_IN_TEST"]==20:
            NI.wordsSelected20.click()
        elif self.config["NUMBER_OF_WORDS_IN_TEST"]==100:
            NI.wordsSelected100.click()
        else:
            NI.wordsSelected50.click()
        #NI.dateEdited.setDate()
        
        
    
    def onCancelNewInterviewForm(self, NewInterviewForm):
        NewInterviewForm.close()
        self.newInterviewFormShowed = False
        self.newInterviewCanceled = True
        print("interview Canceled")
    
    def onSubmitNewInterviewForm(self, NI):
        print("Responder Name : ",NI.responderName.text())
        print("Company Name   : ",NI.companyName.text())
        print("Interviewer Name: ",NI.interviewerName.text())
        print("Date : ",NI.dateEdited.text())
        self.newInterviewSubmited = True
        
    
    def New_Interview_Handler(self): #TODO
        print("New Interview Handler Callback")
        if not self.newInterviewFormShowed:
            NewInterviewForm = QtWidgets.QWidget(self.ui.centralwidget)
            NI = NewInterview.Ui_Form()
            NI.setupUi(NewInterviewForm)
            self.ui.mainCanvas = NewInterviewForm
            NI.cancelInput.clicked.connect(lambda y: self.onCancelNewInterviewForm(NewInterviewForm))
            NI.submitDetails.clicked.connect(lambda y: self.onSubmitNewInterviewForm(NI))
            self.ui.mainCanvas.show()
            NI.enableEdit.setChecked(True)
            self.setDefaultInterviewFields(NI)
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

