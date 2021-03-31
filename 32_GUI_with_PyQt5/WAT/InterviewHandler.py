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
import os

import complexIndicatorHandler
import Interview



class InterviewHandler(object):
    def __init__(self, ui, configFile="interview.json"):
        self.configFile = configFile
        self.configFilePath = "temp_config"
        self.ui = ui
        self.loadInterviewConfiguration()
        self.wordsFile = self.config["INTERVIEW_WORDS_JSON_FILE"]
        self.loadInterviewWords()
        self.interviewOperationStateValue = 0
        self.timerStarted = False
        self.timerValue = 0
        self.timerStartTime = 0
        self._currentWordSerial = self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["CURRENT_TEST_SERIAL"]     
        self.newInterviewSubmited = False
        self.newInterviewFormShowed = False
        self.newInterviewCanceled = False
        self.alive = True
        
        self.generateInterviewForm()
        
        self.CI = complexIndicatorHandler.ComplexIndicatorHandler(self.I_FORM)
        self.CI.generateComplexIndicatorForm()
        
        self.I_FORM.closeWidgetButton.clicked.connect(self.closeInterview)
        self.I_FORM.interviewOperationalButton.clicked.connect(self.interviewOperationalButtonHandler)
    
    def generateInterviewForm(self):
        self.InterviewForm = QtWidgets.QWidget(self.ui.centralwidget)
        #ComplexIndicatorView = QtWidgets.QWidget()         
        self.I_FORM = Interview.Ui_Form()
        self.I_FORM.setupUi(self.InterviewForm)
        self.ui.mainCanvas = self.InterviewForm
    
    def loadInterviewWords(self):
        try:
            print("Loading : ",self.wordsFile)
            with open(self.wordsFile,"r") as fp:
                self.interview_words = json.load(fp)
        except Exception as eWordLoad:
            sys.stderr.write("Unable to load ",self.wordsFile," file" )
            sys.stderr.write(eWordLoad)
            sys.exit(5)
    
    def loadInterviewConfiguration(self):
        try:
            path = os.path.join(self.configFilePath,self.configFile)
            print("Loading : ",path)
            with open(path, "r") as fp:
                self.config = json.load(fp)
        except Exception as eOpen:
            sys.stderr.write(self.configFile+" No such config file or directory")
            sys.stderr.write(eOpen)
            sys.exit(2)
    
    #@staticmethod
    def setInterveiwConfiguration(self,config):
        self.config = config
        #self.saveInterviewConfiguration()
    
    def getInterviewConfiguration(self):
        pass
    
    def saveInterviewConfiguration(self):
        try:
            path = os.path.join("temp_config",os.path.split(self.configFile)[1])
            print("Saving to : ",path)
            with open(path,"w") as fp:
                json.dump(self.config,fp,indent=4)
        except Exception as eSave:
            sys.stderr.write("Unable to write temp interveiw config file ")
            sys.stderr.write(eSave)
            sys.exit(4)
    
    def closeInterview(self): #TODO
        self.InterviewForm.close()
        self.newInterviewSubmited = False
        self.newInterviewFormShowed = False
        self.newInterviewCanceled = False
        self.alive = False
    
    def showInterviewPanel(self):
        self.CI.resetComplexIndicatorInput()
        
        self.CI.hideComplexIndicatorInput()
        self.I_FORM.timeTakenLabel.hide()
        self.I_FORM.responseWrodLabel.hide()
        self.I_FORM.lastResponseWord.hide()
        #self.CI.showComplexIndicatorInput()
        self._interviewMessage = "WAT Interview With "+self.config["NAME_OF_RESPONDER"]+ " of "+self.config["COMPANY_NAME"]+ " on "+self.config["DATE_OF_INTERVIEW"]
        self.I_FORM.interviewDetailsLabel.setText(self._interviewMessage)
        self.showNextWord()
        self.I_FORM.interviewOperationalButton.setText("Start Timer")
        self.InterviewForm.show()
    
    def showNextWord(self):
        
        if self.config["CURRENT_ROUND"] ==1:
            self.I_FORM.testRoundLabel.setText("First Pass")
        elif self.config["CURRENT_ROUND"] ==2:
            self.I_FORM.testRoundLabel.setText("Second Pass")
        else:
            sys.stderr.write("Invalid round")
            sys.exit(6)
        self._wordSerailMessage = "Word "+str(self._currentWordSerial)
        self.I_FORM.wordSerialNumberLabel.setText(self._wordSerailMessage)
        self._currentWord = self.interview_words[str(self._currentWordSerial)]
        self.I_FORM.testWordLabel.setText("<font color='red'>"+self._currentWord+"</font>")
        
    
    def interviewOperationalButtonHandler(self):
        self.interviewOperationStateValue +=1
        self.interviewOperationStateValue %=3
        if self.interviewOperationStateValue==1:
            self.I_FORM.interviewOperationalButton.setText("Stop Timer")
            if self.config["CURRENT_ROUND"]==1:
                self.timerStarted = True
                self.timerStartTime = time.time()
                Thread(target=self.showTimerLCD,args=()).start()
            elif self.config["CURRENT_ROUND"]==2:
                print("ROUND 2 Started")
            self.I_FORM.timeTakenLabel.hide()
            self.I_FORM.responseWrodLabel.hide()
            self.I_FORM.lastResponseWord.hide()
            
        elif self.interviewOperationStateValue==2:
            self.timerStarted = False
            print("Time taken for response : ",self.timerValue," S")
            self.I_FORM.interviewOperationalButton.setText("Submit->Next")
            self.CI.showComplexIndicatorInput()
            self.I_FORM.timeTakenLabel.setText("Time Taken        : "+str(self.timerValue)+ " Seconds")
            self.I_FORM.timeTakenLabel.show()
            self.I_FORM.lastResponseWord.setText("")
            self.I_FORM.responseWrodLabel.show()
            self.I_FORM.lastResponseWord.show()
            
        elif self.interviewOperationStateValue==0:
            self.saveInterviewConfiguration()
            self.I_FORM.interviewOperationalButton.setText("Start Timer")
            self.processResponse()
            if self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["COMPLETED"]:
                if self.config["CURRENT_ROUND"]==2:
                    pass
                else:
                    self.showNextWord()
            else:
                self.showNextWord()
            self.CI.hideComplexIndicatorInput()
            self.I_FORM.timerLabel.display(str(0.00))
            self.I_FORM.timeTakenLabel.hide()
            self.I_FORM.responseWrodLabel.hide()
            self.I_FORM.lastResponseWord.hide()
    
    def processResponse(self):
        """"EXAMPLE_WORD" : {
            "SERIAL_NO" : 1,
            "RESPONSE_WORD": "Example_Response",
            "COMPLEX_INDICATORS": {
                
                },
            "TIME_TAKEN" : "0.00"
            }"""
