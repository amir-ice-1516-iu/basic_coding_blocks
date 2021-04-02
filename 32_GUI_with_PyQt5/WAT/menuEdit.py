#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 06:03:56 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuEdit.py
"""
import json
import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

import GeneratedReport

class menuEdit_Handler(object):
    
    def __init__(self, ui, configFile="interview.json"):
        self.ui = ui
        
        self.tempConfigFile = configFile
        self.tempConfigFilePath = "temp_config"
        #self.loadInterviewConfiguration()
        
        
    def loadInterviewConfiguration(self):
        try:
            path = os.path.join(self.tempConfigFilePath,self.tempConfigFile)
            if self.ui.DEBUG_MODE:
                print("Loading : ",path)
            with open(path, "r") as fp:
                self.config = json.load(fp)
            return 1
        except Exception as eOpen:
            sys.stderr.write(self.tempConfigFile+" No such config file or directory")
            sys.stderr.write(str(eOpen))
            #sys.exit(8)
            return 0
        
    def saveUpdatedReport(self):
        try:
            path = os.path.join(self.tempConfigFilePath,self.tempConfigFile)
            if self.ui.DEBUG_MODE:
                print("Saving Updated Report")
            with open(path, "w") as fp:
                json.dump(self.config,fp,indent=4)
        except Exception as eUpdate:
            sys.stderr.write(self.tempConfigFile+" No such file or directory")
            sys.stderr.write(str(eUpdate))
            sys.exit(9)

    def Current_Interview_Result_Edit_Handler(self):#TODO
        if self.ui.DEBUG_MODE:
            print("Current Interview Result Edit Callback")
        try:
            self.ui.lastActiveWidget.close()
        except Exception as eClear:
            if self.ui.DEBUG_MODE:
                print("Unable to clear window central widget")
            sys.stderr.write(str(eClear))
            sys.exit(11)
        
        if self.loadInterviewConfiguration():
            pass
        else:
            self._showSetupSuccessDialog("Error Report file","No interview report file generated yet")
            return
        self.GRFormWidget = QtWidgets.QWidget(self.ui.centralwidget)
        #ComplexIndicatorView = QtWidgets.QWidget()         
        self.GR_FORM = GeneratedReport.Ui_Form()
        self.GR_FORM.setupUi(self.GRFormWidget)
        self.ui.mainCanvas = self.GRFormWidget
        self.ui.lastActiveWidget = self.GRFormWidget
        
        self._setReportValues()
        self.GR_FORM.updateReport.clicked.connect(self.onUpdateReportClicked)
        self.GRFormWidget.show()
        self.GR_FORM.editGeneratedReport.click()

    def Complex_Indicators_Edit_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Complex Indicators Edit Callback")
    
    def Predefined_Words_Edit_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Predefined Words Edit Callback")
    
    def Current_Interview_Details_Edit_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Current Interview Details Edit Callback")
    
    def _setReportValues(self):
        self.loadInterviewConfiguration()
        print(self.config)
        MAX_ROWS_TO_SHOW = 0
        if self.ui.DEBUG_MODE:
            print("Setting parameters")
        for Round in range(1,3):
            RoundDict = self.config["ROUND"+str(Round)+"_RESPONSES"]
            #print(RoundDict)
            StimulusWords = RoundDict.keys()
            MAX_ROWS_TO_SHOW = max(MAX_ROWS_TO_SHOW,len(StimulusWords))
            currentIndex = 0
            for key in StimulusWords:
                if type(RoundDict[key])==type(dict()):
                    if key != "EXAMPLE_WORD":
                        if Round==1:
                            self.GR_FORM.generatedReport.setItem(currentIndex,0, QtWidgets.QTableWidgetItem(key))
                            #if self.ui.DEBUG_MODE:
                            #    print(key)
                            self.GR_FORM.generatedReport.setItem(currentIndex,1, QtWidgets.QTableWidgetItem(str(RoundDict[key]["TIME_TAKEN"]*5.0)))
                            self.GR_FORM.generatedReport.setItem(currentIndex,2, QtWidgets.QTableWidgetItem(str(RoundDict[key]["TIME_TAKEN"])))
                            self.GR_FORM.generatedReport.setItem(currentIndex,3, QtWidgets.QTableWidgetItem(RoundDict[key]["RESPONSE_WORD"]))
                            #if self.ui.DEBUG_MODE:
                            #    print(RoundDict[key]["RESPONSE_WORD"])
                        elif Round==2:
                            self.GR_FORM.generatedReport.setItem(currentIndex,4, QtWidgets.QTableWidgetItem(RoundDict[key]["RESPONSE_WORD"]))
                        currentIndex += 1
            for row in range(100):
                    if row > (MAX_ROWS_TO_SHOW-3):
                        self.GR_FORM.generatedReport.hideRow(row)
    
    def _getReportValues(self):
        if self.ui.DEBUG_MODE:
            print("Getting parameters")
        for Round in range(1,3):
            RoundString = "ROUND"+str(Round)+"_RESPONSES"
            RoundDict = self.config[RoundString]
            #print(RoundDict)
            StimulusWords = RoundDict.keys()
            currentIndex = 0
            for key in StimulusWords:
                if type(RoundDict[key])==type(dict()):
                    if key != "EXAMPLE_WORD":
                        if Round==1:
                            self.config[RoundString][key]["RESPONSE_WORD"] = self.GR_FORM.generatedReport.item(currentIndex,3).text()
                            #if self.ui.DEBUG_MODE:
                            #    print(RoundDict[key]["RESPONSE_WORD"])
                        elif Round==2:
                            self.config[RoundString][key]["RESPONSE_WORD"] = self.GR_FORM.generatedReport.item(currentIndex,4).text()
                        currentIndex += 1
                        
    def onUpdateReportClicked(self):
        """ do hunky punky"""
        self._getReportValues()
        self.saveUpdatedReport()
        self._showSetupSuccessDialog("Updated Report", "Report Updated Successfully")
        self.GRFormWidget.close()
    
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
        if self.ui.DEBUG_MODE:
            print("value of pressed message box button:", retval)
	
    #def _msgbtn(i):
    #    print("Button pressed is:",i)