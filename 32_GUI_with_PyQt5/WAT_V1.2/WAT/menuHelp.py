#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:39:17 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuHelp.py
"""
import os
class menuHelp_Handler(object): #TODO
    
    def __init__(self, ui, configFile="interview.json"):
        self.ui = ui
        self.configFile = ui.configFile
    
    def About_Help_Handler(self):
        if self.ui.DEBUG_MODE:
            print("About Help Handler")
