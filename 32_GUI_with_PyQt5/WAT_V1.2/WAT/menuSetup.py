#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 06:02:40 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file: menuSetup.py
"""
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, json
import time
from threading import Thread
import os

import menuInterview
import complexIndicatorHandler

class menuSetup_Handler(object):
    
    def __init__(self, ui, configFile="interview.json"):
        self.ui = ui
        self.configFile = configFile
        self.configFilePath = "config"
        #self.loadInterviewConfiguration()
        self.menu_interview_handler = menuInterview.menuInterview_Handler(ui, configFile)
        self.menu_interview_handler.INTERVIEW_SETUP_MODE = True
        #self.Interview_Account_Setup_Handler = self.menu_interview_handler.FreshNewInterview
        
        
        self.newCIForm = False
        self.newInterviewFormShowed = False
        self.newInterviewCanceled = False
        self.alive = True
        
        self.CI_FORM = complexIndicatorHandler.ComplexIndicatorHandler(self.ui)
        self.CI_FORM.inTestSession = False
        #self.CI_FORM.generateComplexIndicatorForm()
    
    def Interview_Account_Setup_Handler(self):
        if self.ui.DEBUG_MODE:
            print("Interview Account Setup Dummy Callback over written by FreshNewIntervieww in side menuInterview.py")
        self.menu_interview_handler.FreshNewInterview()
    
    def Complex_Indicators_Setup_Handler(self): #TODO
        if self.ui.DEBUG_MODE:
            print("Complex Indicators Setup Callback")
    
    def Predefined_Words_Setup_Handler(self):#TODO
        if self.ui.DEBUG_MODE:
            print("Predefined Words Setup Callback")