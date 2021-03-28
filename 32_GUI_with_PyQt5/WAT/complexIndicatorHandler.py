#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 07:38:49 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: ComplexIndicatorHandler.py
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import ComplexIndicator as CI


class ComplexIndicatorHandler(object):
    
    def __init__(self, ui, configFile="config/complexIndicators.json"):
        self.ui = ui
        self.configFile = configFile
    
    def viewComplexIndiciatorHandler(self, canvas):
         ComplexIndicatorView = QtWidgets.QWidget(canvas)
         ui = CI.Ui_Form()
         ui.setupUi(ComplexIndicatorView)
         ui.updateExistingComplexIndicator.setVisible(False)
         ui.complexIndicatorToUpdate.setVisible(False)
         ui.selectedTypeLabel.setVisible(False)
         ui.addNewComplexIndicator.setVisible(False)
         ui.newComplexIndicatorToAdd.setVisible(False)
         ui.selectedComplexIndicatorCategory.setVisible(False)
         ComplexIndicatorView.show()
    
    def editComplexIndicatorHandler(self, canvas):
        pass

if __name__=="__main__":
    pass
