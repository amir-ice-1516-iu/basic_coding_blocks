# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Files/PredefinedWords.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 500)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(1, 1, 1021, 491))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.wordToSearch = QtWidgets.QLineEdit(self.widget)
        self.wordToSearch.setObjectName("wordToSearch")
        self.horizontalLayout.addWidget(self.wordToSearch)
        self.searchPredefinedWord = QtWidgets.QPushButton(self.widget)
        self.searchPredefinedWord.setObjectName("searchPredefinedWord")
        self.horizontalLayout.addWidget(self.searchPredefinedWord)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.wordsTable = QtWidgets.QTableWidget(self.widget)
        self.wordsTable.setShowGrid(True)
        self.wordsTable.setWordWrap(True)
        self.wordsTable.setCornerButtonEnabled(True)
        self.wordsTable.setObjectName("wordsTable")
        self.wordsTable.setColumnCount(4)
        self.wordsTable.setRowCount(50)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(33, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(34, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(35, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(36, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(37, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(38, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(39, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(40, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(41, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(42, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(43, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(44, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(45, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(46, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(47, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(48, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setVerticalHeaderItem(49, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.wordsTable.setHorizontalHeaderItem(3, item)
        self.wordsTable.horizontalHeader().setVisible(True)
        self.wordsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.wordsTable.horizontalHeader().setDefaultSectionSize(240)
        self.verticalLayout.addWidget(self.wordsTable)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.removeWord = QtWidgets.QCheckBox(self.widget)
        self.removeWord.setObjectName("removeWord")
        self.horizontalLayout_3.addWidget(self.removeWord)
        self.updatedWordToCommit = QtWidgets.QLineEdit(self.widget)
        self.updatedWordToCommit.setObjectName("updatedWordToCommit")
        self.horizontalLayout_3.addWidget(self.updatedWordToCommit)
        self.addWord = QtWidgets.QCheckBox(self.widget)
        self.addWord.setObjectName("addWord")
        self.horizontalLayout_3.addWidget(self.addWord)
        self.wordToUpdate = QtWidgets.QPushButton(self.widget)
        self.wordToUpdate.setObjectName("wordToUpdate")
        self.horizontalLayout_3.addWidget(self.wordToUpdate)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PredefinedWords"))
        self.searchPredefinedWord.setText(_translate("Form", "Search Word"))
        self.wordsTable.setSortingEnabled(False)
        item = self.wordsTable.verticalHeaderItem(0)
        item.setText(_translate("Form", "1X"))
        item = self.wordsTable.verticalHeaderItem(1)
        item.setText(_translate("Form", "2x"))
        item = self.wordsTable.verticalHeaderItem(2)
        item.setText(_translate("Form", "3X"))
        item = self.wordsTable.verticalHeaderItem(3)
        item.setText(_translate("Form", "4X"))
        item = self.wordsTable.verticalHeaderItem(4)
        item.setText(_translate("Form", "5X"))
        item = self.wordsTable.verticalHeaderItem(5)
        item.setText(_translate("Form", "6X"))
        item = self.wordsTable.verticalHeaderItem(6)
        item.setText(_translate("Form", "7X"))
        item = self.wordsTable.verticalHeaderItem(7)
        item.setText(_translate("Form", "8X"))
        item = self.wordsTable.verticalHeaderItem(8)
        item.setText(_translate("Form", "9X"))
        item = self.wordsTable.verticalHeaderItem(9)
        item.setText(_translate("Form", "10X"))
        item = self.wordsTable.verticalHeaderItem(10)
        item.setText(_translate("Form", "11X"))
        item = self.wordsTable.verticalHeaderItem(11)
        item.setText(_translate("Form", "12X"))
        item = self.wordsTable.verticalHeaderItem(12)
        item.setText(_translate("Form", "13X"))
        item = self.wordsTable.verticalHeaderItem(13)
        item.setText(_translate("Form", "14X"))
        item = self.wordsTable.verticalHeaderItem(14)
        item.setText(_translate("Form", "15X"))
        item = self.wordsTable.verticalHeaderItem(15)
        item.setText(_translate("Form", "16X"))
        item = self.wordsTable.verticalHeaderItem(16)
        item.setText(_translate("Form", "17X"))
        item = self.wordsTable.verticalHeaderItem(17)
        item.setText(_translate("Form", "18X"))
        item = self.wordsTable.verticalHeaderItem(18)
        item.setText(_translate("Form", "19X"))
        item = self.wordsTable.verticalHeaderItem(19)
        item.setText(_translate("Form", "20X"))
        item = self.wordsTable.verticalHeaderItem(20)
        item.setText(_translate("Form", "21X"))
        item = self.wordsTable.verticalHeaderItem(21)
        item.setText(_translate("Form", "22X"))
        item = self.wordsTable.verticalHeaderItem(22)
        item.setText(_translate("Form", "23X"))
        item = self.wordsTable.verticalHeaderItem(23)
        item.setText(_translate("Form", "24X"))
        item = self.wordsTable.verticalHeaderItem(24)
        item.setText(_translate("Form", "25X"))
        item = self.wordsTable.verticalHeaderItem(25)
        item.setText(_translate("Form", "26X"))
        item = self.wordsTable.verticalHeaderItem(26)
        item.setText(_translate("Form", "27X"))
        item = self.wordsTable.verticalHeaderItem(27)
        item.setText(_translate("Form", "28X"))
        item = self.wordsTable.verticalHeaderItem(28)
        item.setText(_translate("Form", "29X"))
        item = self.wordsTable.verticalHeaderItem(29)
        item.setText(_translate("Form", "30X"))
        item = self.wordsTable.verticalHeaderItem(30)
        item.setText(_translate("Form", "31X"))
        item = self.wordsTable.verticalHeaderItem(31)
        item.setText(_translate("Form", "32X"))
        item = self.wordsTable.verticalHeaderItem(32)
        item.setText(_translate("Form", "33X"))
        item = self.wordsTable.verticalHeaderItem(33)
        item.setText(_translate("Form", "34X"))
        item = self.wordsTable.verticalHeaderItem(34)
        item.setText(_translate("Form", "35X"))
        item = self.wordsTable.verticalHeaderItem(35)
        item.setText(_translate("Form", "36X"))
        item = self.wordsTable.verticalHeaderItem(36)
        item.setText(_translate("Form", "37X"))
        item = self.wordsTable.verticalHeaderItem(37)
        item.setText(_translate("Form", "38X"))
        item = self.wordsTable.verticalHeaderItem(38)
        item.setText(_translate("Form", "39X"))
        item = self.wordsTable.verticalHeaderItem(39)
        item.setText(_translate("Form", "40X"))
        item = self.wordsTable.verticalHeaderItem(40)
        item.setText(_translate("Form", "41X"))
        item = self.wordsTable.verticalHeaderItem(41)
        item.setText(_translate("Form", "42X"))
        item = self.wordsTable.verticalHeaderItem(42)
        item.setText(_translate("Form", "43X"))
        item = self.wordsTable.verticalHeaderItem(43)
        item.setText(_translate("Form", "44X"))
        item = self.wordsTable.verticalHeaderItem(44)
        item.setText(_translate("Form", "45X"))
        item = self.wordsTable.verticalHeaderItem(45)
        item.setText(_translate("Form", "46X"))
        item = self.wordsTable.verticalHeaderItem(46)
        item.setText(_translate("Form", "47X"))
        item = self.wordsTable.verticalHeaderItem(47)
        item.setText(_translate("Form", "48X"))
        item = self.wordsTable.verticalHeaderItem(48)
        item.setText(_translate("Form", "49X"))
        item = self.wordsTable.verticalHeaderItem(49)
        item.setText(_translate("Form", "50X"))
        item = self.wordsTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "|                    1st Quatar                   |"))
        item = self.wordsTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "|                    2nd Quatar                  |"))
        item = self.wordsTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "|                    3rd Quatar                   |"))
        item = self.wordsTable.horizontalHeaderItem(3)
        item.setText(_translate("Form", "|                    4th Quatar                   |"))
        self.removeWord.setText(_translate("Form", "Remove Word"))
        self.addWord.setText(_translate("Form", "Add Word"))
        self.wordToUpdate.setText(_translate("Form", "Update Word"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())