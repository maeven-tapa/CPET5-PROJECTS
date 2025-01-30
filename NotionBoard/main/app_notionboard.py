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
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTreeWidgetItem
from about import Ui_about; from addstudpop import Ui_addstudpop; from edit_addstudpop import Ui_edit_addstudpop
from edit_todopop import Ui_edit_todopop; from editinfopop import Ui_editinfopop; from home import Ui_home; from landingpage import Ui_landingpage
from login_student import Ui_login_student; from login_teacher import Ui_login_teacher; from login import Ui_login; from options import Ui_options; 
from signup_stud import Ui_signup_stud; from signup_teacher import Ui_signup_teacher; from signup import Ui_signup; 
from startup import Ui_startup; from todolist_student import Ui_todolist_student
from todolist_teacher import Ui_todolist_teacher; from postpop import Ui_postpop
from todopop import Ui_todopop







"""
ooooo      ooo               .    o8o                        oooooooooo.                                     .o8  
`888b.     `8'             .o8    `"'                        `888'   `Y8b                                   "888  
 8 `88b.    8   .ooooo.  .o888oo oooo   .ooooo.  ooo. .oo.    888     888  .ooooo.   .oooo.   oooo d8b  .oooo888  
 8   `88b.  8  d88' `88b   888   `888  d88' `88b `888P"Y88b   888oooo888' d88' `88b `P  )88b  `888""8P d88' `888  
 8     `88b.8  888   888   888    888  888   888  888   888   888    `88b 888   888  .oP"888   888     888   888  
 8       `888  888   888   888 .  888  888   888  888   888   888    .88P 888   888 d8(  888   888     888   888  
o8o        `8  `Y8bod8P'   "888" o888o `Y8bod8P' o888o o888o o888bood8P'  `Y8bod8P' `Y888""8o d888b    `Y8bod88P"                                                                                                                                                                                                                                                                                                                                                                                                                    
"""

# By Maeven Tapa & Vinze Benitez


teachers = {}
students = {}

def load_data():
    if os.path.exists('data_notionboard.json'):
        with open('data_notionboard.json', 'r') as file:
            return json.load(file)
    return {'teachers': {}, 'students': {}}

def save_data(data):
    with open('data_notionboard.json', 'w') as file:
        json.dump(data, file, indent=4)

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
        self.close()
        dialog = signup_student(self)  
        dialog.exec_()

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
        self.close()
        dialog = login_student(self)  
        dialog.exec_() 







