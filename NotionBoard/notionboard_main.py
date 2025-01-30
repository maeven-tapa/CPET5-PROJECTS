import sys
import re
import requests
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTreeWidgetItem

teachers = {}
students = {}

class NotionBoard(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('landingpage.ui', self)  # Load the .ui file

        self.start.clicked.connect(self.startUp)

    def startUp(self):
        self.close()
        dialog = StartUp(self)  
        dialog.exec_() 





class StartUp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('startup.ui', self)

        self.lib.clicked.connect(self.login_btn)
        self.sub.clicked.connect(self.signup_btn)
        self.abb.clicked.connect(self.about_btn)

    def login_btn(self):
        self.close()
        dialog = login(self)  
        dialog.exec_() 

    def signup_btn(self):
        self.close()
        dialog = signup(self)  
        dialog.exec_() 

    def about_btn(self):
        self.close()
        dialog = aboutpage(self)  
        dialog.exec_() 

class aboutpage(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('about.ui', self)

        self.pushButton_3.clicked.connect(self.back_btn)

    def back_btn(self):
        self.close()
        dialog = StartUp(self)  
        dialog.exec_() 





class login(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('login.ui', self)

        self.pushButton_4.clicked.connect(self.back_btn)
        self.logteach_btn.clicked.connect(self.login_teacher_btn)
        self.logstud_btn.clicked.connect(self.login_student_btn)

    def back_btn(self):
        self.close()
        dialog = StartUp(self)  
        dialog.exec_() 

    def login_teacher_btn(self):
        self.close()
        dialog = login_teacher(self)  
        dialog.exec_() 

    def login_student_btn(self):
        self.close()
        dialog = login_student(self)  
        dialog.exec_() 

class login_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('login_teacher.ui', self)

        self.pushButton_11.clicked.connect(self.back_btn)
        self.pushButton_10.clicked.connect(self.loginteacher_btn)

    def back_btn(self):
        self.close()
        dialog = login(self)  
        dialog.exec_()

    def loginteacher_btn(self):
        self.close()
        dialog = home_teacher(self)  
        dialog.exec_()

class login_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('login_student.ui', self)

        self.pushButton_11.clicked.connect(self.back_btn)
        self.pushButton_10.clicked.connect(self.loginstudent_btn)

    def back_btn(self):
        self.close()
        dialog = login(self)  
        dialog.exec_()

    def loginstudent_btn(self):
        self.close()
        dialog = home_student(self)  
        dialog.exec_()






class signup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('signup.ui', self)

        self.pushButton_4.clicked.connect(self.back_btn)
        self.logteach_btn.clicked.connect(self.signup_teacher_btn)
        self.logstud_btn.clicked.connect(self.signup_student_btn)

    def back_btn(self):
        self.close()
        dialog = StartUp(self)  
        dialog.exec_() 

    def signup_teacher_btn(self):
        self.close()
        dialog = signup_teacher(self)  
        dialog.exec_() 

    def signup_student_btn(self):
        self.close()
        dialog = signup_student(self)  
        dialog.exec_() 


class signup_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('signup_teacher.ui', self)

        self.pushButton_6.clicked.connect(self.back_btn)
        self.pushButton_4.clicked.connect(self.signup_btn)

    def back_btn(self):
        self.close()
        dialog = signup(self)  
        dialog.exec_() 

    def signup_btn(self):
        self.close()
        dialog = StartUp(self)  
        dialog.exec_() 



class signup_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('signup_stud.ui', self)

        self.pushButton_6.clicked.connect(self.back_btn)
        self.pushButton_4.clicked.connect(self.signup_btn)

    def back_btn(self):
        self.close()
        dialog = signup(self)  
        dialog.exec_() 

    def signup_btn(self):
        self.close()
        dialog = StartUp(self)  
        dialog.exec_() 





class home_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('home.ui', self)

        self.todo_btn.clicked.connect(self.todolist_teacher_btn)
        self.opt_btn.clicked.connect(self.options_btn)
        self.editinfo_btn.clicked.connect(self.editinfopop_btn)
        self.addpost_btn.clicked.connect(self.postpop_btn)
        self.removepost_btn.clicked.connect(self.repost_btn)
        self.notifypost_btn.clicked.connect(self.notify_btn)
        self.tup_btn.clicked.connect(self.tup_page_btn)

    def todolist_teacher_btn(self):
        self.close()
        dialog = todolist_teacher(self)  
        dialog.exec_() 

    def options_btn(self):
        self.close()
        dialog = options_teacher(self)  
        dialog.exec_() 

    def editinfopop_btn(self):
        self.close()
        dialog = editinfopop_teacher(self)  
        dialog.exec_() 

    def postpop_btn(self):
        self.close()
        dialog = postpop_teacher(self)  
        dialog.exec_() 

    def repost_btn(self):
        pass

    def notify_btn(self):
        pass

    def tup_page_btn(self):
        pass

class home_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('home.ui', self)

        self.todo_btn.clicked.connect(self.todolist_student_btn)
        self.opt_btn.clicked.connect(self.options_btn)
        self.editinfo_btn.clicked.connect(self.editinfopop_btn)
        self.addpost_btn.clicked.connect(self.postpop_btn)
        self.removepost_btn.clicked.connect(self.repost_btn)
        self.notifypost_btn.clicked.connect(self.notify_btn)
        self.tup_btn.clicked.connect(self.tup_page_btn)

    def todolist_student_btn(self):
        self.close()
        dialog = todolist_student(self)  
        dialog.exec_() 

    def options_btn(self):
        self.close()
        dialog = options_student(self)  
        dialog.exec_() 

    def editinfopop_btn(self):
        self.close()
        dialog = editinfopop_student(self)  
        dialog.exec_() 

    def postpop_btn(self):
        self.close()
        dialog = postpop_student(self)  
        dialog.exec_() 

    def repost_btn(self):
        pass

    def notify_btn(self):
        pass

    def tup_page_btn(self):
        pass


class editinfopop_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('editinfopop.ui', self)

        self.editback_btn.clicked.connect(self.back_btn)
        self.edit_btn.clicked.connect(self.edit1_btn)

    def back_btn(self):
        self.close()
        dialog = home_teacher(self)  
        dialog.exec_()

    def edit1_btn(self):
        pass

class postpop_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('postpop.ui', self)

        self.postback_btn.clicked.connect(self.back_btn)
        self.addpost_btn.clicked.connect(self.addpost1_btn)

    def back_btn(self):
        self.close()
        dialog = home_teacher(self)  
        dialog.exec_() 

    def addpost1_btn(self):
        pass

class editinfopop_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('editinfopop.ui', self)

        self.editback_btn.clicked.connect(self.back_btn)
        self.edit_btn.clicked.connect(self.edi1t_btn)

    def back_btn(self):
        self.close()
        dialog = home_student(self)  
        dialog.exec_()

    def edit1_btn(self):
        pass


class postpop_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('postpop.ui', self)

        self.postback_btn.clicked.connect(self.back_btn)
        self.addpost_btn.clicked.connect(self.addpost1_btn)

    def back_btn(self):
        self.close()
        dialog = home_student(self)  
        dialog.exec_() 

    def addpost1_btn(self):
        pass











class todolist_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('todolist_teacher.ui', self)

        self.home_btn.clicked.connect(self.home_teacher_btn)
        self.opt_btn.clicked.connect(self.options_btn)
        self.addstud_btn.clicked.connect(self.addstudpop_btn)
        self.addtodo_btn.clicked.connect(self.addtodo1_btn)
        self.editstud_btn.clicked.connect(self.editstud1_btn)
        self.edittodo_btn.clicked.connect(self.edittodo1_btn)
        self.removestud_btn.clicked.connect(self.restud_btn)
        self.removetodo_btn.clicked.connect(self.retodo_btn)

    def home_teacher_btn(self):
        self.close()
        dialog = home_teacher(self)  
        dialog.exec_() 

    def options_btn(self):
        self.close()
        dialog = options_teacher(self)  
        dialog.exec_()

    def addstudpop_btn(self):
        self.close()
        dialog = addstudpop(self)  
        dialog.exec_()

    def addtodo1_btn(self):
        self.close()
        dialog = todopop_teacher(self)  
        dialog.exec_()

    def editstud1_btn(self):
        self.close()
        dialog = editstud(self)  
        dialog.exec_()

    def edittodo1_btn(self):
        self.close()
        dialog = edittodo_teacher(self)  
        dialog.exec_()

    def retodo_btn(self):
        pass

    def restud_btn(self):
        pass

class todolist_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('todolist_student.ui', self)

        self.home_btn.clicked.connect(self.home_student_btn)
        self.opt_btn.clicked.connect(self.options_btn)
        self.stud_addtodo_btn.clicked.connect(self.addtodo_btn)
        self.edittodo_btn.clicked.connect(self.edittodo1_btn)
        self.removetodo_btn.clicked.connect(self.retodo_btn)

    def home_student_btn(self):
        self.close()
        dialog = home_student(self)  
        dialog.exec_() 

    def options_btn(self):
        self.close()
        dialog = options_student(self)  
        dialog.exec_()

    def addtodo_btn(self):
        self.close()
        dialog = todopop_student(self)  
        dialog.exec_()

    def edittodo1_btn(self):
        self.close()
        dialog = edittodo_student(self)  
        dialog.exec_()

    def retodo_btn(self):
        pass

class addstudpop(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('addstudpop.ui', self)

        self.addstudback_btn.clicked.connect(self.back_btn)
        self.addstud_btn.clicked.connect(self.addstud1_btn)

    def back_btn(self):
        self.close()
        dialog = todolist_teacher(self)  
        dialog.exec_()

    def addstud1_btn(self):
        pass

class editstud(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('edit_addstudpop.ui', self)

        self.addstudback_btn.clicked.connect(self.back_btn)
        self.addstud_btn.clicked.connect(self.addstud1_btn)

    def back_btn(self):
        self.close()
        dialog = todolist_teacher(self)  
        dialog.exec_()

    def addstud1_btn(self):
        pass

class todopop_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('todopop.ui', self)

        self.todoback_btn.clicked.connect(self.back_btn)
        self.addtodo_btn.clicked.connect(self.addtodo1_btn)

    def back_btn(self):
        self.close()
        dialog = todolist_teacher(self)  
        dialog.exec_()

    def addtodo1_btn(self):
        pass

class todopop_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('todopop.ui', self)

        self.todoback_btn.clicked.connect(self.back_btn)
        self.addtodo_btn.clicked.connect(self.addtodo1_btn)

    def back_btn(self):
        self.close()
        dialog = todolist_student(self)  
        dialog.exec_()

    def addtodo1_btn(self):
        pass

class edittodo_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('edit_todopop.ui', self)

        self.todoback_btn.clicked.connect(self.back_btn)
        self.addtodo_btn.clicked.connect(self.addtodo1_btn)

    def back_btn(self):
        self.close()
        dialog = todolist_teacher(self)  
        dialog.exec_()

    def addtodo1_btn(self):
        pass

class edittodo_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('edit_todopop.ui', self)

        self.todoback_btn.clicked.connect(self.back_btn)
        self.addtodo_btn.clicked.connect(self.addtodo1_btn)

    def back_btn(self):
        self.close()
        dialog = todolist_student(self)  
        dialog.exec_()

    def addtodo1_btn(self):
        pass





class options_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('options.ui', self)

        self.home_btn.clicked.connect(self.home1_btn)
        self.todo_btn.clicked.connect(self.todo1_btn)
        self.changeusername_btn.clicked.connect(self.changeusername1_btn)
        self.changepass_btn.clicked.connect(self.changepass1_btn)
        self.delacc_btn.clicked.connect(self.delacc1_btn)
        self.exit_btn.clicked.connect(self.close_btn)

    def home1_btn(self):
        self.close()
        dialog = home_teacher(self)  
        dialog.exec_() 

    def todo1_btn(self):
        self.close()
        dialog = todolist_teacher(self)  
        dialog.exec_()

    def changeusername1_btn(self):
        pass

    def changepass1_btn(self):
        pass

    def delacc1_btn(self):
        pass

    def close_btn(self):
        pass

class options_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('options.ui', self)

        self.home_btn.clicked.connect(self.home1_btn)
        self.todo_btn.clicked.connect(self.todo1_btn)
        self.changeusername_btn.clicked.connect(self.changeusername1_btn)
        self.changepass_btn.clicked.connect(self.changepass1_btn)
        self.delacc_btn.clicked.connect(self.delacc1_btn)
        self.exit_btn.clicked.connect(self.close_btn)

    def home1_btn(self):
        self.close()
        dialog = home_student(self)  
        dialog.exec_() 

    def todo1_btn(self):
        self.close()
        dialog = todolist_student(self)  
        dialog.exec_()

    def changeusername1_btn(self):
        pass

    def changepass1_btn(self):
        pass

    def delacc1_btn(self):
        pass

    def close_btn(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = NotionBoard()  # Initialize the Home class
    win.show()
    sys.exit(app.exec())
