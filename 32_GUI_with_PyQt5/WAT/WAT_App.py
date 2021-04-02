#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 02:31:48 2021

@author: Khondokar Amir Hossain
@contact: amirkhondokar@gmail.com
@file:   WAT_App.py
@purpose: main script that stacks all GUI and Logic modules together
@details: This application to do Phsychological Word Pssociation Test and generate report of the test
"""

import sys
import os
import src_rc
from PyQt5 import QtCore, QtGui, QtWidgets
import WordAssociationTest
#import NewInterview
import time
import menuInterview
import menuSetup
import menuEdit
import menuView
import menuDashboard
import menuSearch
import menuHelp

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = WordAssociationTest.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.MainWindow = MainWindow
    configFile = "interview.json"
    #ui.configFilePath = "config"
    #ui.tempConfigFile = "interview.json"
    #ui.tempConfigFilePath = "temp_config"
    #ui.reportFile = "Report.png"
    #ui.reportFilePath = "Reports"
    ui.DEBUG_MODE = True
    ui.lastActiveWidget = None
    
    menu_interview_handler = menuInterview.menuInterview_Handler(ui, configFile)
    menu_interview_handler.ui.actionNew_Interview.triggered.connect(menu_interview_handler.FreshNewInterview)
    menu_interview_handler.ui.actionOpen_Interview_File.triggered.connect(menu_interview_handler.Open_Interview_File_Handler)
    menu_interview_handler.ui.actionSave_Current_Interview_File.triggered.connect(menu_interview_handler.Save_Current_Interview_File_Handler)
    menu_interview_handler.ui.actionExit.triggered.connect(menu_interview_handler.Exit_Handler)
    
    menu_setup_handler = menuSetup.menuSetup_Handler(ui, configFile)
    menu_setup_handler.ui.actionInterview_Account_Setup.triggered.connect(menu_setup_handler.Interview_Account_Setup_Handler)
    menu_setup_handler.ui.actionComplex_Indicators_Setup.triggered.connect(menu_setup_handler.Complex_Indicators_Setup_Handler) #TOEDIT
    menu_setup_handler.ui.actionPredefined_Words_Setup.triggered.connect(menu_setup_handler.Predefined_Words_Setup_Handler)   #TOEDIT
    
    menu_edit_handler = menuEdit.menuEdit_Handler(ui, configFile)
    menu_edit_handler.ui.actionCurrent_Interview_Result_Edit.triggered.connect(menu_edit_handler.Current_Interview_Result_Edit_Handler)
    menu_edit_handler.ui.actionComplex_Indicators_Edit.triggered.connect(menu_edit_handler.Complex_Indicators_Edit_Handler)
    menu_edit_handler.ui.actionPredefined_Words_Edit.triggered.connect(menu_edit_handler.Predefined_Words_Edit_Handler)
    menu_edit_handler.ui.actionCurrent_Interview_Details_Edit.triggered.connect(menu_edit_handler.Current_Interview_Details_Edit_Handler)
    
    menu_view_handler = menuView.menuView_Handler(ui, configFile)
    menu_view_handler.ui.actionLast_Interview_Report_View.triggered.connect(menu_view_handler.Last_Interview_Report_View_Handler)
    menu_view_handler.ui.actionGraphical_Visualization_View.triggered.connect(menu_view_handler.Graphical_Visualization_View_Handler)
    
    menu_dashboard_handler = menuDashboard.menuDashboard_Handler(ui, configFile)
    menu_dashboard_handler.ui.actionGenerate_Report.triggered.connect(menu_dashboard_handler.Generate_Report_Handler)
    
    menu_search_handler = menuSearch.menuSearch_Handler(ui, configFile)
    menu_search_handler.ui.actionPredefined_Words_Search.triggered.connect(menu_search_handler.Predefined_Words_Search_Handler)
    menu_search_handler.ui.actionIn_Last_Interview_Search.triggered.connect(menu_search_handler.In_Last_Interview_Search_Handler)
    menu_search_handler.ui.actionIn_Last_Report_Search.triggered.connect(menu_search_handler.In_Last_Report_Search_Handler)
    
    menu_help_handler = menuHelp.menuHelp_Handler(ui, configFile)
    menu_help_handler.ui.actionAbout_Help.triggered.connect(menu_help_handler.About_Help_Handler)
            
    MainWindow.show()
    ErrorNo= app.exec_()
    try:
        src = "config/interview.json"
        dst = "temp_config/interview.json"
        from shutil import copyfile
        copyfile(src, dst)
    except Exception as eRemove:
        sys.stderr.write("Unable to remove file")
        sys.stderr(str(eRemove))
        sys.exit(0)
    sys.exit(ErrorNo)
    


