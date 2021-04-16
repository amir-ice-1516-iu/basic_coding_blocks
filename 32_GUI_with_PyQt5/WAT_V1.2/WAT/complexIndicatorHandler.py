#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 07:38:49 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: ComplexIndicatorHandler.py

@methods:
    loadComplexIndicatorConfiguration()
    resetComplexIndicatorInput()
    showComplexIndicatorInput()
    hideComplexIndicatorInput()
    _setEditMode()
    viewComplexIndicatorHandler()
    editComplexIndicatorHandler()
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import sys

import ComplexIndicator


class ComplexIndicatorHandler(object):
    
    def __init__(self, ui, configFile="config/complexIndicators.json"):
        
        self.ui = ui
        self.configFile = configFile
        self.inTestSession = True
        
        self.loadComplexIndicatorConfiguration()
        
        # self.generateComplexIndicatorForm()
    
    def generateComplexIndicatorForm(self):
        if self.inTestSession:
            self.ComplexIndicatorViewForm = QtWidgets.QWidget(self.ui.complexIndicatorsSelection)
            print("CI selection widget")
        else:
            self.ComplexIndicatorViewForm = QtWidgets.QWidget(self.ui.centralwidget)
        # ComplexIndicatorView = QtWidgets.QWidget()
        self.CI_FORM = ComplexIndicator.Ui_Form()
        self.CI_FORM.setupUi(self.ComplexIndicatorViewForm)
        
        self.ui.complexIndicatorsSelection = self.ComplexIndicatorViewForm #TRACE BUG HERE IF REQUIRED IN FUTURE
    
    def loadComplexIndicatorConfiguration(self):
        try:
            with open(self.configFile, "r") as fp:
                self.config = json.load(fp)
        except Exception as eOpen:
            sys.stderr.write(self.configFile+" No such config file or directory")
            sys.stderr.write(eOpen)
            sys.exit(2)
            
    def resetComplexIndicatorInput(self):
        self.CI_FORM.reactiionTimeCategoryLabel.setText(self.config["CATEGORY"]["1"]["NAME"])
        self.CI_FORM.meaningCategoryLabel.setText(self.config["CATEGORY"]["2"]["NAME"])
        self.CI_FORM.physicalReactionsCategoryLabel.setText(self.config["CATEGORY"]["3"]["NAME"])
        self.CI_FORM.speechCategoryLabel.setText(self.config["CATEGORY"]["4"]["NAME"])
        self.CI_FORM.patternsCategoryLabel.setText(self.config["CATEGORY"]["5"]["NAME"])
        
        #self.CI_FORM.category1Type1.setChecked(False)
        IDs = self.config["CATEGORY"].keys()
        for ID in IDs:
            KEYs = self.config["CATEGORY"][ID]["TYPES"]
            for KEY,ind in zip(KEYs,range(1,len(KEYs)+1)):
                eval("""self.CI_FORM.category"""+ID+"""Type"""+str(ind)+""".setText(self.config["CATEGORY"][ID]["TYPES"][KEY])""")
                eval("""self.CI_FORM.category"""+ID+"""Type"""+str(ind)+""".setChecked(False)""")
        self._setEditMode()
    
    def showComplexIndicatorInput(self):
        print("show comp input")
        self.ui.complexIndicatorsSelection.show()
    
    def hideComplexIndicatorInput(self):
        self.resetComplexIndicatorInput()
        self.ui.complexIndicatorsSelection.hide()
    
    def _setEditMode(self):
        self.CI_FORM.updateExistingComplexIndicator.setEnabled(not self.inTestSession)
        self.CI_FORM.complexIndicatorToUpdate.setEnabled(not self.inTestSession)
        self.CI_FORM.selectedTypeLabel.setEnabled(not self.inTestSession)
        self.CI_FORM.addNewComplexIndicator.setEnabled(not self.inTestSession)
        self.CI_FORM.newComplexIndicatorToAdd.setEnabled(not self.inTestSession)
        self.CI_FORM.selectedComplexIndicatorCategory.setEnabled(not self.inTestSession)
        self.CI_FORM.doneSetupButton.setEnabled(not self.inTestSession)
        
        self.CI_FORM.updateExistingComplexIndicator.setVisible(not self.inTestSession)
        self.CI_FORM.complexIndicatorToUpdate.setVisible(not self.inTestSession)
        self.CI_FORM.selectedTypeLabel.setVisible(not self.inTestSession)
        self.CI_FORM.addNewComplexIndicator.setVisible(not self.inTestSession)
        self.CI_FORM.newComplexIndicatorToAdd.setVisible(not self.inTestSession)
        self.CI_FORM.selectedComplexIndicatorCategory.setVisible(not self.inTestSession)
        self.CI_FORM.doneSetupButton.setVisible(not self.inTestSession)
        
    def viewComplexIndicatorHandler(self):
        self._setEditMode()
        self.ComplexIndicatorViewForm.show()
         
    def editComplexIndicatorHandler(self):
        self.inTestSession = False
        self._setEditMode()
        

if __name__=="__main__":
    pass
