# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Files/Interview.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.complexIndicatorsSelection = QtWidgets.QWidget(Form)
        self.complexIndicatorsSelection.setGeometry(QtCore.QRect(0, 164, 1024, 271))
        self.complexIndicatorsSelection.setObjectName("complexIndicatorsSelection")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1021, 160))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.interviewDetailsLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.interviewDetailsLabel.setFont(font)
        self.interviewDetailsLabel.setObjectName("interviewDetailsLabel")
        self.verticalLayout_2.addWidget(self.interviewDetailsLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.wordSerialNumberLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.wordSerialNumberLabel.setFont(font)
        self.wordSerialNumberLabel.setObjectName("wordSerialNumberLabel")
        self.horizontalLayout_3.addWidget(self.wordSerialNumberLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.testWordLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.testWordLabel.setFont(font)
        self.testWordLabel.setStyleSheet("")
        self.testWordLabel.setObjectName("testWordLabel")
        self.horizontalLayout_3.addWidget(self.testWordLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.testRoundLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.testRoundLabel.setFont(font)
        self.testRoundLabel.setObjectName("testRoundLabel")
        self.horizontalLayout_3.addWidget(self.testRoundLabel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.interviewOperationalButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.interviewOperationalButton.setFont(font)
        self.interviewOperationalButton.setObjectName("interviewOperationalButton")
        self.horizontalLayout_2.addWidget(self.interviewOperationalButton)
        self.timerLabel = QtWidgets.QLCDNumber(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.timerLabel.setFont(font)
        self.timerLabel.setSmallDecimalPoint(False)
        self.timerLabel.setProperty("value", 0.0)
        self.timerLabel.setObjectName("timerLabel")
        self.horizontalLayout_2.addWidget(self.timerLabel)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.timeTakenLabel = QtWidgets.QLabel(self.layoutWidget)
        self.timeTakenLabel.setObjectName("timeTakenLabel")
        self.verticalLayout.addWidget(self.timeTakenLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.responseWrodLabel = QtWidgets.QLabel(self.layoutWidget)
        self.responseWrodLabel.setObjectName("responseWrodLabel")
        self.horizontalLayout.addWidget(self.responseWrodLabel)
        self.lastResponseWord = QtWidgets.QLineEdit(self.layoutWidget)
        self.lastResponseWord.setObjectName("lastResponseWord")
        self.horizontalLayout.addWidget(self.lastResponseWord)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 456, 1021, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.closeWidgetButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.closeWidgetButton.setObjectName("closeWidgetButton")
        self.horizontalLayout_5.addWidget(self.closeWidgetButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.infoLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.infoLabel.setObjectName("infoLabel")
        self.horizontalLayout_5.addWidget(self.infoLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Interview"))
        self.interviewDetailsLabel.setText(_translate("Form", "Dummy Interview Details"))
        self.wordSerialNumberLabel.setText(_translate("Form", "Word SL"))
        self.testWordLabel.setText(_translate("Form", "Dummy Word"))
        self.testRoundLabel.setText(_translate("Form", "Round"))
        self.interviewOperationalButton.setText(_translate("Form", "Timer/Next"))
        self.timeTakenLabel.setText(_translate("Form", "Time Taken        :"))
        self.responseWrodLabel.setText(_translate("Form", "Response Word:"))
        self.closeWidgetButton.setText(_translate("Form", "Close"))
        self.closeWidgetButton.setShortcut(_translate("Form", "Esc"))
        self.infoLabel.setText(_translate("Form", "*Press Esc to close any time"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
