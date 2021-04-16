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
from PyQt5 import QtWidgets #,QtCore, QtGui
import copy

import GeneratedReport
import PredefinedWords
import menuDashboard

class menuEdit_Handler(object):
    
    def __init__(self, ui, configFile="interview.json"):
        self.ui = ui
        self.EDIT_MODE = True
        self.SEARCH_MODE = False
        self.tempConfigFile = configFile
        self.tempConfigFilePath = "temp_config"
        self.ReportGeneratorObj = None
        #self.loadInterviewConfiguration()
            
    def loadInterviewConfiguration(self):
        try:
            path = os.path.join(self.tempConfigFilePath,self.tempConfigFile)
            if self.ui.DEBUG_MODE:
                print("Loading E8: ",path)
            with open(path, "r") as fp:
                self.config = json.load(fp)
                self.wordsFile = self.config["INTERVIEW_WORDS_JSON_FILE"]
                self.wordsFileLocation = self.config["INTERVIEW_WORDS_JSON_FILE_LOCATION"]
            return 1
        except Exception as eOpen:
            sys.stderr.write(self.tempConfigFile+" No such config file or directory")
            sys.stderr.write(str(eOpen))
            #sys.exit(8)
            return 0
        
    def loadInterviewWords(self):
        try:
            ABS_PATH = os.path.join(self.wordsFileLocation,self.wordsFile)
            if self.ui.DEBUG_MODE:
                print("Loading ED5: ",ABS_PATH)
            with open(ABS_PATH,"r") as fp:
                self.interview_words = json.load(fp)
            return 1
        except Exception as eWordLoad:
            sys.stderr.write("Unable to load "+self.wordsFile+" file" )
            sys.stderr.write(str(eWordLoad))
            #sys.exit(5)
            return 0
            
    def saveInterviewWords(self):
        try:
            if self.ui.DEBUG_MODE:
                print("Saving Predefined Words to : ",self.wordsFile)
            ABS_PATH = os.path.join(self.wordsFileLocation,self.wordsFile)
            with open(ABS_PATH, "w") as fp:
                json.dump(self.interview_words, fp, indent=4)
            return 1
        except Exception as eWordSave:
            sys.stderr.write("Unable to save "+self.wordsFile+" file")
            sys.stderr.write(str(eWordSave))
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

    def Current_Interview_Result_Edit_Handler(self):
        if self.ui.DEBUG_MODE:
            print("Current Interview Result Edit Callback")
        try:
            self.ui.lastActiveWidget.close()
        except Exception as eClear:
            if self.ui.DEBUG_MODE:
                print("Unable to clear window central widget")
            sys.stderr.write(str(eClear))
            sys.exit(11)
        
        self.ReportGeneratorObj = menuDashboard.menuDashboard_Handler(self.ui)
        if self.ReportGeneratorObj.reportConfig["IS_READY_TO_GENERATE_GRAPH"]:
            pass
        else:
            return 0
        self.GRFormWidget = QtWidgets.QWidget(self.ui.centralwidget)     
        self.GR_FORM = GeneratedReport.Ui_Form()
        self.GR_FORM.setupUi(self.GRFormWidget)
        self.ui.mainCanvas = self.GRFormWidget
        self.ui.lastActiveWidget = self.GRFormWidget
        
        self._setReportValues()
        
        if self.EDIT_MODE:
            self.GR_FORM.updateReport.clicked.connect(self.onUpdateReportClicked)
        else:
            self.GR_FORM.updateReport.setText("End View")
            self.GR_FORM.updateReport.clicked.connect(lambda x: self.GRFormWidget.close())
        self.GR_FORM.editGeneratedReport.setVisible(self.EDIT_MODE)
        
        self.GRFormWidget.show()
        self.GR_FORM.editGeneratedReport.click()
        self.GR_FORM.editGeneratedReport.setEnabled(self.EDIT_MODE)
    
    def Predefined_Words_Edit_Handler(self):
        if self.ui.DEBUG_MODE:
            print("Predefined Words Edit Callback")
        if self.loadInterviewConfiguration():
            try:
                self.ui.lastActiveWidget.close()
            except Exception as eClear:
                if self.ui.DEBUG_MODE:
                    print("Unable to clear window central widget")
                sys.stderr.write(str(eClear))
                sys.exit(13)
            self.wordsFile = self.config["INTERVIEW_WORDS_JSON_FILE"]
            self.PWFormWidget = QtWidgets.QWidget(self.ui.centralwidget)
            #ComplexIndicatorView = QtWidgets.QWidget()         
            self.PWS_FORM = PredefinedWords.Ui_Form()
            self.PWS_FORM.setupUi(self.PWFormWidget)
            self.ui.mainCanvas = self.PWFormWidget
            self.ui.lastActiveWidget = self.PWFormWidget
            self._setPredefinedWords()
            
            if self.SEARCH_MODE:
                self.PWS_FORM.searchPredefinedWord.clicked.connect(self._searchOnPredefinedWords)
            else:
                self.PWS_FORM.addWord.clicked.connect(self._setAddWordTexts)
                self.PWS_FORM.removeWord.clicked.connect(self._setRemoveWordTexts)
                self.PWS_FORM.wordToUpdate.clicked.connect(self._handleOperationOnPredefinedWords)
                self.PWS_FORM.addWord.click()
                self.PWS_FORM.addWord.click()
            
            self.PWS_FORM.updatedWordToCommit.setVisible(False)
            
            self.PWS_FORM.searchPredefinedWord.setEnabled(self.SEARCH_MODE)
            self.PWS_FORM.searchPredefinedWord.setVisible(self.SEARCH_MODE)
            self.PWS_FORM.wordToSearch.setEnabled(self.SEARCH_MODE)
            self.PWS_FORM.wordToSearch.setVisible(self.SEARCH_MODE)
            
            self.PWS_FORM.addWord.setEnabled(not self.SEARCH_MODE)
            self.PWS_FORM.addWord.setVisible(not self.SEARCH_MODE)
            self.PWS_FORM.removeWord.setEnabled(not self.SEARCH_MODE)
            self.PWS_FORM.removeWord.setVisible(not self.SEARCH_MODE)
            self.PWS_FORM.wordToUpdate.setEnabled(not self.SEARCH_MODE)
            self.PWS_FORM.wordToUpdate.setVisible(not self.SEARCH_MODE)
            
            self.PWFormWidget.show()
            
        
    def Complex_Indicators_Edit_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Complex Indicators Edit Callback")
            
    def Current_Interview_Details_Edit_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Current Interview Details Edit Callback")
    
    def _setAddWordTexts(self):
        if self.PWS_FORM.addWord.isChecked():
            self.PWS_FORM.wordToUpdate.setText("Add Word")
            self.PWS_FORM.removeWord.setChecked(False)
            self.PWS_FORM.updatedWordToCommit.setVisible(True)
        if not(self.PWS_FORM.addWord.isChecked() or self.PWS_FORM.removeWord.isChecked()):
            self.PWS_FORM.wordToUpdate.setText("Update Word")
            self.PWS_FORM.updatedWordToCommit.setVisible(False)
            
    def _setRemoveWordTexts(self):
        if self.PWS_FORM.removeWord.isChecked():
            self.PWS_FORM.wordToUpdate.setText("Remove Word")
            self.PWS_FORM.addWord.setChecked(False)
            self.PWS_FORM.updatedWordToCommit.setVisible(True)
        if not(self.PWS_FORM.addWord.isChecked() or self.PWS_FORM.removeWord.isChecked()):
            self.PWS_FORM.wordToUpdate.setText("Update Word")
            self.PWS_FORM.updatedWordToCommit.setVisible(False)
    
    def _handleOperationOnPredefinedWords(self):
        if self.PWS_FORM.addWord.isChecked() and self.PWS_FORM.removeWord.isChecked():
            pass #cross check . although both cannot be checked at the same time
        elif self.PWS_FORM.addWord.isChecked() or self.PWS_FORM.removeWord.isChecked():
            if self.PWS_FORM.addWord.isChecked():
                self._addNewWord()
            if self.PWS_FORM.removeWord.isChecked():
                self._removeWord()
        else:
            self._updateExistingWord()
    
    def _updateExistingWord(self):
        self._getPredefinedWords()
        self.saveInterviewWords()
        self.Predefined_Words_Edit_Handler()
        
    
    def _addNewWord(self):
        self._rearrangeInterviewWords()
        addingNewWordSucceed = False
        if self.PWS_FORM.addWord.isChecked():
            Keys = list(self.interview_words.keys())
            if self.PWS_FORM.updatedWordToCommit.text():
                if not self._searchWord(self.PWS_FORM.updatedWordToCommit.text()):
                    for key in Keys:
                        if self.interview_words[key]=="":
                            self.interview_words[key] = copy.copy(self.PWS_FORM.updatedWordToCommit.text())
                            
                            self.PWS_FORM.updatedWordToCommit.setText("")
                            addingNewWordSucceed = True
                            self._showSetupSuccessDialog(" Operation Succeed", "WORD :"+self.interview_words[key]+" ADDED")
                            self._rearrangeInterviewWords()
                            self.saveInterviewWords()
                            self.Predefined_Words_Edit_Handler()
                            return 1
                            #break
                else:
                    self._showSetupSuccessDialog("Operation Denied", "Word Already Exists")
                    return 0
        if not addingNewWordSucceed:
            self._showSetupSuccessDialog("Operation Failed", "Limit 200 Word Filled")
            return 0
    
    def _rearrangeInterviewWords(self):#TODO
        temp_interview_words = dict()
        sl = 0
        Keys = list(self.interview_words.keys())
        for key in Keys:
            if self.interview_words[key]!="":
                temp_interview_words[str(sl)] = self.interview_words[key]
                sl += 1
        while(sl<200):
            temp_interview_words[str(sl)] = ""
            sl += 1
        self.interview_words = copy.deepcopy(temp_interview_words)
        
    def _removeWord(self):
        if self.PWS_FORM.removeWord.isChecked():
            Keys = list(self.interview_words.keys())
            if self.PWS_FORM.updatedWordToCommit.text():
                if self._searchWord(self.PWS_FORM.updatedWordToCommit.text()):
                    for key in Keys:
                        if self.interview_words[key]==self.PWS_FORM.updatedWordToCommit.text():
                            self.interview_words[key] = ""
                            self._rearrangeInterviewWords()
                            self.saveInterviewWords()
                            self._showSetupSuccessDialog(" Operation Succeed", "WORD: "+self.PWS_FORM.updatedWordToCommit.text()+" REMOVED")
                            self.PWS_FORM.updatedWordToCommit.setText("")
                            self.Predefined_Words_Edit_Handler()
                            break
                else:
                    self._showSetupSuccessDialog(" Operation Denied", "WORD: "+self.PWS_FORM.updatedWordToCommit.text()+" Not Present")

    
    def _searchWord(self, word):
        Values = list(self.interview_words.values())
        return word in Values
    
    def _searchRowCol(self, word):
        for row in range(50):
            for col in range(4):
                if self.PWS_FORM.wordsTable.item(row,col):
                    if self.PWS_FORM.wordsTable.item(row,col).text()==word:
                        return (row, col)
        return None,None
    
    def _searchOnPredefinedWords(self):
        if self.PWS_FORM.wordToSearch.text()!="":
            if self._searchWord(self.PWS_FORM.wordToSearch.text()):
                row, col = self._searchRowCol(self.PWS_FORM.wordToSearch.text())
                if row or col:
                    self.PWS_FORM.wordsTable.selectRow(row)
                    #self._showSetupSuccessDialog(" Search Found ", "WORD"+self.PWS_FORM.wordToSearch.text()+" FOUND")
                else:
                    self._showSetupSuccessDialog(" Search Not Found ", "WORD"+self.PWS_FORM.wordToSearch.text()+"Not FOUND")
            else:
                if self.ui.DEBUG_MODE:
                    print("Word Not Found")
                self._showSetupSuccessDialog(" Search Not Found ", "WORD"+self.PWS_FORM.wordToSearch.text()+"Not FOUND")
        else:
            if self.ui.DEBUG_MODE:
                print("Empty Word Searching")
                
    def _setPredefinedWords(self):
        #self.loadInterviewWords()
        if self.loadInterviewWords():
            pass
        else:
            if self.ui.DEBUG_MODE:
                print("Unable to load interview words")
                return
        WordSerialNumber = list(self.interview_words.keys())
        ShouldBreak = False
        sl = 0
        TotalWords = len(WordSerialNumber)
        for row in range(50):
            for col in range(4):
                self.PWS_FORM.wordsTable.setItem(row, col, QtWidgets.QTableWidgetItem(str(self.interview_words[WordSerialNumber[sl]])))
                sl +=1
                if sl>=TotalWords:
                    ShouldBreak = True
                    break
            if ShouldBreak:
                break
                    
    
    def _getPredefinedWords(self):
        sl = 0
        for row in range(50):
            for col in range(4):
                if self.PWS_FORM.wordsTable.item(row, col):
                    self.interview_words[str(sl)] = self.PWS_FORM.wordsTable.item(row, col).text()
                else:
                    self.interview_words[str(sl)] = ""
                sl += 1
    
    def _setReportValues(self): #TODO
        self.loadInterviewConfiguration()
        MAX_ROWS_TO_SHOW = 0
        if self.ui.DEBUG_MODE:
            print("Setting parameters")
        if self.ReportGeneratorObj:
            MAX_ROWS_TO_SHOW = int(self.ReportGeneratorObj.reportConfig["NUMBER_OF_WORDS_IN_TEST"])
            Column = []
            temp_fileds = self.ReportGeneratorObj.reportConfig["SCORES"].keys()
            for temp_field in temp_fileds:
                if temp_field != "SL":
                    Column.append(self.ReportGeneratorObj.reportConfig["SCORES"][temp_field])
            MAX_COLS_TO_SHOW = len(Column)
            if self.ui.DEBUG_MODE:
                print("ROWS, COLUMNS: ",MAX_ROWS_TO_SHOW,MAX_COLS_TO_SHOW)
            for row in range(MAX_ROWS_TO_SHOW):
                for col in range(MAX_COLS_TO_SHOW):
                    self.GR_FORM.generatedReport.setItem(row,col, QtWidgets.QTableWidgetItem(str(Column[col][row])))
        else:
            self._showSetupSuccessDialog("Error", "Report not Generated Yet")
    
    def _getReportValues(self):
        if self.ui.DEBUG_MODE:
            print("Getting parameters")
        if self.ReportGeneratorObj:
            MAX_ROWS_TO_GET = int(self.ReportGeneratorObj.reportConfig["NUMBER_OF_WORDS_IN_TEST"])
            for row in range(MAX_ROWS_TO_GET):
                GR = self.GR_FORM.generatedReport
                self.ReportGeneratorObj.reportConfig["SCORES"]["S_WORDS"][row]= GR.item(row,0).text()
                try:
                    self.config["ROUND1_RESPONSES"][self.GR_FORM.generatedReport.item(row,0).text()]["RESPONSE_WORD"] = self.GR_FORM.generatedReport.item(row,3).text()
                    self.config["ROUND2_RESPONSES"][self.GR_FORM.generatedReport.item(row,0).text()]["RESPONSE_WORD"] = self.GR_FORM.generatedReport.item(row,4).text()
                except Exception as eEdit:
                    assert("Unable to update edited to temp_config/interview.json"+str(eEdit))
                temp_fileds = self.ReportGeneratorObj.reportConfig["SCORES"].keys()
                col= 0
                for temp_field in temp_fileds:
                    if temp_field != "SL":
                        self.ReportGeneratorObj.reportConfig["SCORES"][temp_field][row] = GR.item(row,col).text()
                        col += 1

                temp_Counter = 0
                for i, key in enumerate(self.ReportGeneratorObj.reportConfig["SCORES"].keys()):
                    if i >= 6 and i <= 15:
                        POINT_EARNED = "1"
                        if self.ReportGeneratorObj.reportConfig["SCORES"][key][row] != " ":
                            if i == 13:
                                temp_Counter += 2
                            else:
                                temp_Counter += 1
                self.ReportGeneratorObj.reportConfig["SCORES"]["TOTAL"][row] = str(temp_Counter)
                self.ReportGeneratorObj.reportConfig["ROUND1"]["REACTION"][row] = GR.item(row, 3).text()
                self.ReportGeneratorObj.reportConfig["ROUND2"]["REACTION"][row] = GR.item(row, 4).text()
        else:
            self._showSetupSuccessDialog("Error", "Report not Generated Yet!!!")
                        
    def onUpdateReportClicked(self):
        """ do hunky punky"""
        self._getReportValues()
        self.saveUpdatedReport()
        if self.ReportGeneratorObj:
            self.ReportGeneratorObj._saveInterviewReport()
        self._showSetupSuccessDialog("Updated Report", "Report Updated Successfully")
        self.GRFormWidget.close()
    
    def _showSetupSuccessDialog(self,title, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        retval = msg.exec_()
        if self.ui.DEBUG_MODE:
            print("value of pressed message box button:", retval)