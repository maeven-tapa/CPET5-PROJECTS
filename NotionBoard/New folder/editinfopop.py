# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\maeve\Desktop\nb_app\ui\editinfopop.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_editinfopop(object):
    def setupUi(self, editinfopop):
        editinfopop.setObjectName("editinfopop")
        editinfopop.resize(546, 583)
        self.centralwidget = QtWidgets.QWidget(editinfopop)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 651, 601))
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-20, 0, 691, 631))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.widget.setObjectName("widget")
        self.edit_btn = QtWidgets.QPushButton(self.widget)
        self.edit_btn.setGeometry(QtCore.QRect(110, 445, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(15)
        self.edit_btn.setFont(font)
        self.edit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_btn.setStyleSheet("QPushButton {background-color: rgb(21, 21, 21); border-radius: 30px; color: white;}\n"
"\n"
"QPushButton:hover {border-radius: 30px; color: white; background-color: rgb(85, 170, 255);}\n"
"")
        self.edit_btn.setObjectName("edit_btn")
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
        self.editback_btn = QtWidgets.QPushButton(self.widget)
        self.editback_btn.setEnabled(True)
        self.editback_btn.setGeometry(QtCore.QRect(210, 40, 71, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.editback_btn.setFont(font)
        self.editback_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editback_btn.setStyleSheet("QPushButton {border-radius: 20px; color: white; background-color: rgb(255, 85, 127);}\n"
"\n"
"QPushButton:hover {border-radius: 20px; border: 1px solid #FF557F; color: rgb(255, 85, 127); background-color: white; }\n"
"")
        self.editback_btn.setObjectName("editback_btn")
        self.frm_board_2 = QtWidgets.QListWidget(self.widget)
        self.frm_board_2.setGeometry(QtCore.QRect(70, 100, 441, 431))
        self.frm_board_2.setStyleSheet(" border-radius: 20px;\n"
"background-color: rgb(243, 243, 243);")
        self.frm_board_2.setObjectName("frm_board_2")
        self.birthdayedit = QtWidgets.QLineEdit(self.widget)
        self.birthdayedit.setGeometry(QtCore.QRect(110, 267, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.birthdayedit.setFont(font)
        self.birthdayedit.setStyleSheet("background-color: none; border-radius: 20px; color: grey;   border: 1px solid black;\n"
"")
        self.birthdayedit.setAlignment(QtCore.Qt.AlignCenter)
        self.birthdayedit.setObjectName("birthdayedit")
        self.genderedit = QtWidgets.QLineEdit(self.widget)
        self.genderedit.setGeometry(QtCore.QRect(110, 366, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.genderedit.setFont(font)
        self.genderedit.setStyleSheet("background-color: none; border-radius: 20px; color: grey;   border: 1px solid black;\n"
"")
        self.genderedit.setAlignment(QtCore.Qt.AlignCenter)
        self.genderedit.setObjectName("genderedit")
        self.nameedit = QtWidgets.QLineEdit(self.widget)
        self.nameedit.setGeometry(QtCore.QRect(110, 170, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.nameedit.setFont(font)
        self.nameedit.setStyleSheet("background-color: none; border-radius: 20px; color: grey;   border: 1px solid black;\n"
"")
        self.nameedit.setAlignment(QtCore.Qt.AlignCenter)
        self.nameedit.setObjectName("nameedit")
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
        self.edit_btn.raise_()
        self.tags_pinfo.raise_()
        self.editback_btn.raise_()
        self.birthdayedit.raise_()
        self.genderedit.raise_()
        self.nameedit.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.retranslateUi(editinfopop)
        QtCore.QMetaObject.connectSlotsByName(editinfopop)

    def retranslateUi(self, editinfopop):
        _translate = QtCore.QCoreApplication.translate
        editinfopop.setWindowTitle(_translate("editinfopop", "Dialog"))
        self.edit_btn.setText(_translate("editinfopop", "Confirm"))
        self.tags_pinfo.setText(_translate("editinfopop", "Edit Info"))
        self.editback_btn.setText(_translate("editinfopop", "Back"))
        self.birthdayedit.setText(_translate("editinfopop", "When is your birthday?"))
        self.birthdayedit.setPlaceholderText(_translate("editinfopop", "How\'s the progress?"))
        self.genderedit.setText(_translate("editinfopop", "What\'s your gender?"))
        self.genderedit.setPlaceholderText(_translate("editinfopop", "Do you have a tag for that?"))
        self.nameedit.setText(_translate("editinfopop", "What\'s your name?"))
        self.nameedit.setPlaceholderText(_translate("editinfopop", "What to do?"))
        self.label_3.setText(_translate("editinfopop", "Name:"))
        self.label.setText(_translate("editinfopop", "Gender:"))
        self.label_2.setText(_translate("editinfopop", "Birthday"))
