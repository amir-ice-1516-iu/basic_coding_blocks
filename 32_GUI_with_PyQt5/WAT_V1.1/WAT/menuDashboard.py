#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 06:06:31 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuDashboard.py
"""

import json
import os
import sys
from PyQt5 import QtWidgets #,QtCore, QtGui
import copy
from matplotlib import pyplot as plt

from ListToIMAGE import ListToIMAGE


class menuDashboard_Handler(object): #TODO
    
    def __init__(self, ui, configFile="generatedReport.json", interviewConfigFile="interview.json"):#TODO
        self.ui = ui
        self.configFile = configFile
        self.refInterviewConfigFile="generatedReport.json"
        self.configFilePath = "temp_config"
        self.refInterviewConfigFilePath = "config"
        self.tempConfigFile = copy.copy(self.configFile)
        self.tempConfigFilePath = "temp_config"
        self.interviewConfigFile = interviewConfigFile
        self.imageFileToSave = "WAT_Default.png"
        self.imageFileLocation = "reports"
        
    def Generate_Report_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Generate Report Callback")
        if self._crossCheckInterview():#TODO
            self._saveInterviewReport()
            self._showMessageDialog("Succeed","Report Generated Successfully")
            #call View Report From here
        else:
            if self.ui.DEBUG_MODE:
                print("Unable to Generate Report")
            return
        
    def _crossCheckInterview(self):
        if self.loadInterviewConfiguration():
            pass
        else:
            self._showMessageDialog("Failed", "Unable to load config file: "+self.interviewConfigFile)
            return 0
        if self.loadInterviewReport(ref=True):
            pass
        else:
            self._showMessageDialog("Failed", "Unable to load report file: "+self.tempConfigFile)
            return 0
        
        self.reportConfig["NAME_OF_RESPONDER"] = self.config["NAME_OF_RESPONDER"]
        self.reportConfig["COMPANY_NAME"] = self.config["COMPANY_NAME"]
        self.reportConfig["INTERVIEWED_BY"] = self.config["INTERVIEWED_BY"]
        self.reportConfig["NUMBER_OF_WORDS_IN_TEST"] = self.config["NUMBER_OF_WORDS_IN_TEST"]
        self.reportConfig["DATE_OF_INTERVIEW"] = self.config["DATE_OF_INTERVIEW"]
        
        for Round in range(1,3):
            RoundString = "ROUND"+str(Round)+"_RESPONSES"
            RoundReportString = "ROUND"+str(Round)
            RoundDict = copy.deepcopy(self.config[RoundString])
            #print(RoundDict)
            ReactionTimes = []
            self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["1"]=list()#[] #.append(RoundDict[key]["COMPLEX_INDICATORS"]["Reaction Time"])
            self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["2"]=list()#[] #.append(RoundDict[key]["COMPLEX_INDICATORS"]["Meaning"])
            self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["3"]=list()#[] #.append(RoundDict[key]["COMPLEX_INDICATORS"]["Physical Reactions"])
            self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["4"]=list()#[] #.append(RoundDict[key]["COMPLEX_INDICATORS"]["Speech"])
            self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["5"]=list()#[] #.append(RoundDict[key]["COMPLEX_INDICATORS"]["Patterns"])
            self.reportConfig[RoundReportString]["REACTION_TIME"]               =list()#[] #.append(RoundDict[key]["TIME_TAKEN"])
                    
            if Round==1:
                self.reportConfig["SCORES"]["SL"]                                   =list()#[] #.append(RoundDict[key]["SERIAL_NO"])                        
                self.reportConfig["SCORES"]["S_WORDS"]                              =list()#[] #.append(key)
                self.reportConfig[RoundReportString]["REACTION"]                    =list()#[] #.append(RoundDict[key]["RESPONSE_WORD"])
            
            for key in RoundDict.keys():
                if type(RoundDict[key])==type(dict()):
                    if key=="EXAMPLE_WORD":
                        continue
                    #if self.ui.DEBUG_MODE:
                    #    print(RoundDict[key]["COMPLEX_INDICATORS"])
                    ReactionTimes.append(RoundDict[key]["TIME_TAKEN"])
                    self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["1"].append(RoundDict[key]["COMPLEX_INDICATORS"]["Reaction Time"])
                    self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["2"].append(RoundDict[key]["COMPLEX_INDICATORS"]["Meaning"])
                    self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["3"].append(RoundDict[key]["COMPLEX_INDICATORS"]["Physical Reactions"])
                    self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["4"].append(RoundDict[key]["COMPLEX_INDICATORS"]["Speech"])
                    self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["5"].append(RoundDict[key]["COMPLEX_INDICATORS"]["Patterns"])
                    self.reportConfig[RoundReportString]["REACTION_TIME"].append(RoundDict[key]["TIME_TAKEN"])
                    if Round==1:
                        self.reportConfig["SCORES"]["SL"].append(RoundDict[key]["SERIAL_NO"])
                        #if self.ui.DEBUG_MODE:
                        #    print(self.reportConfig["SCORES"]["SL"])
                        self.reportConfig["SCORES"]["S_WORDS"].append(key)
                        self.reportConfig[RoundReportString]["REACTION"].append(RoundDict[key]["RESPONSE_WORD"])
                    elif Round==2:
                        self.reportConfig[RoundReportString]["REACTION"].append(RoundDict[key]["RESPONSE_WORD"])

            MedianPRT = self._calculateMedian(ReactionTimes)
            self.config[RoundString]["MEDIAN_PRT"] = MedianPRT
            self.reportConfig[RoundReportString]["MEDIAN_PRT"] = MedianPRT
            #if self.ui.DEBUG_MODE:
            #    print(self.reportConfig)
        tempTotalWords = len(self.reportConfig["ROUND1"]["REACTION_TIME"])
        if tempTotalWords==len(self.reportConfig["ROUND2"]["REACTION_TIME"]): # checking wheather report can be produced or has enough info to report
            # Column 4, 5, 6, 7, 8, 9, 10 Scores
            self.reportConfig["SCORES"]["R_T_5TH"] = ["0"]*tempTotalWords
            self.reportConfig["SCORES"]["R_WORDS"] = ["0"]*tempTotalWords
            self.reportConfig["SCORES"]["R_P_WORDS"] = ["0"]*tempTotalWords
            self.reportConfig["SCORES"]["BODY_REAC"] = ["0"]*tempTotalWords
            self.reportConfig["SCORES"]["OVER_PM"] = ["0"]*tempTotalWords
            self.reportConfig["SCORES"]["RE"]= ["0"]*tempTotalWords
            self.reportConfig["SCORES"]["LANGUAGE"] = ["0"]*tempTotalWords
            self.reportConfig["SCORES"]["OTHER"] = ["0"]*tempTotalWords
            # Column 3 Scores
            self.reportConfig["SCORES"]["R_T_SEC"] = self.reportConfig["ROUND1"]["REACTION_TIME"]
            # Column 4, 5, 6, 7, 8, 9, 10 Scores
            for row in range(tempTotalWords):
                logic4 = "F" in self.reportConfig["ROUND1"]["COMPLEX_INDICATOR_TYPES"]["1"][row] #or self.reportConfig["ROUND2"]["COMPLEX_INDICATOR_TYPES"]["1"] 
                logic5 = self.reportConfig["ROUND1"]["REACTION"][row] == self.reportConfig["ROUND2"]["REACTION"][row]
                CIT1 = self.reportConfig["ROUND1"]["COMPLEX_INDICATOR_TYPES"]["3"] 
                logic6 = "GBM" in CIT1 or "PE" in CIT1 
                logic7 = self.reportConfig["ROUND2"]["REACTION_TIME"][row] > self.reportConfig["ROUND1"]["MEDIAN_PRT"] or self.reportConfig["ROUND2"]["REACTION_TIME"][row] > self.reportConfig["ROUND2"]["MEDIAN_PRT"] 
                logic8 = logic5 #Logic not given to me
                R1C4 = self.reportConfig["ROUND1"]["COMPLEX_INDICATOR_TYPES"]["4"]
                logic9 = "FLR" in R1C4 or "MW" in R1C4 or "ST" in R1C4 or "SMP" in R1C4 or "SO" in R1C4
                R1C2 = self.reportConfig["ROUND1"]["COMPLEX_INDICATOR_TYPES"]["2"]
                R1C5 = self.reportConfig["ROUND1"]["COMPLEX_INDICATOR_TYPES"]["5"]
                logic10_a = "MLR" in R1C2 or "MS" in R1C2 or "RSW" in R1C2 or "MR" in R1C2 or "RWC" in R1C2 or "FR" in R1C2
                logic10_b = "P" in R1C5 or "S" in R1C5
                #Column2
                self.reportConfig["SCORES"]["R_T_5TH"][row] = self.reportConfig["SCORES"]["R_T_SEC"][row]*5
                #Column4
                if logic4:
                    self.reportConfig["SCORES"]["R_WORDS"][row] = "2"
                #Column5
                if logic5:
                    self.reportConfig["SCORES"]["R_P_WORDS"][row] = "1"
                #Column6 Body Reaction
                if logic6:
                    self.reportConfig["SCORES"]["BODY_REAC"][row] = "1"
                #Column7 Over Prolonged reaction time Median:
                if logic7:
                    self.reportConfig["SCORES"]["OVER_PM"][row] = "1"
                #Column8 Invalid reproduction of response word
                if logic8:
                    self.reportConfig["SCORES"]["RE"][row] = "1"
                #Column9 Language Reaction
                if logic9:
                    self.reportConfig["SCORES"]["LANGUAGE"][row] = "1"
                #Column10 Other Reactions
                if logic10_a or logic10_b:
                    self.reportConfig["SCORES"]["OTHER"][row] = "1"
           
            
            #Column 11 CI_Scores in total
            self.reportConfig["SCORES"]["CI_S"] = ["0"]*tempTotalWords
            self.reportConfig["SCORES"]["F"] = [" "]*tempTotalWords
            self.reportConfig["SCORES"]["E"] = [" "]*tempTotalWords
            for row in range(tempTotalWords):
                CI_SCORE = 0
                CI_SCORE += int(self.reportConfig["SCORES"]["OVER_PM"][row])
                CI_SCORE += int(self.reportConfig["SCORES"]["RE"][row])
                CI_SCORE += int(self.reportConfig["SCORES"]["LANGUAGE"][row])
                CI_SCORE += int(self.reportConfig["SCORES"]["OTHER"][row])
                self.reportConfig["SCORES"]["CI_S"][row] = str(CI_SCORE)
            self.reportConfig["IS_READY_TO_GENERATE_GRAPH"] = 1
        else:
            self._showMessageDialog("Status Pending", "Interview Not Completed Yet")
            return 0
        return 1      
    
    def _takeFileName(self):#TODO
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, d = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget,"QFileDialog.getSaveFileName()","","WAT Interview (*.png);;All Files (*)", options=options)
        #file_name = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget, 'Save File')
        if len(fileName):
            #self.newInterview.closeInterview()
            path, filename = os.path.split(fileName)
            if filename:
                self.imageFileToSave = filename
                self.imageFileLocation = path
                return 1
            else:
                return 0
        else:
            return 0
    
    def Export_Report_To_Png_Handler(self):
        if self.ui.DEBUG_MODE:
            print(" Export Generated Report To png Handler callback")
        if self._takeFileName():
            pass
        else:
            if self.ui.DEBUG_MODE:
                print("Invalid File or canceled")
            return
        
        #self.loadInterviewReport()
        try:
            if self.reportConfig["IS_READY_TO_GENERATE_GRAPH"]:
                Obj = ListToIMAGE()
                ABS_Path = os.path.join(self.imageFileLocation,self.imageFileToSave)
                Obj.setImageFileName(ABS_Path)
                L = []
                Cols = list(self.reportConfig["SCORES"].keys())
                Pad = []
                for i in range(65,79):
                    #Col.append(str(chr(i))*9)
                    Pad.append("_"*9)
                Obj.setColumLabels([Pad,Cols,Pad])
                #Obj.setAlignment("LEFT")
                Obj.setAlignment("CENTER")
                #Obj.setAlignment("RIGHT")
                
                for row in range(self.reportConfig["NUMBER_OF_WORDS_IN_TEST"]):
                    tempRow = []
                    for col in Cols:
                        if col=="R_WORDS":
                            tempRow.append(self.reportConfig["ROUND1"]["REACTION"][row])
                        elif col=="R_P_WORDS":
                            tempRow.append(self.reportConfig["ROUND2"]["REACTION"][row])
                        else:
                            tempRow.append(self.reportConfig["SCORES"][col][row])
                    L.append(tempRow)
                    L.append(Pad)
                if self.ui.DEBUG_MODE:
                    print("Build End")
                Obj.setFontSize(50)
                #for i in range(len(Obj.FONTS)):
                #    Obj.FONT_INDEX = i
                #    Obj.setImageFileName(ABS_Path[:-4]+"_FONT_"+str(i)+ABS_Path[-4:])
                Obj.generateImage(L)
                if self.ui.DEBUG_MODE:
                    print("Saving End")
                
                
                Height_ROUND1 = self.reportConfig["ROUND1"]["REACTION_TIME"]
                Height_ROUND2 = self.reportConfig["ROUND2"]["REACTION_TIME"]
                Domain_S_WORDS = self.reportConfig["SCORES"]["S_WORDS"]
                Domain_RESPONSE = self.reportConfig["ROUND1"]["REACTION"]
                Domain_REPRODUCTION = self.reportConfig["ROUND2"]["REACTION"]
                Domain_X1 = []
                Domain_X2 = []
                Colors1 = ["green"]*len(Height_ROUND1)
                Colors2 = ["green"]*len(Height_ROUND2)
                
                for i in range(len(Domain_S_WORDS)):
                    Domain_X1.append(Domain_S_WORDS[i]+"\n"+Domain_RESPONSE[i])
                    if Height_ROUND1[i] >= self.reportConfig["ROUND1"]["MEDIAN_PRT"]:
                        Colors1[i] = "red"
                for i in range(len(Domain_S_WORDS)):
                    Domain_X2.append(Domain_S_WORDS[i]+"\nRP:"+Domain_REPRODUCTION[i])
                    if Height_ROUND2[i] >= self.reportConfig["ROUND1"]["MEDIAN_PRT"]:                
                        Colors2[i] = "red"
                
                y = [self.reportConfig["ROUND1"]["MEDIAN_PRT"]]*len(Domain_S_WORDS)
                plt.bar(Domain_RESPONSE, Height_ROUND1, color=Colors1)
                plt.plot(range(len(Domain_S_WORDS)),y)
                plt.xticks(rotation=90)
                plt.yticks(rotation=90)
                plt.savefig(ABS_Path[:-4]+"Graph_Round1"+ABS_Path[-4:])
                
                #plt.clear()
                if self.ui.DEBUG_MODE:
                    print("Plot1 End")
                
                plt.bar(Domain_REPRODUCTION, Height_ROUND2, color=Colors2)
                plt.plot(range(len(Domain_S_WORDS)),y)
                plt.xticks(rotation=90)
                plt.yticks(rotation=90)
                plt.savefig(ABS_Path[:-4]+"Graph_Round2"+ABS_Path[-4:])
                if self.ui.DEBUG_MODE:
                    print("Plot2 End")
                
                self._showMessageDialog(" Exported Successfuly","Exported to png successffully")
        except Exception as eExportPng:
            if self.ui.DEBUG_MODE:
                sys.stderr.write("Unable to Export")
                sys.stderr.write(str(eExportPng))
            self._showMessageDialog(" Denied ", "Failed to Export")
    
    def _calculateMedian(self,values):
        SortedValues = sorted(values)
        Length = len(SortedValues)
        Index = Length//2
        if Length>=2:
            if Length%2==0:
                if self.ui.DEBUG_MODE:
                    print("Median Index: ",str(Index)," ",str(Index-1))
                return (SortedValues[Index]+SortedValues[Index-1])/2.0
            else:
                if self.ui.DEBUG_MODE:
                    print("Median Index: ",str(Index))
                return SortedValues[Index]
        else:
            return 0.0
    
    def loadInterviewReport(self, ref=False):
        try:
            if ref:
                ABS_PATH = os.path.join(self.refInterviewConfigFilePath,self.refInterviewConfigFile)
            else:
                ABS_PATH = os.path.join(self.tempConfigFilePath,self.tempConfigFile)
            if self.ui.DEBUG_MODE:
                print("Loading D8: ",ABS_PATH)
            with open(ABS_PATH, "r") as fp:
                self.reportConfig = json.load(fp)
            return 1
        except Exception as eOpen:
            if self.ui.DEBUG_MODE:
                sys.stderr.write(self.tempConfigFile+" No such config file or directory")
                sys.stderr.write(str(eOpen))
            #sys.exit(8)
            return 0
        
    def loadInterviewConfiguration(self):
        try:
            
            ABS_PATH = os.path.join(self.tempConfigFilePath,self.interviewConfigFile)
            if self.ui.DEBUG_MODE:
                print("Loading D5: ",ABS_PATH)
            with open(ABS_PATH,"r") as fp:
                self.config = json.load(fp)
                #self.wordsFile = self.config["INTERVIEW_WORDS_JSON_FILE"]
                #self.wordsFileLocation = self.config["INTERVIEW_WORDS_JSON_FILE_LOCATION"]
            return 1
        except Exception as eWordLoad:
            if self.ui.DEBUG_MODE:
                sys.stderr.write("Unable to load ",self.wordsFile," file" )
                sys.stderr.write(str(eWordLoad))
            #sys.exit(5)
            return 0
    
    def Save_Generated_Report_Handler(self):
        if self.ui.DEBUG_MODE:
            print("Save Generated Report Handler callback....")
        if self._crossCheckInterview():#TODO
            self._saveInterviewReport()
            self._showMessageDialog("Succeed","Report Generated & Saved Successfully")
            #call View Report From here
        else:
            if self.ui.DEBUG_MODE:
                print("Unable to Generate Report & Save")
    
    def _saveInterviewReport(self):
        try:
            ABS_PATH = os.path.join(self.tempConfigFilePath,self.tempConfigFile)
            if self.ui.DEBUG_MODE:
                print("Saving D8: ",ABS_PATH)
            with open(ABS_PATH, "w") as fp:
                json.dump(self.reportConfig,fp,indent=4)
            return 1
        except Exception as eOpen:
            if self.ui.DEBUG_MODE:
                sys.stderr.write(self.tempConfigFile+" Unable to Save Generated Report")
                sys.stderr.write(str(eOpen))
            #sys.exit(8)
            return 0
    
    def getGeneratedReport(self):
        self.loadInterviewReport()
        return self.reportConfig
    
    def _showMessageDialog(self,title, message):
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