"""
████████ ███████  █████   ██████ ██   ██ ███████ ██████  
   ██    ██      ██   ██ ██      ██   ██ ██      ██   ██ 
   ██    █████   ███████ ██      ███████ █████   ██████  
   ██    ██      ██   ██ ██      ██   ██ ██      ██   ██ 
   ██    ███████ ██   ██  ██████ ██   ██ ███████ ██   ██ 
                                                                                                 
"""

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
        data = load_data()
        data['teachers'][username] = {
            'name': name,
            'birthday': birthday,
            'gender': gender,
            'password': password,
            'email': email,
            'usertype': 'teacher',
            'posts': []
        }
        save_data(data)
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
        data = load_data()
        if username in data['teachers'] and data['teachers'][username]['password'] == password:
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
        data = load_data()
        user_info = data['teachers'].get(self.username, {})
        if not user_info:
            return
        name = user_info.get('name', 'Unknown')
        birthday_str = user_info.get('birthday', '')
        try:
            birthday = datetime.strptime(birthday_str, '%B %d, %Y')
        except ValueError:
            return
        gender = user_info.get('gender', 'Unknown')
        usertype = user_info.get('usertype', 'Unknown')
        today = datetime.today()
        current_hour = datetime.now().hour
        if current_hour < 12:
            greeting = "Hi"
        elif current_hour < 18:
            greeting = "Wazzup"
        else:
            greeting = "Hi"
        self.ui.lbgreetings.setText(f"{greeting}, {name.split(' ')[0]}")  # Using first name for greeting
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
        data = load_data()
        if self.username in data['teachers']:
            posts = data['teachers'][self.username].get('posts', [])
            for post in posts:
                item = QTreeWidgetItem([post.get('post', ''), post.get('deadline', '')])
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
        data = load_data()
        if self.username in data['teachers']:
            data['teachers'][self.username]['posts'].pop(index)
            save_data(data)

    def notify_students(self, subject, message):
        with open("data_notionboard.json", "r") as file:
            data = json.load(file)
        teacher_data = data["teachers"].get(self.username, {})
        students = teacher_data.get("students", [])
        if not students:
            QMessageBox.warning(self, "Error", "No students found.")
            return
        sender_email = 'notionboard.tupcavite@gmail.com'  # Replace with your email
        password = 'fceq jsie lmdk uazf'  # Replace with your email password
        for student in students:
            receiver_email = student.get('email')
            if not receiver_email:
                continue
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
        post_data = []
        with open("data_notionboard.json", "r") as file:
            data = json.load(file)
        if self.username in data["teachers"]:
            teacher_data = data["teachers"][self.username]
            if "students" in teacher_data and teacher_data["students"]:
                for student in teacher_data["students"]:
                    message = f"Dear {student['name']},\n\nThe following posts are available:\n\n"
                    for post in teacher_data["posts"]:
                        message += f"Post: {post['post']}, Deadline: {post['deadline']}\n"
                    try:
                        self.notify_students(subject, message)
                    except Exception as e:
                        QMessageBox.warning(self, "Error", f"Failed to send notification to {student['name']}: {str(e)}")
            else:
                QMessageBox.warning(self, "Warning", "No students found.")
        else:
            QMessageBox.warning(self, "Error", "Teacher not found in the data.")

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
        data = load_data()
        user_info = data['teachers'].get(self.username, {})
        if not user_info:
            return
        self.ui.nameedit.setText(user_info.get('name', ''))
        self.ui.birthdayedit.setText(user_info.get('birthday', ''))
        self.ui.genderedit.setText(user_info.get('gender', ''))

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
        data = load_data()
        data['teachers'][self.username]['name'] = name
        data['teachers'][self.username]['birthday'] = birthday
        data['teachers'][self.username]['gender'] = gender
        save_data(data)
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
        data = load_data()
        if self.username not in data['teachers']:
            data['teachers'][self.username] = {'posts': []}
        if 'posts' not in data['teachers'][self.username]:
            data['teachers'][self.username]['posts'] = []
        data['teachers'][self.username]['posts'].append({'post': post, 'deadline': deadline})
        save_data(data)
        QMessageBox.information(self, "Success", "Post added successfully!")
        self.close()


