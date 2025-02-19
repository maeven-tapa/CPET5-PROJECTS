# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\maeve\Desktop\nb_app\ui\options.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_options(object):
    def setupUi(self, options):
        options.setObjectName("options")
        options.resize(1153, 721)
        self.main_frm = QtWidgets.QFrame(options)
        self.main_frm.setGeometry(QtCore.QRect(-40, -20, 1301, 761))
        font = QtGui.QFont()
        font.setFamily("Swis721 BlkOul BT")
        font.setPointSize(27)
        self.main_frm.setFont(font)
        self.main_frm.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.main_frm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frm.setObjectName("main_frm")
        self.frm_nav = QtWidgets.QListWidget(self.main_frm)
        self.frm_nav.setGeometry(QtCore.QRect(60, 40, 201, 681))
        self.frm_nav.setStyleSheet(" border-radius: 20px; border: 1px solid grey; \n"
"background-color: rgb(255, 255, 255);")
        self.frm_nav.setObjectName("frm_nav")
        self.frm_todo = QtWidgets.QListWidget(self.main_frm)
        self.frm_todo.setGeometry(QtCore.QRect(281, 42, 431, 431))
        self.frm_todo.setStyleSheet(" border-radius: 20px; border: 1px solid grey; \n"
"background-color: rgb(255, 255, 255);")
        self.frm_todo.setObjectName("frm_todo")
        self.changeusername_btn = QtWidgets.QPushButton(self.main_frm)
        self.changeusername_btn.setGeometry(QtCore.QRect(327, 375, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(15)
        self.changeusername_btn.setFont(font)
        self.changeusername_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changeusername_btn.setStyleSheet("QPushButton {background-color: rgb(21, 21, 21); border-radius: 30px; color: white;}\n"
"\n"
"QPushButton:hover {border-radius: 30px; color: white; background-color: rgb(85, 170, 255);}\n"
"")
        self.changeusername_btn.setObjectName("changeusername_btn")
        self.lb_greetings = QtWidgets.QLabel(self.main_frm)
        self.lb_greetings.setEnabled(True)
        self.lb_greetings.setGeometry(QtCore.QRect(96, 70, 124, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.lb_greetings.setFont(font)
        self.lb_greetings.setToolTip("")
        self.lb_greetings.setAutoFillBackground(False)
        self.lb_greetings.setStyleSheet("background-color: NONE;")
        self.lb_greetings.setObjectName("lb_greetings")
        self.home_frame = QtWidgets.QFrame(self.main_frm)
        self.home_frame.setGeometry(QtCore.QRect(85, 122, 151, 161))
        self.home_frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.home_frame.setStyleSheet(" border-radius: 20px; \n"
"background-color: rgb(221, 205, 249);")
        self.home_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_frame.setObjectName("home_frame")
        self.label_14 = QtWidgets.QLabel(self.home_frame)
        self.label_14.setGeometry(QtCore.QRect(-50, -150, 200, 198))
        self.label_14.setStyleSheet("background-color: none;\n"
"border-radius: 99%; /* Make it circular */\n"
"border: 2px solid purple ; /* Add a border */\n"
"\n"
"")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.home_frame)
        self.label_15.setGeometry(QtCore.QRect(70, -130, 200, 198))
        self.label_15.setStyleSheet("background-color: none;\n"
"border-radius: 99%; /* Make it circular */\n"
"border: 2px solid purple ; /* Add a border */\n"
"\n"
"")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.mainpagetext_53 = QtWidgets.QLabel(self.home_frame)
        self.mainpagetext_53.setGeometry(QtCore.QRect(23, 59, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Square721 BT")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.mainpagetext_53.setFont(font)
        self.mainpagetext_53.setToolTip("")
        self.mainpagetext_53.setAutoFillBackground(False)
        self.mainpagetext_53.setStyleSheet("background-color: transparent; border: none;\n"
"color: purple;\n"
"\n"
"\n"
"")
        self.mainpagetext_53.setObjectName("mainpagetext_53")
        self.label_17 = QtWidgets.QLabel(self.home_frame)
        self.label_17.setGeometry(QtCore.QRect(-56, 120, 200, 198))
        self.label_17.setStyleSheet("background-color: none;\n"
"border-radius: 99%; /* Make it circular */\n"
"border: 2px solid purple ; /* Add a border */\n"
"\n"
"")
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(self.home_frame)
        self.label_16.setGeometry(QtCore.QRect(-150, -110, 200, 198))
        self.label_16.setStyleSheet("background-color: none;\n"
"border-radius: 99%; /* Make it circular */\n"
"border: 2px solid purple ; /* Add a border */\n"
"\n"
"")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.home_btn = QtWidgets.QPushButton(self.home_frame)
        self.home_btn.setGeometry(QtCore.QRect(0, 0, 151, 161))
        self.home_btn.setStyleSheet(" border-radius: 20px; \n"
"background-color: transparent;")
        self.home_btn.setText("")
        self.home_btn.setObjectName("home_btn")
        self.todo_frame = QtWidgets.QFrame(self.main_frm)
        self.todo_frame.setGeometry(QtCore.QRect(85, 328, 151, 161))
        self.todo_frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.todo_frame.setStyleSheet(" border-radius: 20px; \n"
"background-color: rgb(198, 239, 216);")
        self.todo_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.todo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.todo_frame.setObjectName("todo_frame")
        self.label_8 = QtWidgets.QLabel(self.todo_frame)
        self.label_8.setGeometry(QtCore.QRect(-88, 120, 200, 198))
        self.label_8.setStyleSheet("background-color: none;\n"
"border-radius: 99%; /* Make it circular */\n"
"border: 2px solid green ; /* Add a border */\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.todo_frame)
        self.label_9.setGeometry(QtCore.QRect(-168, -117, 200, 198))
        self.label_9.setStyleSheet("background-color: none;\n"
"border-radius: 99%; /* Make it circular */\n"
"border: 2px solid green ; /* Add a border */\n"
"\n"
"")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.mainpagetext_52 = QtWidgets.QLabel(self.todo_frame)
        self.mainpagetext_52.setGeometry(QtCore.QRect(14, 57, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(26)
        self.mainpagetext_52.setFont(font)
        self.mainpagetext_52.setToolTip("")
        self.mainpagetext_52.setAutoFillBackground(False)
        self.mainpagetext_52.setStyleSheet("background-color: transparent; border: none;\n"
"color: green;\n"
"\n"
"\n"
"")
        self.mainpagetext_52.setObjectName("mainpagetext_52")
        self.label_10 = QtWidgets.QLabel(self.todo_frame)
        self.label_10.setGeometry(QtCore.QRect(0, -160, 200, 198))
        self.label_10.setStyleSheet("background-color: none;\n"
"border-radius: 99%; /* Make it circular */\n"
"border: 2px solid green ; /* Add a border */\n"
"\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.todo_btn = QtWidgets.QPushButton(self.todo_frame)
        self.todo_btn.setGeometry(QtCore.QRect(0, 0, 151, 161))
        self.todo_btn.setStyleSheet(" border-radius: 20px; \n"
"background-color: transparent;")
        self.todo_btn.setText("")
        self.todo_btn.setObjectName("todo_btn")
        self.opt_frame = QtWidgets.QFrame(self.main_frm)
        self.opt_frame.setGeometry(QtCore.QRect(84, 537, 151, 161))
        self.opt_frame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.opt_frame.setStyleSheet(" border-radius: 20px; \n"
"background-color: rgb(211, 217, 250);")
        self.opt_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.opt_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.opt_frame.setObjectName("opt_frame")
        self.label_12 = QtWidgets.QLabel(self.opt_frame)
        self.label_12.setGeometry(QtCore.QRect(-168, -117, 200, 198))
        self.label_12.setStyleSheet("background-color: none;\n"
"border-radius: 99%; /* Make it circular */\n"
"border: 2px solid blue;\n"
"")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.mainpagetext_61 = QtWidgets.QLabel(self.opt_frame)
        self.mainpagetext_61.setGeometry(QtCore.QRect(38, 56, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Swis721 Blk BT")
        font.setPointSize(24)
        self.mainpagetext_61.setFont(font)
        self.mainpagetext_61.setToolTip("")
        self.mainpagetext_61.setAutoFillBackground(False)
        self.mainpagetext_61.setStyleSheet("background-color: transparent; border: none; \n"
"color: blue;")
        self.mainpagetext_61.setObjectName("mainpagetext_61")
        self.label_11 = QtWidgets.QLabel(self.opt_frame)
        self.label_11.setGeometry(QtCore.QRect(-30, 110, 200, 198))
        self.label_11.setStyleSheet("background-color: none;\n"
"border-radius: 99%; /* Make it circular */\n"
"border: 2px solid blue;\n"
"")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.opt_frame)
        self.label_13.setGeometry(QtCore.QRect(48, -137, 200, 198))
        self.label_13.setStyleSheet("background-color: none;\n"
"border-radius: 99%; /* Make it circular */\n"
"border: 2px solid blue;\n"
"")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.username = QtWidgets.QLineEdit(self.main_frm)
        self.username.setGeometry(QtCore.QRect(330, 180, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color: none; border-radius: 20px; color: grey;   border: 1px solid black;")
        self.username.setText("")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.SUTEXT_3 = QtWidgets.QTextEdit(self.main_frm)
        self.SUTEXT_3.setEnabled(False)
        self.SUTEXT_3.setGeometry(QtCore.QRect(330, 243, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        self.SUTEXT_3.setFont(font)
        self.SUTEXT_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.SUTEXT_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SUTEXT_3.setStyleSheet("background-color: transparent; border: none;")
        self.SUTEXT_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SUTEXT_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SUTEXT_3.setObjectName("SUTEXT_3")
        self.SUTEXT_2 = QtWidgets.QTextEdit(self.main_frm)
        self.SUTEXT_2.setEnabled(False)
        self.SUTEXT_2.setGeometry(QtCore.QRect(330, 135, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        self.SUTEXT_2.setFont(font)
        self.SUTEXT_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.SUTEXT_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SUTEXT_2.setStyleSheet("background-color: transparent; border: none;")
        self.SUTEXT_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SUTEXT_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SUTEXT_2.setObjectName("SUTEXT_2")
        self.confirm_username = QtWidgets.QLineEdit(self.main_frm)
        self.confirm_username.setGeometry(QtCore.QRect(330, 290, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.confirm_username.setFont(font)
        self.confirm_username.setStyleSheet("background-color: none; border-radius: 20px; color: grey;   border: 1px solid black;")
        self.confirm_username.setText("")
        self.confirm_username.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_username.setObjectName("confirm_username")
        self.tags_todolist = QtWidgets.QPushButton(self.main_frm)
        self.tags_todolist.setEnabled(False)
        self.tags_todolist.setGeometry(QtCore.QRect(320, 70, 181, 37))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tags_todolist.setFont(font)
        self.tags_todolist.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tags_todolist.setStyleSheet("background-color: none; border-radius: 18px; color: black;   border: 1px solid grey;")
        self.tags_todolist.setObjectName("tags_todolist")
        self.confirm_password = QtWidgets.QLineEdit(self.main_frm)
        self.confirm_password.setGeometry(QtCore.QRect(780, 285, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.confirm_password.setFont(font)
        self.confirm_password.setStyleSheet("background-color: none; border-radius: 20px; color: grey;   border: 1px solid black;")
        self.confirm_password.setText("")
        self.confirm_password.setAlignment(QtCore.Qt.AlignCenter)
        self.confirm_password.setObjectName("confirm_password")
        self.SUTEXT_6 = QtWidgets.QTextEdit(self.main_frm)
        self.SUTEXT_6.setEnabled(False)
        self.SUTEXT_6.setGeometry(QtCore.QRect(780, 238, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        self.SUTEXT_6.setFont(font)
        self.SUTEXT_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.SUTEXT_6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SUTEXT_6.setStyleSheet("background-color: transparent; border: none;")
        self.SUTEXT_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SUTEXT_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SUTEXT_6.setObjectName("SUTEXT_6")
        self.password = QtWidgets.QLineEdit(self.main_frm)
        self.password.setGeometry(QtCore.QRect(780, 175, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: none; border-radius: 20px; color: grey;   border: 1px solid black;")
        self.password.setText("")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.frm_todo_3 = QtWidgets.QListWidget(self.main_frm)
        self.frm_todo_3.setGeometry(QtCore.QRect(734, 41, 431, 431))
        self.frm_todo_3.setStyleSheet(" border-radius: 20px; border: 1px solid grey; \n"
"background-color: rgb(255, 255, 255);")
        self.frm_todo_3.setObjectName("frm_todo_3")
        self.SUTEXT_7 = QtWidgets.QTextEdit(self.main_frm)
        self.SUTEXT_7.setEnabled(False)
        self.SUTEXT_7.setGeometry(QtCore.QRect(780, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        self.SUTEXT_7.setFont(font)
        self.SUTEXT_7.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.SUTEXT_7.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SUTEXT_7.setStyleSheet("background-color: transparent; border: none;")
        self.SUTEXT_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SUTEXT_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SUTEXT_7.setObjectName("SUTEXT_7")
        self.tags_todolist_3 = QtWidgets.QPushButton(self.main_frm)
        self.tags_todolist_3.setEnabled(False)
        self.tags_todolist_3.setGeometry(QtCore.QRect(771, 72, 181, 37))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tags_todolist_3.setFont(font)
        self.tags_todolist_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tags_todolist_3.setStyleSheet("background-color: none; border-radius: 18px; color: black;   border: 1px solid grey;")
        self.tags_todolist_3.setObjectName("tags_todolist_3")
        self.delete_acc = QtWidgets.QFrame(self.main_frm)
        self.delete_acc.setGeometry(QtCore.QRect(501, 496, 451, 211))
        self.delete_acc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_acc.setStyleSheet(" border-radius: 20px; \n"
"background-color: rgb(255, 158, 158);")
        self.delete_acc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.delete_acc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.delete_acc.setObjectName("delete_acc")
        self.tags_todolist_4 = QtWidgets.QPushButton(self.delete_acc)
        self.tags_todolist_4.setEnabled(False)
        self.tags_todolist_4.setGeometry(QtCore.QRect(23, 20, 181, 37))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tags_todolist_4.setFont(font)
        self.tags_todolist_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tags_todolist_4.setStyleSheet("background-color: none; border-radius: 18px; color: white;   border: 1px solid white;")
        self.tags_todolist_4.setObjectName("tags_todolist_4")
        self.SUTEXT_8 = QtWidgets.QTextEdit(self.delete_acc)
        self.SUTEXT_8.setEnabled(False)
        self.SUTEXT_8.setGeometry(QtCore.QRect(130, 90, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        self.SUTEXT_8.setFont(font)
        self.SUTEXT_8.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.SUTEXT_8.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.SUTEXT_8.setStyleSheet("background-color: transparent; border: none;")
        self.SUTEXT_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SUTEXT_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.SUTEXT_8.setObjectName("SUTEXT_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.delete_acc)
        self.lineEdit_7.setGeometry(QtCore.QRect(51, 144, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Swis721 BT")
        font.setPointSize(12)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color:white; border-radius: 20px; color: grey;   border: 1px solid grey;")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.delacc_btn = QtWidgets.QPushButton(self.delete_acc)
        self.delacc_btn.setEnabled(True)
        self.delacc_btn.setGeometry(QtCore.QRect(220, 20, 91, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.delacc_btn.setFont(font)
        self.delacc_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delacc_btn.setStyleSheet("QPushButton {border-radius: 20px; color: white; background-color: rgb(255, 85, 127);}\n"
"\n"
"QPushButton:hover {border-radius: 20px; border: 1px solid #FF557F; color: rgb(255, 85, 127); background-color: white; }\n"
"")
        self.delacc_btn.setObjectName("delacc_btn")
        self.exit_btn = QtWidgets.QPushButton(self.delete_acc)
        self.exit_btn.setGeometry(QtCore.QRect(320, 20, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.exit_btn.setFont(font)
        self.exit_btn.setStyleSheet("QPushButton {background-color: rgb(21, 21, 21); border-radius: 20px; color: white;}\n"
"\n"
"QPushButton:hover {border-radius: 20px; color: white; background-color: rgb(85, 170, 255);}\n"
"")
        self.exit_btn.setObjectName("exit_btn")
        self.changepass_btn = QtWidgets.QPushButton(self.main_frm)
        self.changepass_btn.setGeometry(QtCore.QRect(777, 372, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Display")
        font.setPointSize(15)
        self.changepass_btn.setFont(font)
        self.changepass_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.changepass_btn.setStyleSheet("QPushButton {background-color: rgb(21, 21, 21); border-radius: 30px; color: white;}\n"
"\n"
"QPushButton:hover {border-radius: 30px; color: white; background-color: rgb(85, 170, 255);}\n"
"")
        self.changepass_btn.setObjectName("changepass_btn")
        self.frm_todo_3.raise_()
        self.frm_nav.raise_()
        self.frm_todo.raise_()
        self.changeusername_btn.raise_()
        self.lb_greetings.raise_()
        self.home_frame.raise_()
        self.todo_frame.raise_()
        self.opt_frame.raise_()
        self.username.raise_()
        self.SUTEXT_3.raise_()
        self.SUTEXT_2.raise_()
        self.confirm_username.raise_()
        self.tags_todolist.raise_()
        self.confirm_password.raise_()
        self.SUTEXT_6.raise_()
        self.password.raise_()
        self.SUTEXT_7.raise_()
        self.tags_todolist_3.raise_()
        self.delete_acc.raise_()
        self.changepass_btn.raise_()

        self.retranslateUi(options)
        QtCore.QMetaObject.connectSlotsByName(options)

    def retranslateUi(self, options):
        _translate = QtCore.QCoreApplication.translate
        options.setWindowTitle(_translate("options", "Dialog"))
        self.changeusername_btn.setText(_translate("options", "Confirm"))
        self.lb_greetings.setText(_translate("options", "What to-do?"))
        self.mainpagetext_53.setText(_translate("options", "HOME"))
        self.mainpagetext_52.setText(_translate("options", "TO-DO"))
        self.mainpagetext_61.setText(_translate("options", "OPT"))
        self.username.setPlaceholderText(_translate("options", "Type your new username:"))
        self.SUTEXT_3.setHtml(_translate("options", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Dubai\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:16pt; color:#a9a8a7;\">Confirm:</span></p></body></html>"))
        self.SUTEXT_2.setHtml(_translate("options", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Dubai\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:16pt; color:#a9a8a7;\">Username:</span></p></body></html>"))
        self.confirm_username.setPlaceholderText(_translate("options", "Confirm your username:"))
        self.tags_todolist.setText(_translate("options", "Change Username"))
        self.confirm_password.setPlaceholderText(_translate("options", "Confirm your password:"))
        self.SUTEXT_6.setHtml(_translate("options", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Dubai\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:16pt; color:#a9a8a7;\">Confirm:</span></p></body></html>"))
        self.password.setPlaceholderText(_translate("options", "Type your new password:"))
        self.SUTEXT_7.setHtml(_translate("options", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Dubai\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:16pt; color:#a9a8a7;\">Password:</span></p></body></html>"))
        self.tags_todolist_3.setText(_translate("options", "Change Password"))
        self.tags_todolist_4.setText(_translate("options", "Delete Account"))
        self.SUTEXT_8.setHtml(_translate("options", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Dubai\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Segoe UI\'; font-size:16pt; color:#ffffff;\">Confirm (Type &quot;yes&quot;):</span></p></body></html>"))
        self.lineEdit_7.setPlaceholderText(_translate("options", "Type \"yes\" or \"YES\":"))
        self.delacc_btn.setText(_translate("options", "Proceed"))
        self.exit_btn.setText(_translate("options", "Fin"))
        self.changepass_btn.setText(_translate("options", "Confirm"))
