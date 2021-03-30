#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 06:03:56 2021

@author: rango
"""
import json

class menuEdit_Handler(object):
    def __init__(self,ui,configFileLocation="config/"):
        pass
    
    def loadConfiguration(self,configFile,Obj):
        with open(configFile,"r") as fp:
            Obj = json.load(fp)
            
    def Current_Interview_Result_Edit_Handler(ui):#TODO
        print("Current Interview Result Edit Callback")

    def Complex_Indicators_Edit_Handler(ui): #TODO
        print("Complex Indicators Edit Callback")
    
    def Predefined_Words_Edit_Handler(ui): #TODO
        print("Predefined Words Edit Callback")
    
    def Current_Interview_Details_Edit_Handler(ui): #TODO
        print("Current Interview Details Edit Callback")