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
from PyQt5 import QtWidgets
import os
from swinlnk.swinlnk import SWinLnk
import WordAssociationTest
import menuInterview
import menuSetup
import menuEdit
import menuView
import menuDashboard
import menuSearch
import menuHelp

import shutil
import errno

def CopyFiles(src, dest):
    # Copy the content of
    # source to destination
    try:
        shutil.copytree(src, dest)
    except OSError as err:

        # error caused if the source was not a directory
        if err.errno == errno.ENOTDIR:
            shutil.copy2(src, dest)
        else:
            print("Error: % s" % err)

if __name__=='__main__':
    LinkPath = "C:/Users/"+os.getlogin()+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs"
    LinkFile = "WAT.lnk"
    LinkPathDesktop = "C:/Users/"+os.getlogin()+"/Desktop"
    ABS_Path = os.path.join(LinkPath, LinkFile)
    ABS_Path_Desktop = os.path.join(LinkPathDesktop, LinkFile)
    FilePath = "C:/Users/" + os.getlogin() + "/WAT"
    CopyFilesTo = "C:/Users/" + os.getlogin()
    FolderPath, FileName = os.path.split(os.path.realpath(__file__))
    print(FolderPath)
    CopyFiles(FolderPath,FilePath)
    print(FilePath)
    if os.path.exists(ABS_Path) and os.path.exists(ABS_Path_Desktop):
        pass
    else:
        swl = SWinLnk()
        ExecutionFileName ="WAT.exe" # "".join(tempFileName[:-1])+".exe"
        ExecutionFileABSPath = os.path.join(FilePath, ExecutionFileName)
        # ABS_Path = ABS_Path.replace("/","\\")
        # ExecutionFileABSPath = ExecutionFileABSPath.replace("/","\\")
        # ABS_Path_Desktop = ABS_Path_Desktop.replace("/","\\")
        print(ExecutionFileABSPath)
        print(ABS_Path_Desktop)
        print(ABS_Path)
        swl.create_lnk(ExecutionFileABSPath, ABS_Path)
        swl.create_lnk(ExecutionFileABSPath, ABS_Path_Desktop)

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = WordAssociationTest.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.MainWindow = MainWindow
    ui.configFile = os.path.join(os.path.join(FilePath,"config"),"interview.json")
    # ui.configFile = ui.configFile.replace("/","\\")
    ui.tempConfigFile = os.path.join(os.path.join(FilePath,"temp_config"),"interview.json")
    # ui.tempConfigFile = ui.tempConfigFile.replace("/","\\")

    ui.reportConfigFile = os.path.join(os.path.join(FilePath,"config"),"generatedReport.json")
    # ui.reportConfigFile = ui.reportConfigFile.replace("/","\\")
    ui.tempReportConfigFile = os.path.join(os.path.join(FilePath, "temp_config"), "generatedReport.json")
    # ui.tempReportConfigFile = ui.tempReportConfigFile.replace("/","\\")

    ui.complexIndicatorsConfigFile = os.path.join(os.path.join(FilePath,"config"),"complexIndicators.json")
    # ui.complexIndicatorsConfigFile = ui.complexIndicatorsConfigFile.replace("/","\\")
    ui.wordsListFile = os.path.join(os.path.join(FilePath,"config"),"wordsList.json")
    # ui.wordsListFile = ui.wordsListFile.replace("/","\\")
    ui.fontFilesPath = os.path.join(FilePath, "fonts")
    # ui.fontFiles = ui.fontFiles.replace("/","\\")
    ui.DEBUG_MODE = True
    ui.lastActiveWidget = None
    
    menu_interview_handler = menuInterview.menuInterview_Handler(ui)
    menu_interview_handler.ui.actionNew_Interview.triggered.connect(menu_interview_handler.FreshNewInterview)
    menu_interview_handler.ui.actionOpen_Interview_File.triggered.connect(menu_interview_handler.Open_Interview_File_Handler)
    menu_interview_handler.ui.actionOpen_Generated_Report.triggered.connect(menu_interview_handler.Open_Generated_Report_Handler)
    menu_interview_handler.ui.actionResume_Interview.triggered.connect(menu_interview_handler.Resume_Interview_Handler)
    menu_interview_handler.ui.actionSave_Current_Interview_File.triggered.connect(menu_interview_handler.Save_Current_Interview_File_Handler)
    menu_interview_handler.ui.actionSave_Generated_Report.triggered.connect(menu_interview_handler.Save_Generated_Report_Handler)
    menu_interview_handler.ui.actionExport_Generated_Report_To_PDF.triggered.connect(menu_interview_handler.Export_Generated_Report_To_PDF_Handler)
    menu_interview_handler.ui.actionExit.triggered.connect(menu_interview_handler.Exit_Handler)
    if ui.DEBUG_MODE:
        print("Menu Interview Success")    
    menu_setup_handler = menuSetup.menuSetup_Handler(ui)
    menu_setup_handler.ui.actionInterview_Account_Setup.triggered.connect(menu_setup_handler.Interview_Account_Setup_Handler)
    menu_setup_handler.ui.actionComplex_Indicators_Setup.triggered.connect(menu_setup_handler.Complex_Indicators_Setup_Handler) #TOEDIT
    menu_setup_handler.ui.actionPredefined_Words_Setup.triggered.connect(menu_setup_handler.Predefined_Words_Setup_Handler)   #TOEDIT
    if ui.DEBUG_MODE:
        print("Menu Setup Success")
    menu_edit_handler = menuEdit.menuEdit_Handler(ui)
    menu_edit_handler.ui.actionCurrent_Interview_Result_Edit.triggered.connect(menu_edit_handler.Current_Interview_Result_Edit_Handler)
    menu_edit_handler.ui.actionComplex_Indicators_Edit.triggered.connect(menu_edit_handler.Complex_Indicators_Edit_Handler)
    menu_edit_handler.ui.actionPredefined_Words_Edit.triggered.connect(menu_edit_handler.Predefined_Words_Edit_Handler)
    menu_edit_handler.ui.actionCurrent_Interview_Details_Edit.triggered.connect(menu_edit_handler.Current_Interview_Details_Edit_Handler)
    if ui.DEBUG_MODE:
        print("Menu Edit Success")
    menu_view_handler = menuView.menuView_Handler(ui)
    menu_view_handler.ui.actionLast_Interview_Report_View.triggered.connect(menu_view_handler.Last_Interview_Report_View_Handler)
    menu_view_handler.ui.actionGraphical_Visualization_View.triggered.connect(menu_view_handler.Graphical_Visualization_View_Handler)
    if ui.DEBUG_MODE:
        print("Menu View Success")
    menu_dashboard_handler = menuDashboard.menuDashboard_Handler(ui)
    menu_dashboard_handler.ui.actionGenerate_Report.triggered.connect(menu_dashboard_handler.Generate_Report_Handler)
    menu_dashboard_handler.ui.actionExport_Report_To_Png.triggered.connect(menu_dashboard_handler.Export_Report_To_Png_Handler)
    if ui.DEBUG_MODE:
        print("Menu Dashboard Success")
    menu_search_handler = menuSearch.menuSearch_Handler(ui)
    menu_search_handler.ui.actionPredefined_Words_Search.triggered.connect(menu_search_handler.Predefined_Words_Search_Handler)
    menu_search_handler.ui.actionIn_Last_Interview_Search.triggered.connect(menu_search_handler.In_Last_Interview_Search_Handler)
    menu_search_handler.ui.actionIn_Last_Report_Search.triggered.connect(menu_search_handler.In_Last_Report_Search_Handler)
    if ui.DEBUG_MODE:
        print("Menu Search Success")
    menu_help_handler = menuHelp.menuHelp_Handler(ui)
    menu_help_handler.ui.actionAbout_Help.triggered.connect(menu_help_handler.About_Help_Handler)
    if ui.DEBUG_MODE:
        print("Menu Help Success")        
    MainWindow.show()
    ErrorNo= app.exec_()
    try:
        src = os.path.join(os.path.join(FilePath,"config"),"generatedReport.json")
        dst = os.path.join(os.path.join(FilePath,"temp_config"),"generatedReport.json")
        from shutil import copyfile
        copyfile(src, dst)
    except Exception as eRemove:
        sys.stderr.write("Unable to copy ref generatedReport file")
        sys.stderr(str(eRemove))
        sys.exit(0)
    sys.exit(ErrorNo)
    