#        if self.config["CURRENT_ROUND"]==2:
#            if self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["COMPLETED"]:
#                self.saveInterviewConfiguration()
#                self.closeInterview()
        
        
        if self._currentWordSerial == self.config["NUMBER_OF_WORDS_IN_TEST"]:
            if self.config["CURRENT_ROUND"] == 1:
                self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["COMPLETED"] = 1
                self.processAssociatedComplexIndicators()
                self.config["CURRENT_ROUND"]=2
                self._currentWordSerial = 1
                print("First pass completed")
            elif self.config["CURRENT_ROUND"]==2:
                self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["COMPLETED"] = 1
                self.processAssociatedComplexIndicators()
                print("Interview completed waiting for report to generate")
                self.closeInterview()
                return
            else:
                sys.stderr.write("Something wrong happed invalid current round")
                sys.exit(7)
        else:
            self.processAssociatedComplexIndicators()
            
        self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["CURRENT_TEST_SERIAL"] = self._currentWordSerial
        print("CTS: "+str(self._currentWordSerial))
        print("CR: "+str(self.config["CURRENT_ROUND"]))
        print("CR1:"+str(self.config["ROUND1_RESPONSES"]["COMPLETED"]))
        print("CR2:"+str(self.config["ROUND2_RESPONSES"]["COMPLETED"]))
        self.saveInterviewConfiguration()     
        self.CI.resetComplexIndicatorInput()
    
    def processAssociatedComplexIndicators(self):
        temp_selected_complex_indicators = dict()
        IDs = self.CI.config["CATEGORY"].keys()
        for ID in IDs:
            KEYs = self.CI.config["CATEGORY"][ID]["TYPES"]
            temp_selected_complex_indicators[self.CI.config["CATEGORY"][ID]["NAME"]]=[]
            for KEY,ind in zip(KEYs,range(1,len(KEYs)+1)):
                if eval("""self.CI.CI_FORM.category"""+ID+"""Type"""+str(ind)+".isChecked()"):
                    temp_selected_complex_indicators[self.CI.config["CATEGORY"][ID]["NAME"]].append(KEY)   
        temp_word_processing = {"SERIAL_NO" : self._currentWordSerial,
                                "RESPONSE_WORD":self.I_FORM.lastResponseWord.text(),
                                "COMPLEX_INDICATORS":temp_selected_complex_indicators,
                                "TIME_TAKEN":self.timerValue}
        self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"][self._currentWord] = temp_word_processing
        self._currentWordSerial +=1
    
    def setInterviewValues(self):
        pass
    
    def startInterview(self):
        pass
    
    def showTimerLCD(self):
        self.I_FORM.timerLabel.display(str(0.00))
        while(self.timerStarted and self.alive):
            self.timerValue = time.time()-self.timerStartTime
            self.timerValue *= 100
            self.timerValue = int(self.timerValue)/100.00
            time.sleep(0.2)
            self.I_FORM.timerLabel.display(str(self.timerValue))
    
if __name__=='__main__':
    pass
