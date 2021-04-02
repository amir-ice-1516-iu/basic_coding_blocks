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

import GeneratedReport

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
        self.tempConfigFile = configFile # use self.ui.configFile
        self.tempConfigFile = "temp_config"
    
    def Last_Interview_Report_View_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Last Interview Report View Callback")
    
    def Graphical_Visualization_View_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Graphical Visualization View Callback")
    
