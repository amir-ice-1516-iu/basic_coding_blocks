# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Files\WordAssociationTest.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1035, 550)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1035, 550))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/WAT_Dummy_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("bg-color: /icons/icons/BackGround.jpg")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainCanvas = QtWidgets.QWidget(self.centralwidget)
        self.mainCanvas.setGeometry(QtCore.QRect(0, 14, 1024, 500))
        self.mainCanvas.setStyleSheet("")
        self.mainCanvas.setObjectName("mainCanvas")
        self.welcomeMessage_Panel = QtWidgets.QLabel(self.mainCanvas)
        self.welcomeMessage_Panel.setGeometry(QtCore.QRect(0, 0, 1024, 500))
        self.welcomeMessage_Panel.setMinimumSize(QtCore.QSize(1024, 500))
        self.welcomeMessage_Panel.setMaximumSize(QtCore.QSize(1024, 600))
        self.welcomeMessage_Panel.setText("")
        self.welcomeMessage_Panel.setObjectName("welcomeMessage_Panel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1035, 21))
        self.menubar.setObjectName("menubar")
        self.menuInterview = QtWidgets.QMenu(self.menubar)
        self.menuInterview.setObjectName("menuInterview")
        self.menuSetup = QtWidgets.QMenu(self.menubar)
        self.menuSetup.setObjectName("menuSetup")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuDashboard = QtWidgets.QMenu(self.menubar)
        self.menuDashboard.setObjectName("menuDashboard")
        self.menuSearch = QtWidgets.QMenu(self.menubar)
        self.menuSearch.setObjectName("menuSearch")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Interview = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/New_Interview_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionNew_Interview.setIcon(icon1)
        self.actionNew_Interview.setObjectName("actionNew_Interview")
        self.actionOpen_Interview_File = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/Open_Interview_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionOpen_Interview_File.setIcon(icon2)
        self.actionOpen_Interview_File.setObjectName("actionOpen_Interview_File")
        self.actionSave_Current_Interview_File = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/Save_Interview_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionSave_Current_Interview_File.setIcon(icon3)
        self.actionSave_Current_Interview_File.setObjectName("actionSave_Current_Interview_File")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/Exit_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionInterview_Account_Setup = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/Menu_Setup_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionInterview_Account_Setup.setIcon(icon5)
        self.actionInterview_Account_Setup.setObjectName("actionInterview_Account_Setup")
        self.actionComplex_Indicators_Setup = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/Interview_Account_Setup.jpg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionComplex_Indicators_Setup.setIcon(icon6)
        self.actionComplex_Indicators_Setup.setObjectName("actionComplex_Indicators_Setup")
        self.actionPredefined_Words_Setup = QtWidgets.QAction(MainWindow)
        self.actionPredefined_Words_Setup.setObjectName("actionPredefined_Words_Setup")
        self.actionCurrent_Interview_Result_Edit = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/Menu_Edit_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionCurrent_Interview_Result_Edit.setIcon(icon7)
        self.actionCurrent_Interview_Result_Edit.setObjectName("actionCurrent_Interview_Result_Edit")
        self.actionComplex_Indicators_Edit = QtWidgets.QAction(MainWindow)
        self.actionComplex_Indicators_Edit.setObjectName("actionComplex_Indicators_Edit")
        self.actionPredefined_Words_Edit = QtWidgets.QAction(MainWindow)
        self.actionPredefined_Words_Edit.setObjectName("actionPredefined_Words_Edit")
        self.actionCurrent_Interview_Details_Edit = QtWidgets.QAction(MainWindow)
        self.actionCurrent_Interview_Details_Edit.setObjectName("actionCurrent_Interview_Details_Edit")
        self.actionLast_Interview_Report_View = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/Menu_View_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionLast_Interview_Report_View.setIcon(icon8)
        self.actionLast_Interview_Report_View.setObjectName("actionLast_Interview_Report_View")
        self.actionGraphical_Visualization_View = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/Graphical_Visualization_View_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionGraphical_Visualization_View.setIcon(icon9)
        self.actionGraphical_Visualization_View.setObjectName("actionGraphical_Visualization_View")
        self.action_All_In_One_file = QtWidgets.QAction(MainWindow)
        self.action_All_In_One_file.setObjectName("action_All_In_One_file")
        self.actionExport_to_pdf = QtWidgets.QAction(MainWindow)
        self.actionExport_to_pdf.setObjectName("actionExport_to_pdf")
        self.actionGenerate_Report = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/Menu_Dashboard_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionGenerate_Report.setIcon(icon10)
        self.actionGenerate_Report.setObjectName("actionGenerate_Report")
        self.actionPredefined_Words_Search = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/Menu_Search_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionPredefined_Words_Search.setIcon(icon11)
        self.actionPredefined_Words_Search.setObjectName("actionPredefined_Words_Search")
        self.actionIn_Last_Interview_Search = QtWidgets.QAction(MainWindow)
        self.actionIn_Last_Interview_Search.setObjectName("actionIn_Last_Interview_Search")
        self.actionIn_Last_Report_Search = QtWidgets.QAction(MainWindow)
        self.actionIn_Last_Report_Search.setObjectName("actionIn_Last_Report_Search")
        self.actionAbout_Help = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/Menu_Help_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionAbout_Help.setIcon(icon12)
        self.actionAbout_Help.setObjectName("actionAbout_Help")
        self.actionResume_Interview = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/Resume_Interview_logo.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionResume_Interview.setIcon(icon13)
        self.actionResume_Interview.setObjectName("actionResume_Interview")
        self.actionExport_Report_To_Png = QtWidgets.QAction(MainWindow)
        self.actionExport_Report_To_Png.setObjectName("actionExport_Report_To_Png")
        self.actionSave_Generated_Report = QtWidgets.QAction(MainWindow)
        self.actionSave_Generated_Report.setIcon(icon3)
        self.actionSave_Generated_Report.setObjectName("actionSave_Generated_Report")
        self.actionExport_Generated_Report_To_PDF = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/Export_Generated_Report_To_PDF_logo.jpg"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.actionExport_Generated_Report_To_PDF.setIcon(icon14)
        self.actionExport_Generated_Report_To_PDF.setObjectName("actionExport_Generated_Report_To_PDF")
        self.actionOpen_Generated_Report = QtWidgets.QAction(MainWindow)
        self.actionOpen_Generated_Report.setIcon(icon2)
        self.actionOpen_Generated_Report.setObjectName("actionOpen_Generated_Report")
        self.menuInterview.addAction(self.actionNew_Interview)
        self.menuInterview.addAction(self.actionOpen_Interview_File)
        self.menuInterview.addAction(self.actionOpen_Generated_Report)
        self.menuInterview.addAction(self.actionResume_Interview)
        self.menuInterview.addAction(self.actionSave_Current_Interview_File)
        self.menuInterview.addAction(self.actionSave_Generated_Report)
        self.menuInterview.addAction(self.actionExport_Generated_Report_To_PDF)
        self.menuInterview.addAction(self.actionExit)
        self.menuSetup.addAction(self.actionInterview_Account_Setup)
        self.menuSetup.addAction(self.actionComplex_Indicators_Setup)
        self.menuSetup.addAction(self.actionPredefined_Words_Setup)
        self.menuEdit.addAction(self.actionCurrent_Interview_Result_Edit)
        self.menuEdit.addAction(self.actionComplex_Indicators_Edit)
        self.menuEdit.addAction(self.actionPredefined_Words_Edit)
        self.menuEdit.addAction(self.actionCurrent_Interview_Details_Edit)
        self.menuView.addAction(self.actionLast_Interview_Report_View)
        self.menuView.addAction(self.actionGraphical_Visualization_View)
        self.menuDashboard.addAction(self.actionGenerate_Report)
        self.menuDashboard.addAction(self.actionExport_Report_To_Png)
        self.menuSearch.addAction(self.actionPredefined_Words_Search)
        self.menuSearch.addAction(self.actionIn_Last_Interview_Search)
        self.menuSearch.addAction(self.actionIn_Last_Report_Search)
        self.menuHelp.addAction(self.actionAbout_Help)
        self.menubar.addAction(self.menuInterview.menuAction())
        self.menubar.addAction(self.menuSetup.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuDashboard.menuAction())
        self.menubar.addAction(self.menuSearch.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Word Association Tester"))
        self.menuInterview.setTitle(_translate("MainWindow", "Interview"))
        self.menuSetup.setTitle(_translate("MainWindow", "Setup Interview"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuDashboard.setTitle(_translate("MainWindow", "Dashboard"))
        self.menuSearch.setTitle(_translate("MainWindow", "Search Words"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Interview.setText(_translate("MainWindow", "New Interview"))
        self.actionNew_Interview.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen_Interview_File.setText(_translate("MainWindow", "Open Interview"))
        self.actionOpen_Interview_File.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Current_Interview_File.setText(_translate("MainWindow", "Save Current Interview"))
        self.actionSave_Current_Interview_File.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionInterview_Account_Setup.setText(_translate("MainWindow", "Interview Account"))
        self.actionInterview_Account_Setup.setShortcut(_translate("MainWindow", "Shift+S"))
        self.actionComplex_Indicators_Setup.setText(_translate("MainWindow", "Complex Indicators"))
        self.actionComplex_Indicators_Setup.setShortcut(_translate("MainWindow", "Shift+C"))
        self.actionPredefined_Words_Setup.setText(_translate("MainWindow", "Predefined Words"))
        self.actionPredefined_Words_Setup.setShortcut(_translate("MainWindow", "Shift+W"))
        self.actionCurrent_Interview_Result_Edit.setText(_translate("MainWindow", "Current Interview Result"))
        self.actionCurrent_Interview_Result_Edit.setShortcut(_translate("MainWindow", "Alt+R"))
        self.actionComplex_Indicators_Edit.setText(_translate("MainWindow", "Complex Indicators"))
        self.actionComplex_Indicators_Edit.setShortcut(_translate("MainWindow", "Alt+C"))
        self.actionPredefined_Words_Edit.setText(_translate("MainWindow", "Predefined Words"))
        self.actionPredefined_Words_Edit.setShortcut(_translate("MainWindow", "Alt+W"))
        self.actionCurrent_Interview_Details_Edit.setText(_translate("MainWindow", "Current Interview Details"))
        self.actionCurrent_Interview_Details_Edit.setShortcut(_translate("MainWindow", "Alt+D"))
        self.actionLast_Interview_Report_View.setText(_translate("MainWindow", "Last Interview Report"))
        self.actionLast_Interview_Report_View.setShortcut(_translate("MainWindow", "Shift+R"))
        self.actionGraphical_Visualization_View.setText(_translate("MainWindow", "Graphical Visualization"))
        self.action_All_In_One_file.setText(_translate("MainWindow", " All In One file"))
        self.actionExport_to_pdf.setText(_translate("MainWindow", "Export to pdf"))
        self.actionGenerate_Report.setText(_translate("MainWindow", "Generate Report"))
        self.actionGenerate_Report.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.actionPredefined_Words_Search.setText(_translate("MainWindow", "Predefined Words"))
        self.actionPredefined_Words_Search.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionIn_Last_Interview_Search.setText(_translate("MainWindow", "In Last Interview"))
        self.actionIn_Last_Report_Search.setText(_translate("MainWindow", "In Last Report"))
        self.actionAbout_Help.setText(_translate("MainWindow", "About"))
        self.actionResume_Interview.setText(_translate("MainWindow", "Resume Interview"))
        self.actionResume_Interview.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionExport_Report_To_Png.setText(_translate("MainWindow", "Export Report to *.png"))
        self.actionExport_Report_To_Png.setShortcut(_translate("MainWindow", "Shift+E"))
        self.actionSave_Generated_Report.setText(_translate("MainWindow", "Save Generated Report"))
        self.actionSave_Generated_Report.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionExport_Generated_Report_To_PDF.setText(_translate("MainWindow", "Export Generated Rport To PDF"))
        self.actionExport_Generated_Report_To_PDF.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionOpen_Generated_Report.setText(_translate("MainWindow", "Open Generated Report"))
        self.actionOpen_Generated_Report.setShortcut(_translate("MainWindow", "Alt+O"))
import src_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
