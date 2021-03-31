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
import src_rc
from PyQt5 import QtCore, QtGui, QtWidgets
import WordAssociationTest
#import NewInterview
import time
import menuInterview
import menuEdit

def onCancel(OBJ):
    OBJ.close()

def NewInterviewSetup(GUI):
    NewInterviewForm = QtWidgets.QWidget(GUI.centralwidget)
    
    NI = NewInterview.Ui_Form()
    NI.setupUi(NewInterviewForm)
    GUI.mainCanvas = NewInterviewForm
    print("NewInterview")
    NI.cancelInput.clicked.connect(lambda y: onCancel(NewInterviewForm))
    GUI.mainCanvas.show()
    NI.enableEdit.setChecked(True)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = WordAssociationTest.Ui_MainWindow()
ui.setupUi(MainWindow)
ui.MainWindow = MainWindow

menu_interview_handler = menuInterview.menuInterview_Handler(ui,"interview.json")
menu_edit_handler = menuEdit.menuEdit_Handler(ui,"")
    
MainWindow.show()
sys.exit(app.exec_())



