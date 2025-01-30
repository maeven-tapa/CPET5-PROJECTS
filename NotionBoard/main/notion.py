import re
import os
import sys
import json
import socket
import smtplib
import requests
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QDesktopServices, QIcon
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTreeWidgetItem, QTableWidgetItem
from about import Ui_about; from addstudpop import Ui_addstudpop; from edit_addstudpop import Ui_edit_addstudpop
from edit_todopop import Ui_edit_todopop; from editinfopop import Ui_editinfopop; from home import Ui_home; from landingpage import Ui_landingpage
from login_student import Ui_login_student; from login_teacher import Ui_login_teacher; from login import Ui_login; from options import Ui_options; 
from signup_stud import Ui_signup_stud; from signup_teacher import Ui_signup_teacher; from signup import Ui_signup; 
from startup import Ui_startup; from todolist_student import Ui_todolist_student
from todolist_teacher import Ui_todolist_teacher; from postpop import Ui_postpop
from todopop import Ui_todopop


import sqlite3

teachers = {}
students = {}

# Database setup
def init_db():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        username TEXT PRIMARY KEY,
        name TEXT,
        birthday TEXT,
        gender TEXT,
        password TEXT,
        email TEXT,
        usertype TEXT
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birthday TEXT NOT NULL,
        email TEXT NOT NULL,
        teacher_username TEXT,
        FOREIGN KEY(teacher_username) REFERENCES teachers(username)
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        progress TEXT NOT NULL,
        tags TEXT NOT NULL,
        teacher_username TEXT,
        FOREIGN KEY(teacher_username) REFERENCES teachers(username)
    )''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        post TEXT,
        deadline TEXT,
        FOREIGN KEY(username) REFERENCES teachers(username)
    )''')
    conn.commit()
    conn.close()

init_db()

def execute_query(query, params=()):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()

def fetch_query(query, params=()):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows


class NotionBoard(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_landingpage()  
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.setWindowIcon(QIcon('nb_logo.png'))
        self.ui.start.clicked.connect(self.startUp)

    def startUp(self):
        self.close()
        dialog = StartUp(self)  
        dialog.exec_()

class StartUp(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_startup()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.ui.lib.clicked.connect(self.login_btn)
        self.ui.sub.clicked.connect(self.signup_btn)
        self.ui.abb.clicked.connect(self.about_btn)

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
        self.ui = Ui_about()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.ui.pushButton_3.clicked.connect(self.back_btn)

    def back_btn(self):
        self.close()
        dialog = StartUp(self)  
        dialog.exec_() 

class signup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_signup()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.ui.pushButton_4.clicked.connect(self.back_btn)
        self.ui.logteach_btn.clicked.connect(self.signup_teacher_btn)
        self.ui.logstud_btn.clicked.connect(self.signup_student_btn)

    def back_btn(self):
        self.close()
        dialog = StartUp(self)  
        dialog.exec_() 

    def signup_teacher_btn(self):
        self.close()
        dialog = signup_teacher(self)  
        dialog.exec_() 

    def signup_student_btn(self):
        pass

class login(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_login()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.ui.pushButton_4.clicked.connect(self.back_btn)
        self.ui.logteach_btn.clicked.connect(self.login_teacher_btn)
        self.ui.logstud_btn.clicked.connect(self.login_student_btn)

    def back_btn(self):
        self.close()
        dialog = StartUp(self)  
        dialog.exec_() 

    def login_teacher_btn(self):
        self.close()
        dialog = login_teacher(self)  
        dialog.exec_() 

    def login_student_btn(self):
        pass

class signup_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_signup_teacher()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.ui.pushButton_6.clicked.connect(self.back_btn)
        self.ui.pushButton_4.clicked.connect(self.signup_btn)

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
        name = self.ui.ssn1.text()
        birthday = self.ui.ssb1.text()
        gender = self.ui.ssg1.text()
        username = self.ui.stu1.text()
        password = self.ui.ssp1.text()
        email = self.ui.ssg1_2.text()
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
        execute_query('''
            INSERT INTO teachers (username, name, birthday, gender, password, email, usertype)
            VALUES (?, ?, ?, ?, ?, ?, 'teacher')
        ''', (username, name, birthday, gender, password, email))
        QMessageBox.information(self, "Success", "Teacher signed up successfully!")
        self.close()
        dialog = StartUp(self)  
        dialog.exec_()

class login_teacher(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_login_teacher()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.ui.pushButton_11.clicked.connect(self.back_btn)
        self.ui.pushButton_10.clicked.connect(self.loginteacher_btn)

    def back_btn(self):
        self.close()
        dialog = login(self)  
        dialog.exec_()

    def loginteacher_btn(self):
        username = self.ui.ltu1.text()
        password = self.ui.ltp1.text()
        rows = fetch_query('SELECT * FROM teachers WHERE username = ? AND password = ?', (username, password))
        if rows:
            QMessageBox.information(self, "Success", "Logged in successfully!")
            self.close()
            dialog = home_teacher(self, username=username)  
            dialog.exec_() 
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials.")

class home_teacher(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_home() 
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.update_labels()
        self.populate_post_table()
        self.get_weather()
        self.ui.todo_btn.clicked.connect(self.todolist_teacher_btn)
        self.ui.opt_btn.clicked.connect(self.options_btn)
        self.ui.editinfo_btn.clicked.connect(self.editinfopop_btn)
        self.ui.addpost_btn.clicked.connect(self.postpop_btn)
        self.ui.removepost_btn.clicked.connect(self.repost_btn)
        self.ui.notifypost_btn.clicked.connect(self.notify_btn)
        self.ui.tup_btn.clicked.connect(self.tup_page_btn)

    def update_labels(self):
        user_info = fetch_query('SELECT * FROM teachers WHERE username = ?', (self.username,))
        if not user_info:
            return
        user_info = user_info[0]
        name, birthday_str, gender, usertype = user_info[1], user_info[2], user_info[3], user_info[6]
        try:
            birthday = datetime.strptime(birthday_str, '%B %d, %Y')
        except ValueError:
            return
        today = datetime.today()
        current_hour = datetime.now().hour
        greeting = "Hi" if current_hour < 12 else "Wazzup" if current_hour < 18 else "Hi"
        self.ui.lbgreetings.setText(f"{greeting}, {name.split(' ')[0]}")
        self.ui.lbname.setText(name)
        self.ui.lbgender.setText(f"{gender} | {usertype}")
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        self.ui.lbage.setText(f"{birthday.strftime('%B %d, %Y')} | {age} years old")
        self.ui.lbdate.setText(today.strftime('%B %d, %Y'))
        part_of_day = "Morning" if current_hour < 12 else "Afternoon" if current_hour < 18 else "Evening"
        self.ui.lbday.setText(f"{today.strftime('%A')}, {part_of_day}")

    def get_weather(self):
        try:
            api_key = "a77f2ef1d95f695092242042a413088b"
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            city = "Dasmariñas,PH" 
            complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"  
            response = requests.get(complete_url)
            data = response.json()
            temperature = int(data['main']['temp'])
            self.ui.lbweather.setText(f"{temperature}°C")
        except Exception as e:
            print("Error fetching weather:", e)
            self.ui.lbweather.setText("N/A")

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

    def populate_post_table(self):
        self.ui.post_table.clear()
        self.ui.post_table.setHeaderLabels(["Post:", "Deadline"])
        posts = fetch_query('SELECT post, deadline FROM posts WHERE username = ?', (self.username,))
        for post in posts:
            item = QTreeWidgetItem([post[0], post[1]])
            item.setTextAlignment(0, Qt.AlignHCenter)
            item.setTextAlignment(1, Qt.AlignHCenter)
            self.ui.post_table.addTopLevelItem(item)

    def postpop_btn(self):
        self.dialog = postpop_teacher(self, self.username)
        self.dialog.exec_()
        self.populate_post_table()

    def repost_btn(self):
        selected_item = self.ui.post_table.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Error", "Please select a post to remove.")
            return
        index = self.ui.post_table.indexOfTopLevelItem(selected_item)
        self.ui.post_table.takeTopLevelItem(index)
        post = selected_item.text(0)
        deadline = selected_item.text(1)
        execute_query('DELETE FROM posts WHERE username = ? AND post = ? AND deadline = ?', (self.username, post, deadline))

    def notify_students(self, subject, message):
        teacher_data = fetch_query('SELECT email FROM students')
        if not teacher_data:
            QMessageBox.warning(self, "Error", "No students found.")
            return
        sender_email = 'notionboard.tupcavite@gmail.com'  
        password = 'fceq jsie lmdk uazf'  
        for student in teacher_data:
            receiver_email = student[0]
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            try:
                socket.create_connection(("www.google.com", 80))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                text = msg.as_string()
                server.sendmail(sender_email, receiver_email, text)
                server.quit()
                print(f"Notification sent to {receiver_email}")
            except Exception as e:
                print(f"Failed to send notification to {receiver_email}: {e}")
                raise RuntimeError("No internet connection.")

    def notify_btn(self):
        subject = "New Post Notification"
        posts = fetch_query('SELECT post, deadline FROM posts WHERE username = ?', (self.username,))
        teacher_data = fetch_query('SELECT name, students.email FROM teachers LEFT JOIN students ON students.username = teachers.username WHERE teachers.username = ?', (self.username,))
        if not teacher_data or not posts:
            QMessageBox.warning(self, "Error", "No students or posts found.")
            return
        teacher_name = teacher_data[0][0]
        for student in teacher_data:
            receiver_email = student[1]
            message = f"Dear {student[0]},\n\nThe following posts are available:\n\n"
            for post in posts:
                message += f"Post: {post[0]}, Deadline: {post[1]}\n"
            try:
                self.notify_students(subject, message)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to send notification to {receiver_email}: {str(e)}")

    def tup_page_btn(self):
        url = QUrl("https://www.tup.edu.ph/")
        QDesktopServices.openUrl(url)

class editinfopop_teacher(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_editinfopop()  
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.populate_fields()
        self.ui.editback_btn.clicked.connect(self.back_btn)
        self.ui.edit_btn.clicked.connect(self.edit1_btn)

    def populate_fields(self):
        user_info = fetch_query('SELECT * FROM teachers WHERE username = ?', (self.username,))
        if not user_info:
            return
        user_info = user_info[0]
        self.ui.nameedit.setText(user_info[1])
        self.ui.birthdayedit.setText(user_info[2])
        self.ui.genderedit.setText(user_info[3])

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
        name = self.ui.nameedit.text()
        birthday = self.ui.birthdayedit.text()
        gender = self.ui.genderedit.text()
        if not self.validate_name(name):
            QMessageBox.warning(self, "Error", "Name must be in the format 'Firstname M. Lastname'.")
            return
        if not self.validate_birthday(birthday):
            QMessageBox.warning(self, "Error", "Birthday must be in the format 'Month DD, YYYY'.")
            return
        if not self.validate_gender(gender):
            QMessageBox.warning(self, "Error", "Gender must be 'Male' or 'Female'.")
            return
        execute_query('''
            UPDATE teachers SET name = ?, birthday = ?, gender = ? WHERE username = ?
        ''', (name, birthday, gender, self.username))
        QMessageBox.information(self, "Success", "Information updated successfully!")
        self.close()
        dialog = home_teacher(self, self.username)
        dialog.exec_()

class postpop_teacher(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_postpop()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.ui.postback_btn.clicked.connect(self.back_btn)
        self.ui.addpost_btn.clicked.connect(self.addpost1_btn)

    def back_btn(self):
        self.close()

    def validate_deadline(self, deadline):
        try:
            datetime.strptime(deadline, '%B %d, %Y')
            return True
        except ValueError:
            return False

    def addpost1_btn(self):
        post = self.ui.ps1.text()
        deadline = self.ui.dl1.text()
        if not post:
            QMessageBox.warning(self, "Error", "Please enter a post.")
            return
        if not self.validate_deadline(deadline):
            QMessageBox.warning(self, "Error", "Deadline must be in the format 'Month DD, YYYY'.")
            return
        execute_query('INSERT INTO posts (username, post, deadline) VALUES (?, ?, ?)', (self.username, post, deadline))
        QMessageBox.information(self, "Success", "Post added successfully!")
        self.close()


class todolist_teacher(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_todolist_teacher()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.populate_todo_tree()
        self.populate_stud_tree()
        self.ui.home_btn.clicked.connect(self.home_teacher_btn)
        self.ui.opt_btn.clicked.connect(self.options_btn)
        self.ui.addstud_btn.clicked.connect(self.addstudpop_btn)
        self.ui.addtodo_btn.clicked.connect(self.addtodo1_btn)
        self.ui.editstud_btn.clicked.connect(self.editstud1_btn)
        self.ui.edittodo_btn.clicked.connect(self.edittodo1_btn)
        self.ui.removestud_btn.clicked.connect(self.restud_btn)
        self.ui.removetodo_btn.clicked.connect(self.retodo_btn)
        self.ui.notifyme__btn.clicked.connect(self.notify_btn)

    def populate_todo_tree(self):
        self.ui.teachtodo_table.clear()
        todos = fetch_query('SELECT task, progress, tags FROM todos WHERE teacher_username = ?', (self.username,))
        for todo in todos:
            todo_item = QTreeWidgetItem([todo[2], todo[0], todo[1]])
            for i in range(3):
                todo_item.setTextAlignment(i, Qt.AlignHCenter)
            self.ui.teachtodo_table.addTopLevelItem(todo_item)

    def populate_stud_tree(self):
        self.ui.teachstudlist_table.clear()
        students = fetch_query('SELECT name, birthday, email FROM students WHERE teacher_username = ?', (self.username,))
        for student in students:
            age = self.calculate_age(student[1])
            stud_item = QTreeWidgetItem([student[0], str(age), student[2]])
            for i in range(3):
                stud_item.setTextAlignment(i, Qt.AlignHCenter)
            self.ui.teachstudlist_table.addTopLevelItem(stud_item)

    def calculate_age(self, birthday_str):
        try:
            birthday = datetime.strptime(birthday_str, '%B %d, %Y')
            today = datetime.today()
            return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        except ValueError:
            return 'Unknown'

    def home_teacher_btn(self):
        self.close()
        dialog = home_teacher(self, self.username)
        dialog.exec_()

    def options_btn(self):
        self.close()
        dialog = options_teacher(self, self.username)
        dialog.exec_()

    def addstudpop_btn(self):
        self.close()
        dialog = addstudpop(self, self.username)
        dialog.exec_()

    def addtodo1_btn(self):
        self.close()
        dialog = todopop_teacher(self, self.username)
        dialog.exec_()

    def editstud1_btn(self):
        self.close()
        dialog = editstud(self, self.username)
        dialog.exec_()

    def edittodo1_btn(self):
        self.close()
        dialog = edittodo_teacher(self, self.username)
        dialog.exec_()

    def notify_students(self, subject, message):
        students = fetch_query('SELECT email FROM students WHERE teacher_username = ?', (self.username,))
        if not students:
            QMessageBox.warning(self, "Warning", "No students found.")
            return
        sender_email = 'notionboard.tupcavite@gmail.com'
        password = 'fceq jsie lmdk uazf'
        for student in students:
            receiver_email = student[0]
            if not receiver_email:
                continue
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                text = msg.as_string()
                server.sendmail(sender_email, receiver_email, text)
                server.quit()
                print(f"Notification sent to {receiver_email}")
            except Exception as e:
                print(f"Failed to send notification to {receiver_email}: {e}")

    def notify_btn(self):
        subject = "New To-Do Notification"
        message = "Dear student,\n\nHere are your new to-do items:\n\n"
        for row in range(self.ui.teachtodo_table.topLevelItemCount()):
            item = self.ui.teachtodo_table.topLevelItem(row)
            task = item.text(1)
            progress = item.text(2)
            tags = item.text(0)
            message += f"Task: {task}, Progress: {progress}, Tags: {tags}\n"
        try:
            requests.get('https://www.google.com', timeout=5)
        except requests.ConnectionError:
            QMessageBox.warning(self, "Warning", "No internet connection. Please check your network settings.")
            return
        self.notify_students(subject, message)

    def restud_btn(self):
        selected_item = self.ui.teachstudlist_table.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Error", "Please select a student to remove.")
            return
        name = selected_item.text(0)
        execute_query('DELETE FROM students WHERE name = ? AND teacher_username = ?', (name, self.username))
        self.populate_stud_tree()

    def retodo_btn(self):
        selected_item = self.ui.teachtodo_table.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Error", "Please select a task to remove.")
            return
        task = selected_item.text(1)
        execute_query('DELETE FROM todos WHERE task = ? AND teacher_username = ?', (task, self.username))
        self.populate_todo_tree()

class addstudpop(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_addstudpop()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.ui.addstudback_btn.clicked.connect(self.back_btn)
        self.ui.addstud_btn.clicked.connect(self.addstud1_btn)

    def back_btn(self):
        self.close()
        dialog = todolist_teacher(self.parent(), self.username)
        dialog.exec_()

    def addstud1_btn(self):
        name = self.ui.studnameedit.text()
        birthday = self.ui.studbirthdayedit.text()
        email = self.ui.studgenderedit.text()
        if not name or not birthday or not email:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return
        try:
            datetime.strptime(birthday, '%B %d, %Y')
        except ValueError:
            QMessageBox.warning(self, "Error", "Birthday must be in the format 'Month DD, YYYY'.")
            return
        execute_query('INSERT INTO students (name, birthday, email, teacher_username) VALUES (?, ?, ?, ?)', (name, birthday, email, self.username))
        QMessageBox.information(self, "Success", "Student added successfully!")
        self.close()
        dialog = todolist_teacher(self.parent(), self.username)
        dialog.exec_()

class editstud(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_edit_addstudpop()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.populate_fields()
        self.ui.addstudback_btn.clicked.connect(self.back_btn)
        self.ui.addstud_btn.clicked.connect(self.editstud_btn)

    def populate_fields(self):
        selected_item = self.parent().ui.teachstudlist_table.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Error", "No student selected for editing.")
            self.close()
            return
        self.selected_index = self.parent().ui.teachstudlist_table.indexOfTopLevelItem(selected_item)
        students = fetch_query('SELECT name, birthday, email FROM students WHERE teacher_username = ?', (self.username,))
        if self.selected_index < 0 or self.selected_index >= len(students):
            QMessageBox.warning(self, "Error", "Invalid student selected.")
            self.close()
            return
        student = students[self.selected_index]
        self.ui.studnameedit.setText(student[0])
        self.ui.studbirthdayedit.setText(student[1])
        self.ui.studgenderedit.setText(student[2])

    def back_btn(self):
        self.close()
        dialog = todolist_teacher(self.parent(), self.username)
        dialog.exec_()

    def validate_birthday(self, birthday):
        try:
            datetime.strptime(birthday, '%B %d, %Y')
            return True
        except ValueError:
            return False

    def editstud_btn(self):
        name = self.ui.studnameedit.text()
        birthday = self.ui.studbirthdayedit.text()
        email = self.ui.studgenderedit.text()
        if not name or not birthday or not email:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return
        if not self.validate_birthday(birthday):
            QMessageBox.warning(self, "Error", "Birthday must be in the format 'Month DD, YYYY'.")
            return
        execute_query('UPDATE students SET name = ?, birthday = ?, email = ? WHERE id = ? AND teacher_username = ?', (name, birthday, email, self.selected_index, self.username))
        QMessageBox.information(self, "Success", "Student information updated successfully!")
        self.close()
        dialog = todolist_teacher(self.parent(), self.username)
        dialog.exec_()

class todopop_teacher(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_todopop()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.ui.todoback_btn.clicked.connect(self.back_btn)
        self.ui.addtodo_btn.clicked.connect(self.addtodo1_btn)

    def back_btn(self):
        self.close()
        dialog = todolist_teacher(self.parent(), self.username)
        dialog.exec_()

    def addtodo1_btn(self):
        task = self.ui.taskinput.text()
        progress = self.ui.progressinput.text()
        tags = self.ui.tagskinput.text()
        if not task or not progress or not tags:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return
        execute_query('INSERT INTO todos (task, progress, tags, teacher_username) VALUES (?, ?, ?, ?)', (task, progress, tags, self.username))
        QMessageBox.information(self, "Success", "To-do added successfully!")
        self.close()
        dialog = todolist_teacher(self.parent(), self.username)
        dialog.exec_()

class edittodo_teacher(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_edit_todopop()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.populate_fields()
        self.ui.todoback_btn.clicked.connect(self.back_btn)
        self.ui.addtodo_btn.clicked.connect(self.edittodo_btn)

    def populate_fields(self):
        selected_item = self.parent().ui.teachtodo_table.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Error", "No todo item selected for editing.")
            self.close()
            return
        self.selected_index = self.parent().ui.teachtodo_table.indexOfTopLevelItem(selected_item)
        todos = fetch_query('SELECT task, progress, tags FROM todos WHERE teacher_username = ?', (self.username,))
        if self.selected_index < 0 or self.selected_index >= len(todos):
            QMessageBox.warning(self, "Error", "Invalid todo item selected.")
            self.close()
            return
        todo = todos[self.selected_index]
        self.ui.taskinput.setText(todo[0])
        self.ui.progressinput.setText(todo[1])
        self.ui.tagskinput.setText(todo[2])

    def back_btn(self):
        self.close()
        dialog = todolist_teacher(self.parent(), self.username)
        dialog.exec_()

    def edittodo_btn(self):
        task = self.ui.taskinput.text()
        progress = self.ui.progressinput.text()
        tags = self.ui.tagskinput.text()
        if not task or not progress or not tags:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return
        execute_query('UPDATE todos SET task = ?, progress = ?, tags = ? WHERE id = ? AND teacher_username = ?', (task, progress, tags, self.selected_index, self.username))
        QMessageBox.information(self, "Success", "Todo item updated successfully!")
        self.close()
        dialog = todolist_teacher(self.parent(), self.username)
        dialog.exec_()

    
class options_teacher(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_options()  
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.ui.home_btn.clicked.connect(self.home1_btn)
        self.ui.todo_btn.clicked.connect(self.todo1_btn)
        self.ui.changeusername_btn.clicked.connect(self.changeusername1_btn)
        self.ui.changepass_btn.clicked.connect(self.changepass1_btn)
        self.ui.delacc_btn.clicked.connect(self.delacc1_btn)
        self.ui.exit_btn.clicked.connect(self.close_btn)

    def home1_btn(self):
        self.close()
        dialog = home_teacher(self, self.username)  
        dialog.exec_() 

    def todo1_btn(self):
        self.close()
        dialog = todolist_teacher(self, self.username)  
        dialog.exec_()

    def changeusername1_btn(self):
        new_username = self.ui.username.text().strip()
        confirm_username = self.ui.confirm_username.text().strip()
        if new_username != confirm_username:
            QMessageBox.warning(self, "Error", "Usernames do not match.")
            return
        if not new_username:
            QMessageBox.warning(self, "Error", "New username cannot be empty.")
            return
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE teachers SET username = ? WHERE username = ?', (new_username, self.username))
        conn.commit()
        if cursor.rowcount == 0:
            QMessageBox.warning(self, "Error", "Username change failed.")
        else:
            QMessageBox.information(self, "Success", "Username changed successfully.")
            self.username = new_username
        conn.close()

    def changepass1_btn(self):
        new_password = self.ui.password.text().strip()
        confirm_password = self.ui.confirm_password.text().strip()
        if new_password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return
        if not new_password:
            QMessageBox.warning(self, "Error", "New password cannot be empty.")
            return
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE teachers SET password = ? WHERE username = ?', (new_password, self.username))
        conn.commit()
        if cursor.rowcount == 0:
            QMessageBox.warning(self, "Error", "Password change failed.")
        else:
            QMessageBox.information(self, "Success", "Password changed successfully.")
        conn.close()

    def delacc1_btn(self):
        confirmation = self.ui.lineEdit_7.text().strip().lower()
        if confirmation != 'yes':
            QMessageBox.warning(self, "Error", "Type 'YES' to confirm account deletion.")
            return
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM teachers WHERE username = ?', (self.username,))
        conn.commit()
        if cursor.rowcount == 0:
            QMessageBox.warning(self, "Error", "Account deletion failed.")
        else:
            QMessageBox.information(self, "Success", "Account deleted successfully.")
            self.close()
            dialog = StartUp(self)
            dialog.exec_()
        conn.close()

    def close_btn(self):
        self.close()
        dialog = NotionBoard(self)
        dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = NotionBoard()
    win.show()
    sys.exit(app.exec())
    
























