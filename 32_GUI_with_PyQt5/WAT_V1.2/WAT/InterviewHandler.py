#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 07:35:47 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: InterviewHandler.py
"""

from PyQt5 import QtWidgets
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
        self.wordsFileLocation = self.config["INTERVIEW_WORDS_JSON_FILE_LOCATION"]
        self._currentWordSerial = self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["CURRENT_TEST_SERIAL"]
        self.loadInterviewWords()
        self.interviewOperationStateValue = 0
        self.timerStarted = False
        self.timerValue = 0
        self.timerStartTime = 0
        self.newInterviewSubmited = False
        self.newInterviewFormShowed = False
        self.newInterviewCanceled = False
        self.alive = True
        self.resumed = False
        
        self.generateInterviewForm()
        
        self.CI_FORM = complexIndicatorHandler.ComplexIndicatorHandler(self.I_FORM)
        self.CI_FORM.generateComplexIndicatorForm()
        
        self.I_FORM.closeWidgetButton.clicked.connect(self.closeInterview)
        self.I_FORM.interviewOperationalButton.clicked.connect(self.interviewOperationalButtonHandler)
    
    def generateInterviewForm(self):
        self.InterviewForm = QtWidgets.QWidget(self.ui.centralwidget)
        #ComplexIndicatorView = QtWidgets.QWidget()         
        self.I_FORM = Interview.Ui_Form()
        self.I_FORM.setupUi(self.InterviewForm)
        self.ui.mainCanvas = self.InterviewForm
        self.ui.lastActiveWidget = self.InterviewForm
        
        self.I_FORM.timeTakenLabel.setText("")
        self.I_FORM.responseWrodLabel.setText("")
        self.I_FORM.lastResponseWord.setText("")
        self.I_FORM.testRoundLabel.setText("")
    
    def loadInterviewWords(self):
        try:
            ABS_PATH = os.path.join(self.wordsFileLocation,self.wordsFile)
            if self.ui.DEBUG_MODE:
                print("Loading E5: ",ABS_PATH)
            with open(ABS_PATH,"r") as fp:
                self.interview_words = json.load(fp)
        except Exception as eWordLoad:
            if self.ui.DEBUG_MODE:
                sys.stderr.write("Unable to load "+self.wordsFile+" file" )
                sys.stderr.write(str(eWordLoad))
            sys.exit(5)
    
    def loadInterviewConfiguration(self):
        try:
            path = os.path.join(self.configFilePath,self.configFile)
            if self.ui.DEBUG_MODE:
                print("Loading E2: ",path)
            with open(path, "r") as fp:
                self.config = json.load(fp)
                self.wordsFile = self.config["INTERVIEW_WORDS_JSON_FILE"]
                self.wordsFileLocation = self.config["INTERVIEW_WORDS_JSON_FILE_LOCATION"]
        except Exception as eOpen:
            if self.ui.DEBUG_MODE:
                sys.stderr.write(self.configFile+" No such config file or directory \n")
                sys.stderr.write(str(eOpen))
            sys.exit(2)
    
    #@staticmethod
    def setInterveiwConfiguration(self,config):
        self.config = config
        #self.saveInterviewConfiguration()
    
    def getInterviewConfiguration(self):
        return self.config
    
    def saveInterviewConfiguration(self):
        try:
            path = os.path.join(self.configFilePath,os.path.split(self.configFile)[1])
            if self.ui.DEBUG_MODE:
                print("Saving to : ",path)
            with open(path,"w") as fp:
                json.dump(self.config,fp,indent=4)
        except Exception as eSave:
            if self.ui.DEBUG_MODE:
                sys.stderr.write("Unable to write temp interveiw config file ")
                sys.stderr.write(str(eSave))
            sys.exit(4)
    
    def closeInterview(self): #TODO
        self.InterviewForm.close()
        self.newInterviewSubmited = False
        self.newInterviewFormShowed = False
        self.newInterviewCanceled = False
        self.alive = False
    
    def showInterviewPanel(self):
        self.CI_FORM.resetComplexIndicatorInput()
        
        self.CI_FORM.hideComplexIndicatorInput()
        self.I_FORM.timeTakenLabel.hide()
        self.I_FORM.responseWrodLabel.hide()
        self.I_FORM.lastResponseWord.hide()
        #self.CI.showComplexIndicatorInput()
        self._interviewMessage = "WAT Interview With "+self.config["NAME_OF_RESPONDER"]+ " of "+self.config["COMPANY_NAME"]+ " on "+self.config["DATE_OF_INTERVIEW"]
        self.I_FORM.interviewDetailsLabel.setText(self._interviewMessage)
        self.I_FORM.interviewOperationalButton.setText("Start Timer")
        if self.showNextWord():
            pass
        else:
            #TODO add message pop up
            self.closeInterview()
        self.InterviewForm.show()
    
    def showNextWord(self):
        if self.resumed:
            self.I_FORM.wordSerialNumberLabel.setText("")
            self.I_FORM.testWordLabel.setText("")
            if self.config["ROUND1_RESPONSES"]["COMPLETED"]:
                self.I_FORM.interviewOperationalButton.setText("Start/Resume 2nd Round")
            else:
                self.I_FORM.interviewOperationalButton.setText("Start/Resume 1st Round")
            self.CI_FORM.hideComplexIndicatorInput()
            self.I_FORM.timerLabel.hide()#setText("")
            self.I_FORM.timeTakenLabel.setText("")
            self.I_FORM.responseWrodLabel.setText("")
            self.I_FORM.lastResponseWord.setText("")
            self.interviewOperationStateValue = 2
            return 1
        else:
            if self.config["CURRENT_ROUND"] ==1:
                self.I_FORM.testRoundLabel.setText("First Pass")
            elif self.config["CURRENT_ROUND"] ==2:
                self.I_FORM.testRoundLabel.setText("Second Pass")
            else:
                if self.ui.DEBUG_MODE:
                    sys.stderr.write("Invalid round")
                sys.exit(6)
        if self._currentWordSerial > self.config["NUMBER_OF_WORDS_IN_TEST"]:
            print("Interview Ended")
            return 0
        self._wordSerailMessage = "Word "+str(self._currentWordSerial)
        self.I_FORM.wordSerialNumberLabel.setText(self._wordSerailMessage)
        self._currentWord = self.interview_words[str(self._currentWordSerial)]
        self.I_FORM.testWordLabel.setText("<font color='red'>"+self._currentWord+"</font>")
        return 1
        
    
    def interviewOperationalButtonHandler(self):
        self.interviewOperationStateValue +=1
        self.interviewOperationStateValue %=3
        if self.interviewOperationStateValue==1:
            self.I_FORM.interviewOperationalButton.setText("Stop Timer")
            #if self.config["CURRENT_ROUND"]==1:
            self.timerStarted = True
            self.timerStartTime = time.time()
            Thread(target=self.showTimerLCD,args=()).start()
            
            #self.I_FORM.timerLabel.show()
            
            self.I_FORM.timeTakenLabel.hide()
            self.I_FORM.responseWrodLabel.hide()
            self.I_FORM.lastResponseWord.hide()
            
        elif self.interviewOperationStateValue==2:
            self.timerStarted = False
            if self.ui.DEBUG_MODE:
                print("Time taken for response : ",self.timerValue," S")
            self.I_FORM.interviewOperationalButton.setText("Submit->Next")
            self.CI_FORM.showComplexIndicatorInput()
            self.I_FORM.timeTakenLabel.setText("Time Taken        : "+str(self.timerValue)+ " Seconds")
            self.I_FORM.timeTakenLabel.show()
            self.I_FORM.lastResponseWord.setText("")
            self.I_FORM.responseWrodLabel.show()
            self.I_FORM.lastResponseWord.show()
            
        elif self.interviewOperationStateValue==0:
            if self.resumed:
                self.resumed = False
                if self.showNextWord():
                    pass
                else:
                    #TODO add popup message
                    self.closeInterview()
                self.I_FORM.interviewOperationalButton.setText("Start Timer")
                return
            
            self.saveInterviewConfiguration()
            self.I_FORM.interviewOperationalButton.setText("Start Timer")
            self.processResponse()
            if self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["COMPLETED"]:
                if self.config["CURRENT_ROUND"]==2:
                    pass
                else:
                    if self.showNextWord():
                        pass
                    else: 
                        #TODO add popup message
                        self.closeInterview()
            else:
                if self.showNextWord():
                    pass
                else:
                    #TODO add popup message
                    self.closeInterview()
            self.CI_FORM.hideComplexIndicatorInput()
            self.I_FORM.timerLabel.display(str(0.00))
            self.I_FORM.timeTakenLabel.hide()
            self.I_FORM.responseWrodLabel.hide()
            self.I_FORM.lastResponseWord.hide()
    
    def processResponse(self):
        
        if self._currentWordSerial == self.config["NUMBER_OF_WORDS_IN_TEST"]:
            if self.config["CURRENT_ROUND"] == 1:
                self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["COMPLETED"] = 1
                self.processAssociatedComplexIndicators()
                self.config["CURRENT_ROUND"]=2
                self._currentWordSerial = 1
                self.resumed = True
                if self.ui.DEBUG_MODE:
                    print("First pass completed")
                self._showSetupSuccessDialog("Round Complete","Round 1 Completed \n Please take rest and we will start \n for next round with new words")
                self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["CURRENT_TEST_SERIAL"] = self._currentWordSerial
                if self.ui.DEBUG_MODE:
                    print("CTS: "+str(self._currentWordSerial))
                    print("CR: "+str(self.config["CURRENT_ROUND"]))
                    print("CR1:"+str(self.config["ROUND1_RESPONSES"]["COMPLETED"]))
                    print("CR2:"+str(self.config["ROUND2_RESPONSES"]["COMPLETED"]))
                self.saveInterviewConfiguration()
                self.CI_FORM.resetComplexIndicatorInput()
                return
            elif self.config["CURRENT_ROUND"]==2:
                self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["COMPLETED"] = 1
                self.processAssociatedComplexIndicators()
                self.config["INTERVIEW_COMPLETED"] = 1
                #self.saveInterviewConfiguration()
                self.closeInterview()
                if self.ui.DEBUG_MODE:
                    print("Interview completed waiting for report to generate")
                #return
            else:
                if self.ui.DEBUG_MODE:
                    sys.stderr.write("Something wrong happened invalid current round")
                sys.exit(7)
        else:
            self.processAssociatedComplexIndicators()
            
        self.config["ROUND"+str(self.config["CURRENT_ROUND"])+"_RESPONSES"]["CURRENT_TEST_SERIAL"] = self._currentWordSerial
        if self.ui.DEBUG_MODE:
            print("CTS: "+str(self._currentWordSerial))
            print("CR: "+str(self.config["CURRENT_ROUND"]))
            print("CR1:"+str(self.config["ROUND1_RESPONSES"]["COMPLETED"]))
            print("CR2:"+str(self.config["ROUND2_RESPONSES"]["COMPLETED"]))
        self.saveInterviewConfiguration()     
        self.CI_FORM.resetComplexIndicatorInput()
    
    def processAssociatedComplexIndicators(self):
        temp_selected_complex_indicators = dict()
        IDs = self.CI_FORM.config["CATEGORY"].keys()
        for ID in IDs:
            KEYs = self.CI_FORM.config["CATEGORY"][ID]["TYPES"]
            temp_selected_complex_indicators[self.CI_FORM.config["CATEGORY"][ID]["NAME"]]=[]
            for KEY,ind in zip(KEYs,range(1,len(KEYs)+1)):
                if eval("""self.CI_FORM.CI_FORM.category"""+ID+"""Type"""+str(ind)+".isChecked()"):
                    temp_selected_complex_indicators[self.CI_FORM.config["CATEGORY"][ID]["NAME"]].append(KEY)   
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
        self.I_FORM.timerLabel.show()
        self.I_FORM.timerLabel.display(str(0.00))
        while(self.timerStarted and self.alive):
            self.timerValue = time.time()-self.timerStartTime
            self.timerValue *= 100
            self.timerValue = int(self.timerValue)/100.00
            time.sleep(0.1)
            self.I_FORM.timerLabel.display(str(self.timerValue))

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
    
if __name__=='__main__':
    pass
