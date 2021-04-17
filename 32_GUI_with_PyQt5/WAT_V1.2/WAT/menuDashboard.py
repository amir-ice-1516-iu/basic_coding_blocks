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
# from matplotlib import pyplot as plt

from ListToIMAGE import ListToIMAGE
from menuView import  menuView_Handler


class menuDashboard_Handler(object): #TODO
    
    def __init__(self, ui, configFile="generatedReport.json", interviewConfigFile="interview.json"):#TODO
        self.ui = ui
        self.configFile = configFile
        self.refInterviewConfigFile= ui.configFile
        self.tempReportConfigFile = ui.tempReportConfigFile
        self.refReportConfigFile = ui.reportConfigFile
        self.interviewConfigFile = ui.tempConfigFile
        self.imageFileToSave = "WAT_Default.png"
        self.imageFileLocation = "reports"
        
        try:
            self.loadInterviewReport()
        except Exception as eLoadReport:
            assert("Unable to Load report "+str(eLoadReport))
            
        try:
            self.loadInterviewConfiguration()
        except Exception as eLoadInterview:
            assert("Unable to load interview "+str(eLoadInterview))
        
    def Generate_Report_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Generate Report Callback")
        if self._crossCheckInterview():#TODO
            self._saveInterviewReport()
            self._showMessageDialog("Succeed","Report Generated Successfully")
            Obj = menuView_Handler(self.ui)
            Obj.Last_Interview_Report_View_Handler()
            return 1
            #call View Report From here
        else:
            if self.ui.DEBUG_MODE:
                print("Unable to Generate Report")
            return 0

    def _tempRefil(self,Obj,tempTotalWords,default_value):
        tl = len(Obj)
        if tl < tempTotalWords:
            for _ in range(tempTotalWords - tl):
                Obj.append(default_value)
                print("appended : "+default_value)

    def _crossCheckInterview(self):
        if self.loadInterviewConfiguration():
            pass
        else:
            self._showMessageDialog("Failed", "Unable to load config file: "+self.interviewConfigFile)
            return 0
        if self.loadInterviewReport(ref=False): #previous was True
            pass
        else:
            self._showMessageDialog("Failed", "Unable to load report file: "+self.tempReportConfigFile)
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
            ReactionTimes = []
            self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["1"]= list()
            self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["2"]= list()
            self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["3"]= list()
            self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["4"]= list()
            self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["5"]= list()
            self.reportConfig[RoundReportString]["REACTION_TIME"]               = list()
            self.reportConfig[RoundReportString]["REACTION"]                    = list()
            if Round==1:
                self.reportConfig["SCORES"]["SL"]                                   = list()
                self.reportConfig["SCORES"]["S_WORDS"]                              = list()

            for key in RoundDict.keys():
                if type(RoundDict[key])==type(dict()):
                    if key=="EXAMPLE_WORD":
                        continue
                    ReactionTimes.append(RoundDict[key]["TIME_TAKEN"])
                    self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["1"].append(RoundDict[key]["COMPLEX_INDICATORS"]["Reaction Time"])
                    self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["2"].append(RoundDict[key]["COMPLEX_INDICATORS"]["Meaning"])
                    self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["3"].append(RoundDict[key]["COMPLEX_INDICATORS"]["Physical Reactions"])
                    self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["4"].append(RoundDict[key]["COMPLEX_INDICATORS"]["Speech"])
                    self.reportConfig[RoundReportString]["COMPLEX_INDICATOR_TYPES"]["5"].append(RoundDict[key]["COMPLEX_INDICATORS"]["Patterns"])
                    self.reportConfig[RoundReportString]["REACTION_TIME"].append(RoundDict[key]["TIME_TAKEN"])
                    if Round==1:
                        self.reportConfig["SCORES"]["SL"].append(RoundDict[key]["SERIAL_NO"])
                        self.reportConfig["SCORES"]["S_WORDS"].append(key)
                        self.reportConfig[RoundReportString]["REACTION"].append(RoundDict[key]["RESPONSE_WORD"])
                    elif Round==2:
                        self.reportConfig[RoundReportString]["REACTION"].append(RoundDict[key]["RESPONSE_WORD"])

            MedianPRT = self._calculateMedian(ReactionTimes)
            self.config[RoundString]["MEDIAN_PRT"] = MedianPRT
            self.reportConfig[RoundReportString]["MEDIAN_PRT"] = MedianPRT
        tempTotalWords = len(self.reportConfig["ROUND1"]["REACTION_TIME"])
        if tempTotalWords==len(self.reportConfig["ROUND2"]["REACTION_TIME"]): # checking wheather report can be produced or has enough info to report
            # Column 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 Scores
            self._tempRefil(self.reportConfig["SCORES"]["R_T_5TH"]      , tempTotalWords,"-")
            self._tempRefil(self.reportConfig["SCORES"]["R_WORDS"]      , tempTotalWords, " ")
            self._tempRefil(self.reportConfig["SCORES"]["R_P_WORDS"]    , tempTotalWords, " ")
            for i, key in enumerate(self.reportConfig["SCORES"].keys()):
                if i >= 6 and i <= 15:
                    self._tempRefil(self.reportConfig["SCORES"][key]          , tempTotalWords, " ")
            self._tempRefil(self.reportConfig["SCORES"]["TOTAL"]        , tempTotalWords, "0")
            self._tempRefil(self.reportConfig["SCORES"]["FACTUAL"]      , tempTotalWords, " ")
            self._tempRefil(self.reportConfig["SCORES"]["EGO_CENTRIC"]  , tempTotalWords, " ")
            # Column 3, 4, 5 Scores
            self.reportConfig["SCORES"]["R_T_SEC"]      = self.reportConfig["ROUND1"]["REACTION_TIME"]
            self.reportConfig["SCORES"]["R_WORDS"]      = self.reportConfig["ROUND1"]["REACTION"]
            self.reportConfig["SCORES"]["R_P_WORDS"]    = self.reportConfig["ROUND2"]["REACTION"]
            # Column 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17 Scores
            for row in range(tempTotalWords):
                SW = self.reportConfig["SCORES"]["S_WORDS"][row]
                logic6 = self.reportConfig["ROUND1"]["REACTION_TIME"][row] > self.reportConfig["ROUND1"]["MEDIAN_PRT"]
                logic7 = self.config["ROUND1_RESPONSES"][SW] == self.config["ROUND2_RESPONSES"][SW]
                logic8 = "B"   in self.config["ROUND1_RESPONSES"][SW]["COMPLEX_INDICATORS"]["Physical Reactions"]
                logic9 = "MS"  in self.config["ROUND1_RESPONSES"][SW]["COMPLEX_INDICATORS"]["Meaning"]
                logic10= "RSW" in self.config["ROUND1_RESPONSES"][SW]["COMPLEX_INDICATORS"]["Meaning"]
                logic11= "SO"  in self.config["ROUND1_RESPONSES"][SW]["COMPLEX_INDICATORS"]["Speech"]
                logic12= "MW"  in self.config["ROUND1_RESPONSES"][SW]["COMPLEX_INDICATORS"]["Speech"]
                logic13 = "F"  in self.config["ROUND1_RESPONSES"][SW]["COMPLEX_INDICATORS"]["Reaction Time"]
                logic14 = "S"  in self.config["ROUND1_RESPONSES"][SW]["COMPLEX_INDICATORS"]["Patterns"]
                logic15 = "P"  in self.config["ROUND1_RESPONSES"][SW]["COMPLEX_INDICATORS"]["Patterns"]
                logics = [logic6, logic7, logic8, logic9, logic10, logic11, logic12, logic13, logic14, logic15]
                # Column2 R_T_5TH:
                self.reportConfig["SCORES"]["R_T_5TH"][row] = int((self.reportConfig["SCORES"]["R_T_SEC"][row]*5)+0.5)
                current_logic = 0
                temp_Counter = 0
                for i,key in enumerate(self.reportConfig["SCORES"].keys()):
                    if i>=6 and i<=15:
                        if logics[current_logic]:
                            self.reportConfig["SCORES"][key][row] = key
                        if self.reportConfig["SCORES"][key][row] != " ":
                            if i==13:
                                temp_Counter += 2
                            else:
                                temp_Counter += 1
                        current_logic += 1
                # Column16
                self.reportConfig["SCORES"]["TOTAL"][row] = str(temp_Counter)
            self.reportConfig["IS_READY_TO_GENERATE_GRAPH"] = 1
        else:
            self._showMessageDialog("Status Pending", "Interview Not Completed Yet")
            return 0
        return 1      
    
    def _takeFileName(self):#TODO
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, d = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget,"QFileDialog.getSaveFileName()","","WAT Interview (*.png);;All Files (*)", options=options)
        if len(fileName):
            path, filename = os.path.split(fileName)
            if filename:
                self.imageFileToSave = filename
                self.imageFileLocation = path
                return 1
            else:
                return 0
        else:
            return 0

    def _doPadding(self,word,Length,symbol="-"):
        spaces = ""
        if len(word)<Length:
            spaces = symbol*(Length-len(word))
        return word+spaces

    def _sortRows(self, ListArray):
        tempArray = []
        for rowIndex1, row1 in enumerate(ListArray):
            for rowIndex2, row2 in enumerate(ListArray):
                try:
                    if int(ListArray[rowIndex1][-3]) > int(ListArray[rowIndex2][-3]):
                        tempArray = copy.deepcopy(ListArray[rowIndex1])
                        ListArray[rowIndex1] = copy.deepcopy(ListArray[rowIndex2])
                        ListArray[rowIndex2] = copy.deepcopy(tempArray)
                except Exception as eStr:
                    pass
        print(ListArray)
        return ListArray

    def Export_Report_To_Png_Handler(self):
        if self.ui.DEBUG_MODE:
            print(" Export Generated Report To png Handler callback")
        if self._takeFileName():
            pass
        else:
            if self.ui.DEBUG_MODE:
                print("Invalid File or canceled")
            return
        
        self.loadInterviewReport()
        # try:
        if self.reportConfig["IS_READY_TO_GENERATE_GRAPH"]:
            Obj = ListToIMAGE(fontFilePath=self.ui.fontFilesPath)
            # Obj.setFontFilePath(self.ui.fontFilesPath)
            ABS_Path = os.path.join(self.imageFileLocation,self.imageFileToSave)
            Obj.setImageFileName(ABS_Path)
            Obj.numberOfLinesPerPage = 40
            L = []
            Cols = list(self.reportConfig["SCORES"].keys())
            dummyCols = copy.deepcopy(Cols)
            # dummyCols[6] = "COM"
            # dummyCols[7] = "PL"
            # dummyCols[8] = "E"
            # dummyCols[9] = "X"
            # dummyCols[10] = "IND"
            # dummyCols[11] = "IC"
            # dummyCols[12] = "AT"
            # dummyCols[13] = "O"
            # dummyCols[14] = "R"
            # dummyCols[15] = "S"
            Pad = []
            for i in range(len(Cols)):
                Pad.append("_"*len(Cols[i]))
            Obj.setColumLabels([Pad,dummyCols,Pad])
            Obj.setAlignment("CENTER")
            for row in range(self.reportConfig["NUMBER_OF_WORDS_IN_TEST"]):
                tempRow = []
                for colIndex,col in enumerate(Cols):
                    if col=="R_WORDS":
                        tempRow.append(self.reportConfig["ROUND1"]["REACTION"][row])
                    elif col=="R_P_WORDS":
                        tempRow.append(self.reportConfig["ROUND2"]["REACTION"][row])
                    else:
                        tempRow.append(self.reportConfig["SCORES"][col][row])
                    if len(Pad[colIndex]) < len(str(tempRow[-1])):
                        Pad[colIndex] = self._doPadding(Pad[colIndex],len(str(tempRow[-1])),"_")
                L.append(tempRow)
                L.append(Pad)
            if self.ui.DEBUG_MODE:
                print("Build End1")
            Obj.setFontSize(50)
            Obj.generateImage(L)
            if self.ui.DEBUG_MODE:
                print("Saving End1")

            Obj = ListToIMAGE(fontFilePath=self.ui.fontFilesPath)
            Obj.setImageFileName(ABS_Path[:-4]+str("R2")+ABS_Path[-4:])
            L = []
            Pad = []
            for i in range(len(Cols)):
                Pad.append("_" * len(Cols[i]))
            Labels = ["","","","","Words","With","2","","","","","or","","","","","more","points",""]
            Obj.setColumLabels([Pad,Labels,Pad,dummyCols,Pad])
            Obj.setAlignment("CENTER")
            for row in range(self.reportConfig["NUMBER_OF_WORDS_IN_TEST"]):
                tempRow = []
                if int(self.reportConfig["SCORES"]["TOTAL"][row]) >= 2:
                    for colIndex,col in enumerate(Cols):
                        if col=="R_WORDS":
                            tempRow.append(self.reportConfig["ROUND1"]["REACTION"][row])
                        elif col=="R_P_WORDS":
                            tempRow.append(self.reportConfig["ROUND2"]["REACTION"][row])
                        else:
                            tempRow.append(self.reportConfig["SCORES"][col][row])
                        if len(Pad[colIndex]) < len(str(tempRow[-1])):
                            Pad[colIndex] = self._doPadding(Pad[colIndex], len(str(tempRow[-1])), "_")
                    L.append(tempRow)
                    L.append(Pad)


            Obj.setFontSize(50)
            L = self._sortRows(L)
            Obj.generateImage(L)
            if self.ui.DEBUG_MODE:
                print("Build End2")

            Obj = ListToIMAGE(fontFilePath=self.ui.fontFilesPath)
            Obj.setImageFileName(ABS_Path[:-4]+str("Stereos")+ABS_Path[-4:])
            L = []
            Pad = []
            for i in range(len(Cols)):
                Pad.append("_" * len(Cols[i]))
            Labels = ["","","Words","With","stereo","types","","","","","","in","","","","","any","round",""]
            Obj.setColumLabels([Pad,Labels,Pad,dummyCols,Pad])
            Obj.setAlignment("CENTER")
            for row in range(self.reportConfig["NUMBER_OF_WORDS_IN_TEST"]):
                tempRow = []
                l1 = "S" in self.reportConfig["ROUND1"]["COMPLEX_INDICATOR_TYPES"]["5"][row]
                l2 = "S" in self.reportConfig["ROUND2"]["COMPLEX_INDICATOR_TYPES"]["5"][row]
                if l1 or l2:
                    for colIndex,col in enumerate(Cols):
                        if col=="R_WORDS":
                            tempRow.append(self.reportConfig["ROUND1"]["REACTION"][row])
                        elif col=="R_P_WORDS":
                            tempRow.append(self.reportConfig["ROUND2"]["REACTION"][row])
                        else:
                            tempRow.append(self.reportConfig["SCORES"][col][row])
                        if len(Pad[colIndex]) < len(str(tempRow[-1])):
                            Pad[colIndex] = self._doPadding(Pad[colIndex], len(str(tempRow[-1])), "_")
                    L.append(tempRow)
                    L.append(Pad)

            if self.ui.DEBUG_MODE:
                print("Build End3")
            Obj.setFontSize(50)
            L = self._sortRows(L)
            Obj.generateImage(L)

            # Height_ROUND1 = self.reportConfig["ROUND1"]["REACTION_TIME"]
            # Height_ROUND2 = self.reportConfig["ROUND2"]["REACTION_TIME"]
            # Domain_S_WORDS = self.reportConfig["SCORES"]["S_WORDS"]
            # Domain_RESPONSE = self.reportConfig["ROUND1"]["REACTION"]
            # Domain_REPRODUCTION = self.reportConfig["ROUND2"]["REACTION"]
            # Domain_X1 = []
            # Domain_X2 = []
            # Colors1 = ["green"]*len(Height_ROUND1)
            # Colors2 = ["green"]*len(Height_ROUND2)
            #
            # for i in range(len(Domain_S_WORDS)):
            #     Domain_X1.append(Domain_S_WORDS[i]+"\n"+Domain_RESPONSE[i])
            #     if Height_ROUND1[i] >= self.reportConfig["ROUND1"]["MEDIAN_PRT"]:
            #         Colors1[i] = "red"
            # for i in range(len(Domain_S_WORDS)):
            #     Domain_X2.append(Domain_S_WORDS[i]+"\nRP:"+Domain_REPRODUCTION[i])
            #     if Height_ROUND2[i] >= self.reportConfig["ROUND1"]["MEDIAN_PRT"]:
            #         Colors2[i] = "red"
            #
            # y = [self.reportConfig["ROUND1"]["MEDIAN_PRT"]]*len(Domain_S_WORDS)
            # fig, ax1 = plt.subplots()
            # ax1.bar(Domain_S_WORDS, Height_ROUND1, color=Colors1)
            # plt.xticks(rotation=90)
            # plt.yticks(rotation=90)
            # ax2 = ax1.twiny()
            # ax2.bar(Domain_RESPONSE, Height_ROUND1, color=Colors1)
            # plt.xticks(rotation=90)
            # plt.yticks(rotation=90)
            # ax1.plot(range(len(Domain_S_WORDS)),y)
            # ax2.plot(range(len(Domain_S_WORDS)),y)
            # ax1.set_ylabel("Time in Seconds")
            # plt.savefig(ABS_Path[:-4]+"Graph_Round1"+ABS_Path[-4:])
            #
            # #plt.clear()
            # if self.ui.DEBUG_MODE:
            #     print("Plot1 End")
            # fig, Ax1 = plt.subplots()
            # print(len(Domain_S_WORDS))
            # Ax1.bar(Domain_S_WORDS, Height_ROUND2, color=Colors2)
            # plt.xticks(rotation=90)
            # plt.yticks(rotation=90)
            # Ax2 = Ax1.twiny()
            # print(len(Domain_REPRODUCTION))
            # print(len(Height_ROUND2))
            # Ax2.bar(Domain_REPRODUCTION,Height_ROUND2, color=Colors2)
            # plt.xticks(rotation=90)
            # plt.yticks(rotation=90)
            # Ax1.plot(range(len(Domain_S_WORDS)),y)
            # Ax2.plot(range(len(Domain_S_WORDS)),y)
            # Ax1.set_ylabel("Time in Seconds")
            # plt.savefig(ABS_Path[:-4]+"Graph_Round2"+ABS_Path[-4:])
            # if self.ui.DEBUG_MODE:
            #     print("Plot2 End")

            self._showMessageDialog(" Exported Successfully","Exported to png successfully")
        else:
            self._showMessageDialog(" Export Halt", "Generate Report First")
        # except Exception as eExportPng:
        #     if self.ui.DEBUG_MODE:
        #         assert("unable to Export " + str(eExportPng))
        #     self._showMessageDialog(" Denied ", "Failed to Export"+str(eExportPng))
    
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
                ABS_PATH = self.refReportConfigFile
                if self.ui.DEBUG_MODE:
                    print("Loading ref report")
            else:
                ABS_PATH = self.tempReportConfigFile
                if self.ui.DEBUG_MODE:
                    print("Loading temp report")
            if self.ui.DEBUG_MODE:
                print("Loading D8: ",ABS_PATH)
            with open(ABS_PATH, "r") as fp:
                self.reportConfig = json.load(fp)
            return 1
        except Exception as eOpen:
            if self.ui.DEBUG_MODE:
                #sys.stderr.write(self.tempConfigFile+" No such config file or directory")
                #sys.stderr.write(str(eOpen))
                assert("No such file or directory " +str(eOpen))
            #sys.exit(8)
            return 0
        
    def loadInterviewConfiguration(self):
        try:
            
            ABS_PATH = self.interviewConfigFile
            if self.ui.DEBUG_MODE:
                print("Loading D5: ",ABS_PATH)
            with open(ABS_PATH,"r") as fp:
                self.config = json.load(fp)
                #self.wordsFile = self.config["INTERVIEW_WORDS_JSON_FILE"]
                #self.wordsFileLocation = self.config["INTERVIEW_WORDS_JSON_FILE_LOCATION"]
            return 1
        except Exception as eWordLoad:
            if self.ui.DEBUG_MODE:
                #sys.stderr.write("Unable to load ",self.wordsFile," file" )
                #sys.stderr.write(str(eWordLoad))
                assert("Unable to load wordsfile: "+str(eWordLoad))
            #sys.exit(5)
            return 0
    
    def Save_Generated_Report_Handler(self):
        if self.ui.DEBUG_MODE:
            print("Save Generated Report Handler callback....")
        if self._crossCheckInterview():#TODO
            self._saveInterviewReport()
            self._showMessageDialog("Succeed","Report Generated & Saved Successfully")
            Obj = menuView_Handler(self.ui)
            Obj.Last_Interview_Report_View_Handler()
        else:
            if self.ui.DEBUG_MODE:
                print("Unable to Generate Report & Save")
    
    def _saveInterviewReport(self):
        try:
            ABS_PATH = self.tempReportConfigFile
            if self.ui.DEBUG_MODE:
                print("Saving D8: ",ABS_PATH)
            with open(ABS_PATH, "w") as fp:
                json.dump(self.reportConfig,fp,indent=4)
            return 1
        except Exception as eSave:
            if self.ui.DEBUG_MODE:
                assert("Unablel to save generated report "+str(eSave))
            self._showMessageDialog("Save Failed","Error in saving Report")
            return 0
    
    def getGeneratedReport(self):
        self.loadInterviewReport()
        return self.reportConfig
    
    def _showMessageDialog(self,title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()
        if self.ui.DEBUG_MODE:
            print("value of pressed message box button:", retval)