class todolist_teacher(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_todolist_teacher()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.user_data = load_data().get('teachers', {}).get(self.username, {})
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
        todos = self.user_data.get('todos', [])
        for todo_data in todos:
            todo_item = QTreeWidgetItem([todo_data.get('tags', ''), todo_data.get('task', ''), todo_data.get('progress', '')])
            for i in range(3):
                todo_item.setTextAlignment(i, Qt.AlignHCenter)
            self.ui.teachtodo_table.addTopLevelItem(todo_item)

    def populate_stud_tree(self):
        self.ui.teachstudlist_table.clear()
        students = self.user_data.get('students', [])
        for stud_data in students:
            age = self.calculate_age(stud_data.get('birthday', ''))
            stud_item = QTreeWidgetItem([stud_data.get('name', ''), str(age), stud_data.get('email', '')])
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
        students = self.user_data.get('students', [])
        if not students:
            QMessageBox.warning(self, "Warning", "No students found.")
            return
        sender_email = 'notionboard.tupcavite@gmail.com'
        password = 'fceq jsie lmdk uazf'
        for student in students:
            receiver_email = student.get('email')
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
            requests.get('https://www.google.com', timeout=5)  # Change the URL if needed
        except requests.ConnectionError:
            QMessageBox.warning(self, "Warning", "No internet connection. Please check your network settings.")
            return
        self.notify_students(subject, message)

    def restud_btn(self):
        selected_item = self.ui.teachstudlist_table.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Error", "Please select a student to remove.")
            return
        index = self.ui.teachstudlist_table.indexOfTopLevelItem(selected_item)
        self.ui.teachstudlist_table.takeTopLevelItem(index)
        self.user_data['students'].pop(index)
        data = load_data()
        data['teachers'][self.username]['students'] = self.user_data['students']
        save_data(data)

    def retodo_btn(self):
        selected_item = self.ui.teachtodo_table.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Error", "Please select a task to remove.")
            return
        index = self.ui.teachtodo_table.indexOfTopLevelItem(selected_item)
        self.ui.teachtodo_table.takeTopLevelItem(index)
        self.user_data['todos'].pop(index)
        data = load_data()
        data['teachers'][self.username]['todos'] = self.user_data['todos']
        save_data(data)

class addstudpop(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_addstudpop()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.user_data = load_data().get('teachers', {}).get(self.username, {})
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
        stud_data = {'name': name, 'birthday': birthday, 'email': email}
        self.user_data.setdefault('students', []).append(stud_data)
        data = load_data()
        data['teachers'][self.username]['students'] = self.user_data['students']
        save_data(data)
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
        self.user_data = load_data().get('teachers', {}).get(self.username, {})
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
        students = self.user_data.get('students', [])
        if self.selected_index < 0 or self.selected_index >= len(students):
            QMessageBox.warning(self, "Error", "Invalid student selected.")
            self.close()
            return
        student = students[self.selected_index]
        self.ui.studnameedit.setText(student['name'])
        self.ui.studbirthdayedit.setText(student['birthday'])
        self.ui.studgenderedit.setText(student['email'])

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
        student = {'name': name, 'birthday': birthday, 'email': email}
        self.user_data['students'][self.selected_index] = student
        data = load_data()
        data['teachers'][self.username]['students'] = self.user_data['students']
        save_data(data)
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
        self.user_data = load_data().get('teachers', {}).get(self.username, {})
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
        todo_data = {'task': task, 'progress': progress, 'tags': tags}
        self.user_data.setdefault('todos', []).append(todo_data)
        data = load_data()
        data['teachers'][self.username]['todos'] = self.user_data['todos']
        save_data(data)
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
        self.user_data = load_data().get('teachers', {}).get(self.username, {})
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
        todos = self.user_data.get('todos', [])
        if self.selected_index < 0 or self.selected_index >= len(todos):
            QMessageBox.warning(self, "Error", "Invalid todo item selected.")
            self.close()
            return
        todo = todos[self.selected_index]
        self.ui.taskinput.setText(todo['task'])
        self.ui.progressinput.setText(todo['progress'])
        self.ui.tagskinput.setText(todo['tags'])

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
        todo = {'task': task, 'progress': progress, 'tags': tags}
        self.user_data['todos'][self.selected_index] = todo
        data = load_data()
        data['teachers'][self.username]['todos'] = self.user_data['todos']
        save_data(data)
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
        data = load_data()
        if self.username in data['teachers']:
            data['teachers'][new_username] = data['teachers'].pop(self.username)
            save_data(data)
            self.username = new_username
            QMessageBox.information(self, "Success", "Username changed successfully.")

    def changepass1_btn(self):
        new_password = self.ui.password.text().strip()
        confirm_password = self.ui.confirm_password.text().strip()
        if new_password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return
        data = load_data()
        if self.username in data['teachers']:
            data['teachers'][self.username]['password'] = new_password
            save_data(data)
            QMessageBox.information(self, "Success", "Password changed successfully.")

    def delacc1_btn(self):
        confirmation = self.ui.lineEdit_7.text().strip().lower()
        if confirmation != 'yes':
            QMessageBox.warning(self, "Error", "Type 'YES' to confirm account deletion.")
            return
        data = load_data()
        if self.username in data['teachers']:
            del data['teachers'][self.username]
            save_data(data)
            QMessageBox.information(self, "Success", "Account deleted successfully.")
            self.close()
            dialog = StartUp(self)  
            dialog.exec_()

    def close_btn(self):
        save_data(load_data())
        self.close()
        dialog = NotionBoard(self)  
        dialog.show()









"""
███████ ████████ ██    ██ ██████  ███████ ███    ██ ████████ 
██         ██    ██    ██ ██   ██ ██      ████   ██    ██    
███████    ██    ██    ██ ██   ██ █████   ██ ██  ██    ██    
     ██    ██    ██    ██ ██   ██ ██      ██  ██ ██    ██    
███████    ██     ██████  ██████  ███████ ██   ████    ██    
                                                                                                                      
"""
class signup_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_signup_stud()
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
        data = load_data()
        data['students'][username] = {
            'name': name,
            'birthday': birthday,
            'gender': gender,
            'password': password,
            'email': email,
            'usertype': 'students',
            'posts': []
        }
        save_data(data)
        QMessageBox.information(self, "Success", "Student signed up successfully!")
        self.close()
        dialog = StartUp(self)  
        dialog.exec_()

class login_student(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_login_student()
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
        data = load_data()
        if username in data['students'] and data['students'][username]['password'] == password:
            QMessageBox.information(self, "Success", "Logged in successfully!")
            self.close()
            dialog = home_student(self, username=username)  
            dialog.exec_() 
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials.")

class home_student(QDialog):
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
        data = load_data()
        user_info = data['students'].get(self.username, {})
        if not user_info:
            return
        name = user_info.get('name', 'Unknown')
        birthday_str = user_info.get('birthday', '')
        try:
            birthday = datetime.strptime(birthday_str, '%B %d, %Y')
        except ValueError:
            return
        gender = user_info.get('gender', 'Unknown')
        usertype = user_info.get('usertype', 'Unknown')
        today = datetime.today()
        current_hour = datetime.now().hour
        if current_hour < 12:
            greeting = "Hi"
        elif current_hour < 18:
            greeting = "Wazzup"
        else:
            greeting = "Hi"
        self.ui.lbgreetings.setText(f"{greeting}, {name.split(' ')[0]}")  # Using first name for greeting
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
        dialog = todolist_student(self, self.username)
        dialog.exec_()

    def options_btn(self):
        self.close()
        dialog = options_student(self, self.username)
        dialog.exec_()

    def editinfopop_btn(self):
        self.close()
        dialog = editinfopop_student(self, self.username)
        dialog.exec_()

    def populate_post_table(self):
        self.ui.post_table.clear()
        self.ui.post_table.setHeaderLabels(["Post:", "Deadline"])
        data = load_data()
        if self.username in data['students']:
            posts = data['students'][self.username].get('posts', [])
            for post in posts:
                item = QTreeWidgetItem([post.get('post', ''), post.get('deadline', '')])
                item.setTextAlignment(0, Qt.AlignHCenter)
                item.setTextAlignment(1, Qt.AlignHCenter)
                self.ui.post_table.addTopLevelItem(item)

    def postpop_btn(self):
        self.dialog = postpop_student(self, self.username)
        self.dialog.exec_()
        self.populate_post_table()

    def repost_btn(self):
        selected_item = self.ui.post_table.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Error", "Please select a post to remove.")
            return

        index = self.ui.post_table.indexOfTopLevelItem(selected_item)
        self.ui.post_table.takeTopLevelItem(index)

        data = load_data()
        if self.username in data['students']:
            data['students'][self.username]['posts'].pop(index)
            save_data(data)

    def notify_me(self, subject, message):
        sender_email = 'notionboard.tupcavite@gmail.com'
        password = 'fceq jsie lmdk uazf'
        with open("data_notionboard.json", "r") as file:
            data = json.load(file)
        user_data = data.get('students', {}).get(self.username, {})
        user_email = user_data.get('email')
        if not user_email:
            QMessageBox.warning(self, "Error", "User email not found.")
            return
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = user_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        try:
            socket.create_connection(("www.google.com", 80))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, user_email, text)
            server.quit()
            print(f"Notification sent to {user_email}")
        except Exception as e:
            print(f"Failed to send notification to {user_email}: {e}")
            raise RuntimeError("No internet connection.")

    def notify_btn(self):
        subject = "New Post Notification"
        with open("data_notionboard.json", "r") as file:
            data = json.load(file)
        if self.username in data["students"]:
            student_data = data["students"][self.username]
            message = f"Dear {student_data['name']},\n\nThe following posts are available:\n\n"
            for post in student_data.get("posts", []):
                message += f"Post: {post['post']}, Deadline: {post['deadline']}\n"
            try:
                self.notify_me(subject, message)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Failed to send notification: {str(e)}")
        else:
            QMessageBox.warning(self, "Error", "Teacher not found in the data.")

    def tup_page_btn(self):
        url = QUrl("https://www.tup.edu.ph/")
        QDesktopServices.openUrl(url)

class editinfopop_student(QDialog):
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
        data = load_data()
        user_info = data['students'].get(self.username, {})
        if not user_info:
            return
        self.ui.nameedit.setText(user_info.get('name', ''))
        self.ui.birthdayedit.setText(user_info.get('birthday', ''))
        self.ui.genderedit.setText(user_info.get('gender', ''))

    def back_btn(self):
        self.close()
        dialog = home_student(self, self.username)
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
        data = load_data()
        data['students'][self.username]['name'] = name
        data['students'][self.username]['birthday'] = birthday
        data['students'][self.username]['gender'] = gender
        save_data(data)
        QMessageBox.information(self, "Success", "Information updated successfully!")
        self.close()
        dialog = home_student(self, self.username)
        dialog.exec_()


class postpop_student(QDialog):
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
        data = load_data()
        if self.username not in data['students']:
            data['students'][self.username] = {'posts': []}
        if 'posts' not in data['students'][self.username]:
            data['students'][self.username]['posts'] = []
        data['students'][self.username]['posts'].append({'post': post, 'deadline': deadline})
        save_data(data)
        QMessageBox.information(self, "Success", "Post added successfully!")
        self.close()

class todolist_student(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_todolist_student()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.user_data = load_data().get('students', {}).get(self.username, {})
        self.populate_todo_tree()
        self.ui.home_btn.clicked.connect(self.home_teacher_btn)
        self.ui.opt_btn.clicked.connect(self.options_btn)
        self.ui.stud_addtodo_btn.clicked.connect(self.addtodo1_btn)
        self.ui.edittodo_btn.clicked.connect(self.edittodo1_btn)
        self.ui.removepost_btn.clicked.connect(self.retodo_btn)
        self.ui.notifyme__btn.clicked.connect(self.notify_btn)

    def populate_todo_tree(self):
        self.ui.studtodo_table.clear()
        todos = self.user_data.get('todos', [])
        for todo_data in todos:
            todo_item = QTreeWidgetItem([todo_data.get('tags', ''), todo_data.get('task', ''), todo_data.get('progress', '')])
            for i in range(3):
                todo_item.setTextAlignment(i, Qt.AlignHCenter)
            self.ui.studtodo_table.addTopLevelItem(todo_item)


    def calculate_age(self, birthday_str):
        try:
            birthday = datetime.strptime(birthday_str, '%B %d, %Y')
            today = datetime.today()
            return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
        except ValueError:
            return 'Unknown'

    def home_teacher_btn(self):
        self.close()
        dialog = home_student(self, self.username)
        dialog.exec_()

    def options_btn(self):
        self.close()
        dialog = options_teacher(self, self.username)
        dialog.exec_()

    def addtodo1_btn(self):
        self.close()
        dialog = todopop_student(self, self.username)
        dialog.exec_()

    def edittodo1_btn(self):
        self.close()
        dialog = edittodo_student(self, self.username)
        dialog.exec_()

    def notify_me(self, subject, message):
        sender_email = 'notionboard.tupcavite@gmail.com'
        password = 'fceq jsie lmdk uazf'
        with open("data_notionboard.json", "r") as file:
            data = json.load(file)
        user_data = data.get('students', {}).get(self.username, {})
        user_email = user_data.get('email')
        if not user_email:
            QMessageBox.warning(self, "Error", "User email not found.")
            return
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = user_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        try:
            socket.create_connection(("www.google.com", 80))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, user_email, text)
            server.quit()
            print(f"Notification sent to {user_email}")
        except Exception as e:
            print(f"Failed to send notification to {user_email}: {e}")
            raise RuntimeError("No internet connection.")

    def notify_btn(self):
        subject = "New To-Do Notification"
        message = "Dear User,\n\nHere are your new to-do items:\n\n"
        for row in range(self.ui.studtodo_table.topLevelItemCount()):
            item = self.ui.studtodo_table.topLevelItem(row)
            task = item.text(1)
            progress = item.text(2)
            tags = item.text(0)
            message += f"Task: {task}, Progress: {progress}, Tags: {tags}\n"
        try:
            self.notify_students(subject, message)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to send notification: {str(e)}")

    def retodo_btn(self):
        selected_item = self.ui.studtodo_table.currentItem()
        if selected_item is None:
            QMessageBox.warning(self, "Error", "Please select a task to remove.")
            return
        index = self.ui.studtodo_table.indexOfTopLevelItem(selected_item)
        self.ui.studtodo_table.takeTopLevelItem(index)
        self.user_data['todos'].pop(index)
        data = load_data()
        data['students'][self.username]['todos'] = self.user_data['todos']
        save_data(data)

class todopop_student(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_todopop()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.user_data = load_data().get('students', {}).get(self.username, {})
        self.ui.todoback_btn.clicked.connect(self.back_btn)
        self.ui.addtodo_btn.clicked.connect(self.addtodo1_btn)

    def back_btn(self):
        self.close()
        dialog = todolist_student(self.parent(), self.username)
        dialog.exec_()

    def addtodo1_btn(self):
        task = self.ui.taskinput.text()
        progress = self.ui.progressinput.text()
        tags = self.ui.tagskinput.text()
        if not task or not progress or not tags:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return
        todo_data = {'task': task, 'progress': progress, 'tags': tags}
        self.user_data.setdefault('todos', []).append(todo_data)
        data = load_data()
        data['students'][self.username]['todos'] = self.user_data['todos']
        save_data(data)
        QMessageBox.information(self, "Success", "To-do added successfully!")
        self.close()
        dialog = todolist_student(self.parent(), self.username)
        dialog.exec_()

class edittodo_student(QDialog):
    def __init__(self, parent=None, username=None):
        super().__init__(parent)
        self.ui = Ui_edit_todopop()
        self.ui.setupUi(self)
        self.setWindowTitle("NotionBoard")
        self.username = username
        self.user_data = load_data().get('students', {}).get(self.username, {})
        self.populate_fields()
        self.ui.todoback_btn.clicked.connect(self.back_btn)
        self.ui.addtodo_btn.clicked.connect(self.edittodo_btn)

    def populate_fields(self):
        selected_item = self.parent().ui.studtodo_table.currentItem()
        if not selected_item:
            QMessageBox.warning(self, "Error", "No todo item selected for editing.")
            self.close()
            return
        self.selected_index = self.parent().ui.studtodo_table.indexOfTopLevelItem(selected_item)
        todos = self.user_data.get('todos', [])
        if self.selected_index < 0 or self.selected_index >= len(todos):
            QMessageBox.warning(self, "Error", "Invalid todo item selected.")
            self.close()
            return
        todo = todos[self.selected_index]
        self.ui.taskinput.setText(todo['task'])
        self.ui.progressinput.setText(todo['progress'])
        self.ui.tagskinput.setText(todo['tags'])

    def back_btn(self):
        self.close()
        dialog = todolist_student(self.parent(), self.username)
        dialog.exec_()

    def edittodo_btn(self):
        task = self.ui.taskinput.text()
        progress = self.ui.progressinput.text()
        tags = self.ui.tagskinput.text()
        if not task or not progress or not tags:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return
        todo = {'task': task, 'progress': progress, 'tags': tags}
        self.user_data['todos'][self.selected_index] = todo
        data = load_data()
        data['students'][self.username]['todos'] = self.user_data['todos']
        save_data(data)
        QMessageBox.information(self, "Success", "Todo item updated successfully!")
        self.close()
        dialog = todolist_teacher(self.parent(), self.username)
        dialog.exec_()

class options_student(QDialog):
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
        dialog = home_student(self, self.username)  
        dialog.exec_() 

    def todo1_btn(self):
        self.close()
        dialog = todolist_student(self, self.username)  
        dialog.exec_()

    def changeusername1_btn(self):
        new_username = self.ui.username.text().strip()
        confirm_username = self.ui.confirm_username.text().strip()
        if new_username != confirm_username:
            QMessageBox.warning(self, "Error", "Usernames do not match.")
            return
        data = load_data()
        if self.username in data['students']:
            data['students'][new_username] = data['students'].pop(self.username)
            save_data(data)
            self.username = new_username
            QMessageBox.information(self, "Success", "Username changed successfully.")

    def changepass1_btn(self):
        new_password = self.ui.password.text().strip()
        confirm_password = self.ui.confirm_password.text().strip()
        if new_password != confirm_password:
            QMessageBox.warning(self, "Error", "Passwords do not match.")
            return
        data = load_data()
        if self.username in data['students']:
            data['students'][self.username]['password'] = new_password
            save_data(data)
            QMessageBox.information(self, "Success", "Password changed successfully.")

    def delacc1_btn(self):
        confirmation = self.ui.lineEdit_7.text().strip().lower()
        if confirmation != 'yes':
            QMessageBox.warning(self, "Error", "Type 'YES' to confirm account deletion.")
            return
        data = load_data()
        if self.username in data['students']:
            del data['students'][self.username]
            save_data(data)
            QMessageBox.information(self, "Success", "Account deleted successfully.")
            self.close()
            dialog = StartUp(self)  
            dialog.exec_()

    def close_btn(self):
        save_data(load_data())
        self.close()
        dialog = NotionBoard(self)  
        dialog.show()






#Starter
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = NotionBoard()
    win.show()
    sys.exit(app.exec())