#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 06:07:18 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuSearch.py
"""

import menuEdit

class menuSearch_Handler(object):
    
    def __init__(self, ui, configFile="interview.json"):
        self.ui = ui
        self.configFile = configFile
        self.configFilePath = "config"
        self.PredefinedWordSearch = menuEdit.menuEdit_Handler(ui, configFile)

    def Predefined_Words_Search_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Predefined Words Search Callback")
        self.PredefinedWordSearch.SEARCH_MODE = True
        self.PredefinedWordSearch.Predefined_Words_Edit_Handler()
    
    def In_Last_Interview_Search_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Last Interview Search Callback")
    
    def In_Last_Report_Search_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Last Report Search Callback")