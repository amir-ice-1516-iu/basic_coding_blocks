#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 06:06:31 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuDashboard.py
"""

class menuDashboard_Handler(object): #TODO
    
    def __init__(self, ui, configFile="interview.json"):#TODO
        self.ui = ui
        self.configFile = configFile
        self.configFilePath = "config"
        
    def Generate_Report_Handler(ui): #TODO
        print("Generate Report Callback")
