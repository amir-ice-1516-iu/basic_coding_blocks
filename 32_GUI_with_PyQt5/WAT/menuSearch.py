#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 06:07:18 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuSearch.py
"""

class menuSearch_Handler(object):
    
    def __init__(self, ui, configFile="interview.json"):
        self.ui = ui
        self.configFile = configFile
        self.configFilePath = "config"

    def Predefined_Words_Search_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Predefined Words Search Callback")
    
    def In_Last_Interview_Search_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Last Interview Search Callback")
    
    def In_Last_Report_Search_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Last Report Search Callback")