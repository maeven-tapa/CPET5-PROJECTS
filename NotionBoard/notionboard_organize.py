import sys
import re
import requests
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTreeWidgetItem
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

teachers = {}
students = {}

class NotionBoard(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('Landingpage.ui', self)  # Load the .ui file

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















#Teacher

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

    def validate_name(self, name):
        pattern = r'^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$'
        return re.match(pattern, name) is not None

    def validate_birthday(self, birthday):
        try:
            datetime.strptime(birthday, '%B %d, %Y')
            return True
        except ValueError:
            return False

    def validate_gender(self, gender):
        return gender in ['Male', 'Female']

    def validate_username(self, username):
        return len(username) >= 5

    def validate_password(self, password):
        return len(password) >= 6

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    def signup_btn(self):
        name = self.ssn1.text()
        birthday = self.ssb1.text()
        gender = self.ssg1.text()
        username = self.stu1.text()
        password = self.ssp1.text()
        email = self.ssg1_2.text()
        
        if not self.validate_name(name):
            QMessageBox.warning(self, "Error", "Name must be in the format 'Firstname M. Lastname'.")
            return

        if not self.validate_birthday(birthday):
            QMessageBox.warning(self, "Error", "Birthday must be in the format 'Month DD, YYYY'.")
            return

        if not self.validate_gender(gender):
            QMessageBox.warning(self, "Error", "Gender must be 'Male' or 'Female'.")
            return

        if not self.validate_username(username):
            QMessageBox.warning(self, "Error", "Username must be at least 5 characters.")
            return

        if not self.validate_password(password):
            QMessageBox.warning(self, "Error", "Password must be at least 6 characters.")
            return

        if not self.validate_email(email):
            QMessageBox.warning(self, "Error", "Invalid email address.")
            return

        teachers[username] = {
            'name': name,
            'birthday': birthday,
            'gender': gender,
            'password': password,
            'email': email,
            'usertype': 'teacher'  # Adding usertype as teacher
        }
        QMessageBox.information(self, "Success", "Teacher signed up successfully!")

        self.close()
        dialog = StartUp(self)  
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
        username = self.ltu1.text()
        password = self.ltp1.text()

        if username in teachers and teachers[username]['password'] == password:
            QMessageBox.information(self, "Success", "Logged in successfully!")
            self.close()
            dialog = home_teacher(self)  
            dialog.exec_() 
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials.")


class home_teacher(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        uic.loadUi('home.ui', self)

        self.username = username
        self.update_labels()

        self.todo_btn.clicked.connect(self.todolist_teacher_btn)
        self.opt_btn.clicked.connect(self.options_btn)
        self.editinfo_btn.clicked.connect(self.editinfopop_btn)
        self.addpost_btn.clicked.connect(self.postpop_btn)
        self.removepost_btn.clicked.connect(self.repost_btn)
        self.notifypost_btn.clicked.connect(self.notify_btn)
        self.tup_btn.clicked.connect(self.tup_page_btn)

    def update_labels(self):
        print("Teachers Dictionary:", teachers) 
        user_info = teachers.get(self.username)
        if not user_info:
            return
        
        name = user_info['name']
        birthday = datetime.strptime(user_info['birthday'], '%B %d, %Y')
        gender = user_info['gender']
        usertype = user_info['usertype']
        today = datetime.today()

        # Update lb_greetings
        current_hour = datetime.now().hour
        if current_hour < 12:
            greeting = "Good Morning"
        elif current_hour < 18:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"
        self.lb_greetings.setText(f"{greeting}, {name.split(' ')[0]}")  # Using first name for greeting

        # Update lb_name
        self.lb_name.setText(name)

        # Update lb_gender
        self.lb_gender.setText(f"{gender} | {usertype}")

        # Update lb_age
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        self.lb_age.setText(f"{birthday.strftime('%B %d, %Y')} | {age} years old")

        # Update lb_date
        self.lb_date.setText(today.strftime('%B %d, %Y'))

        # Update lb_day
        part_of_day = "Morning" if current_hour < 12 else "Afternoon" if current_hour < 18 else "Evening"
        self.lb_day.setText(f"{today.strftime('%A')}, {part_of_day}")

    def todolist_teacher_btn(self):
        self.close()
        dialog = todolist_teacher(self, self.username)  
        dialog.exec_() 

    def options_btn(self):
        self.close()
        dialog = options_teacher(self, self.username)  
        dialog.exec_() 

    def editinfopop_btn(self):
        self.close()
        dialog = editinfopop_teacher(self, self.username)  
        dialog.exec_() 

    def postpop_btn(self):
        self.close()
        dialog = postpop_teacher(self, self.username)  
        dialog.exec_() 

    def repost_btn(self):
        selected_item = self.post_table.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Error", "Please select a post to repost.")
            return

        index = self.post_table.indexOfTopLevelItem(selected_item)
        self.post_table.takeTopLevelItem(index)

    def notify_btn(self):
        pass

    def tup_page_btn(self):
        url = QUrl("https://www.tup.edu.ph/")
        QDesktopServices.openUrl(url)


class editinfopop_teacher(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        uic.loadUi('editinfopop.ui', self)

        self.username = username
        self.populate_fields()

        self.editback_btn.clicked.connect(self.back_btn)
        self.edit_btn.clicked.connect(self.edit1_btn)

    def populate_fields(self):
        user_info = teachers.get(self.username)
        if not user_info:
            return
        
        self.nameedit.setText(user_info['name'])
        self.birthdayedit.setText(user_info['birthday'])
        self.genderedit.setText(user_info['gender'])

    def back_btn(self):
        self.close()
        dialog = home_teacher(self, self.username)  
        dialog.exec_()

    def validate_name(self, name):
        pattern = r'^[A-Za-z]+ [A-Za-z]\. [A-Za-z]+$'
        return re.match(pattern, name) is not None

    def validate_birthday(self, birthday):
        try:
            datetime.strptime(birthday, '%B %d, %Y')
            return True
        except ValueError:
            return False

    def validate_gender(self, gender):
        return gender in ['Male', 'Female']

    def edit1_btn(self):
        name = self.nameedit.text()
        birthday = self.birthdayedit.text()
        gender = self.genderedit.text()

        if not self.validate_name(name):
            QMessageBox.warning(self, "Error", "Name must be in the format 'Firstname M. Lastname'.")
            return

        if not self.validate_birthday(birthday):
            QMessageBox.warning(self, "Error", "Birthday must be in the format 'Month DD, YYYY'.")
            return

        if not self.validate_gender(gender):
            QMessageBox.warning(self, "Error", "Gender must be 'Male' or 'Female'.")
            return

        teachers[self.username]['name'] = name
        teachers[self.username]['birthday'] = birthday
        teachers[self.username]['gender'] = gender

        QMessageBox.information(self, "Success", "Information updated successfully!")
        self.close()
        dialog = home_teacher(self, self.username)  
        dialog.exec_()


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

    def validate_deadline(self, deadline):
        try:
            datetime.strptime(deadline, '%B %d, %Y')
            return True
        except ValueError:
            return False

    def addpost1_btn(self):
        post = self.ps1.text()
        deadline = self.dl1.text()

        if not post:
            QMessageBox.warning(self, "Error", "Please enter a post.")
            return

        if not self.validate_deadline(deadline):
            QMessageBox.warning(self, "Error", "Deadline must be in the format 'Month DD, YYYY'.")
            return

        # Add the post to the post_table
        item = QTreeWidgetItem([f"Deadline: {deadline}", f"Post: {post}"])
        self.parent().post_table.addTopLevelItem(item)

        QMessageBox.information(self, "Success", "Post added successfully!")
        self.close()

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








#Students

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






# Initialize the Home class
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = NotionBoard()  # Initialize the Home class
    win.show()
    sys.exit(app.exec())

