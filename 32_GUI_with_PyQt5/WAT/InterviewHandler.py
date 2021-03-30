#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 07:35:47 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: InterviewHandler.py
"""

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, json
import time
from threading import Thread

import complexIndicatorHandler
import Interview



class InterviewHandler(object):
    def __init__(self, ui, configFile="temp_config/interview.json"):
        self.configFile = configFile
        self.ui = ui
        self.loadInterviewConfiguration()
        self.interviewOperationStateValue = 0
        self.timerStarted = False
        self.timerValue = 0
        self.timerStartTime = 0
        
        self.InterviewForm = QtWidgets.QWidget(self.ui.centralwidget)
        #ComplexIndicatorView = QtWidgets.QWidget()         
        self.I_FORM = Interview.Ui_Form()
        self.I_FORM.setupUi(self.InterviewForm)
        self.ui.mainCanvas = self.InterviewForm
        
        self.CI = complexIndicatorHandler.ComplexIndicatorHandler(self.I_FORM)
        self.CI.generateComplexIndicatorForm()
        
        self.I_FORM.closeWidgetButton.clicked.connect(self.closeInterview)
        self.I_FORM.interviewOperationalButton.clicked.connect(self.interviewOperationalButtonHandler)
        
    
    def loadInterviewConfiguration(self):
        try:
            with open(self.configFile, "r") as fp:
                self.config = json.load(fp)
        except Exception as eOpen:
            sys.stderr.write(self.configFile," No such config file or directory")
            sys.stderr.write(eOpen)
            sys.exit(2)
    
    def setInterveiwConfiguration(self,config):
        self.config = config
    
    def getInterviewConfiguration(self):
        pass
    
    def saveInterviewConfiguration(self):
        try:
            with open(self.configFile,"w") as fp:
                json.dump(self.config,fp,indent=4)
        except Exception as eSave:
            sys.stderr.write("Unable to write temp interveiw config file ")
            sys.stderr.write(eSave)
            sys.exit(4)
    
    def closeInterview(self): #TODO
        self.InterviewForm.close()
    
    def showInterviewPanel(self):
        self.CI.resetComplexIndicatorInput()
        
        self.CI.hideComplexIndicatorInput()
        self.I_FORM.timeTakenLabel.hide()
        self.I_FORM.responseWrodLabel.hide()
        self.I_FORM.lastResponseWord.hide()
        #self.CI.showComplexIndicatorInput()
        self.I_FORM.interviewOperationalButton.setText("Start Timer")
        self.InterviewForm.show()
    
    def interviewOperationalButtonHandler(self):
        self.interviewOperationStateValue +=1
        self.interviewOperationStateValue %=3
        if self.interviewOperationStateValue==1:
            self.I_FORM.interviewOperationalButton.setText("Stop Timer")
            self.timerStarted = True
            self.timerStartTime = time.time()
            Thread(target=self.showTimerLCD,args=()).start()
            self.I_FORM.timeTakenLabel.hide()
            self.I_FORM.responseWrodLabel.hide()
            self.I_FORM.lastResponseWord.hide()
            
        elif self.interviewOperationStateValue==2:
            self.timerStarted = False
            print("Time taken for response : ",self.timerValue," S")
            self.I_FORM.interviewOperationalButton.setText("Submit->Next")
            self.CI.showComplexIndicatorInput()
            self.I_FORM.timeTakenLabel.setVisible(not self.timerStarted)
            self.I_FORM.responseWrodLabel.setVisible(not self.timerStarted)
            self.I_FORM.lastResponseWord.setVisible(not self.timerStarted)
            self.I_FORM.timeTakenLabel.setText("Time Taken        : "+str(self.timerValue)+ " Seconds")
            self.I_FORM.timeTakenLabel.show()
            self.I_FORM.responseWrodLabel.show()
            self.I_FORM.lastResponseWord.show()
            
        elif self.interviewOperationStateValue==0:
            self.saveInterviewConfiguration()
            self.I_FORM.interviewOperationalButton.setText("Start Timer")
            self.CI.hideComplexIndicatorInput()
            self.I_FORM.timerLabel.display(str(0.00))
            self.I_FORM.timeTakenLabel.hide()
            self.I_FORM.responseWrodLabel.hide()
            self.I_FORM.lastResponseWord.hide()
            
    
    def setInterviewValues(self):
        pass
    
    def startInterview(self):
        pass
    
    def showTimerLCD(self):
        self.I_FORM.timerLabel.display(str(0.00))
        while(self.timerStarted):
            self.timerValue = time.time()-self.timerStartTime
            self.timerValue *= 100
            self.timerValue = int(self.timerValue)/100.00
            time.sleep(0.2)
            self.I_FORM.timerLabel.display(str(self.timerValue))
    
if __name__=='__main__':
    pass
