#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 06:05:21 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuView.py
"""
import json
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

import menuEdit
import os

class menuView_Handler(object):
    
    def __init__(self, ui, configFile="interview.json"):
        """
        ui.configFile = "interview.json"
        ui.configFilePath = "config"
        ui.tempConfigFile = "interview.json"
        ui.tempConfigFilePath = "temp_config"
        ui.reportFile = "Report.png"
        ui.reportFilePath = "Reports"
        """
        self.ui = ui
        self.tempConfigFile = os.path.split(ui.tempConfigFile)[1] # use self.ui.configFile
        self.tempConfigFile =  os.path.split(ui.tempConfigFile)[0]
        self.ReportViewer = menuEdit.menuEdit_Handler(ui, configFile)
    
    def Last_Interview_Report_View_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Last Interview Report View Callback")
        self.ReportViewer.EDIT_MODE = False
        self.ReportViewer.Current_Interview_Result_Edit_Handler()
    
    def Graphical_Visualization_View_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Graphical Visualization View Callback")
    
