# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\maeve\Desktop\nb_app\ui\addstudpop.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addstudpop(object):
    def setupUi(self, addstudpop):
        addstudpop.setObjectName("addstudpop")
        addstudpop.resize(544, 583)
        self.centralwidget = QtWidgets.QWidget(addstudpop)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 651, 601))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-20, 0, 691, 631))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.widget.setObjectName("widget")
        self.addstud_btn = QtWidgets.QPushButton(self.widget)
        self.addstud_btn.setGeometry(QtCore.QRect(110, 445, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(15)
        self.addstud_btn.setFont(font)
        self.addstud_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addstud_btn.setStyleSheet("QPushButton {background-color: rgb(21, 21, 21); border-radius: 30px; color: white;}\n"
"\n"
"QPushButton:hover {border-radius: 30px; color: white; background-color: rgb(85, 170, 255);}\n"
"")
        self.addstud_btn.setObjectName("addstud_btn")
        self.frm_board = QtWidgets.QListWidget(self.widget)
        self.frm_board.setGeometry(QtCore.QRect(40, 20, 501, 541))
        self.frm_board.setStyleSheet(" border-radius: 20px; border: 1px solid grey; \n"
"background-color: rgb(255, 255, 255);")
        self.frm_board.setObjectName("frm_board")
        self.tags_pinfo = QtWidgets.QPushButton(self.widget)
        self.tags_pinfo.setEnabled(False)
        self.tags_pinfo.setGeometry(QtCore.QRect(69, 41, 130, 37))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tags_pinfo.setFont(font)
        self.tags_pinfo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tags_pinfo.setStyleSheet("background-color: none; border-radius: 18px; color: black;   border: 1px solid grey;")
        self.tags_pinfo.setObjectName("tags_pinfo")
        self.addstudback_btn = QtWidgets.QPushButton(self.widget)
        self.addstudback_btn.setEnabled(True)
        self.addstudback_btn.setGeometry(QtCore.QRect(210, 40, 71, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.addstudback_btn.setFont(font)
        self.addstudback_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.addstudback_btn.setStyleSheet("QPushButton {border-radius: 20px; color: white; background-color: rgb(255, 85, 127);}\n"
"\n"
"QPushButton:hover {border-radius: 20px; border: 1px solid #FF557F; color: rgb(255, 85, 127); background-color: white; }\n"
"")
        self.addstudback_btn.setObjectName("addstudback_btn")
        self.frm_board_2 = QtWidgets.QListWidget(self.widget)
        self.frm_board_2.setGeometry(QtCore.QRect(70, 100, 441, 431))
        self.frm_board_2.setStyleSheet(" border-radius: 20px;\n"
"background-color: rgb(243, 243, 243);")
        self.frm_board_2.setObjectName("frm_board_2")
        self.studbirthdayedit = QtWidgets.QLineEdit(self.widget)
        self.studbirthdayedit.setGeometry(QtCore.QRect(110, 267, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.studbirthdayedit.setFont(font)
        self.studbirthdayedit.setStyleSheet("background-color: none; border-radius: 20px; color: grey;   border: 1px solid black;\n"
"")
        self.studbirthdayedit.setText("")
        self.studbirthdayedit.setAlignment(QtCore.Qt.AlignCenter)
        self.studbirthdayedit.setObjectName("studbirthdayedit")
        self.studgenderedit = QtWidgets.QLineEdit(self.widget)
        self.studgenderedit.setGeometry(QtCore.QRect(110, 366, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.studgenderedit.setFont(font)
        self.studgenderedit.setStyleSheet("background-color: none; border-radius: 20px; color: grey;   border: 1px solid black;\n"
"")
        self.studgenderedit.setText("")
        self.studgenderedit.setAlignment(QtCore.Qt.AlignCenter)
        self.studgenderedit.setObjectName("studgenderedit")
        self.studnameedit = QtWidgets.QLineEdit(self.widget)
        self.studnameedit.setGeometry(QtCore.QRect(110, 170, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.studnameedit.setFont(font)
        self.studnameedit.setStyleSheet("background-color: none; border-radius: 20px; color: grey;   border: 1px solid black;\n"
"")
        self.studnameedit.setText("")
        self.studnameedit.setAlignment(QtCore.Qt.AlignCenter)
        self.studnameedit.setObjectName("studnameedit")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(110, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: transparent; border: none; color: grey;")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(110, 326, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: transparent; border: none; color: grey;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(110, 228, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: transparent; border: none; color: grey;")
        self.label_2.setObjectName("label_2")
        self.frm_board.raise_()
        self.frm_board_2.raise_()
        self.addstud_btn.raise_()
        self.tags_pinfo.raise_()
        self.addstudback_btn.raise_()
        self.studbirthdayedit.raise_()
        self.studgenderedit.raise_()
        self.studnameedit.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(addstudpop)
        QtCore.QMetaObject.connectSlotsByName(addstudpop)

    def retranslateUi(self, addstudpop):
        _translate = QtCore.QCoreApplication.translate
        addstudpop.setWindowTitle(_translate("addstudpop", "Dialog"))
        self.addstud_btn.setText(_translate("addstudpop", "Confirm"))
        self.tags_pinfo.setText(_translate("addstudpop", "Add-Student"))
        self.addstudback_btn.setText(_translate("addstudpop", "Back"))
        self.studbirthdayedit.setPlaceholderText(_translate("addstudpop", "What about their birthday?"))
        self.studgenderedit.setPlaceholderText(_translate("addstudpop", "What\'s their email address?"))
        self.studnameedit.setPlaceholderText(_translate("addstudpop", "What\'s the student name?"))
        self.label_3.setText(_translate("addstudpop", "Name:"))
        self.label.setText(_translate("addstudpop", "Email:"))
        self.label_2.setText(_translate("addstudpop", "Birthday:"))
