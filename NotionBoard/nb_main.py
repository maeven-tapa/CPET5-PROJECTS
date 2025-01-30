import sys
import re
import requests
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QTreeWidgetItem
from landingpage import Ui_Landingpage
from startup import Ui_startup
from about import Ui_About
from signup import Ui_SignUP
from signup2 import Ui_SignUP2
from signup3 import Ui_SignUP3
from Login import Ui_LogIN
from Login2 import Ui_LogIN2
from Login3 import Ui_LogIN3
from Home import Ui_Home
from todonoti import Ui_todonoti
from Options import Ui_Options
from postpop import Ui_postpop
from studpop import Ui_studpop
from todopop import Ui_todopop
from restudpop import Ui_restudpop
from viewpost import Ui_viewpost
from viewtodo import Ui_viewtodo
from sendnotif import Ui_sendnotif
from viewstud import Ui_viewstud

teachers = {}
students = {}


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Landingpage()  
        self.ui.setupUi(self)  

        self.ui.start.clicked.connect(self.startUp)

    def startUp(self):
        self.close()
        dialog = StartUpDialog(self)  
        dialog.exec_() 


class StartUpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_startup()
        self.ui.setupUi(self)  

        self.ui.sub.clicked.connect(self.signUp)
        self.ui.lib.clicked.connect(self.logIn)
        self.ui.abb.clicked.connect(self.about)

    def about(self):
        self.close()
        dialog = AboutDialog(self)
        dialog.exec_() 

    def signUp(self):
        self.close()
        dialog = SignUpDialog(self)
        dialog.exec_()  

    def logIn(self):
        self.close()
        dialog = LogInDialog(self)
        dialog.exec_()  

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_About()
        self.ui.setupUi(self)  

        self.ui.pushButton_3.clicked.connect(self.back)

    def back(self):
        self.close()
        dialog = StartUpDialog(self)  
        dialog.exec_() 

class SignUpDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignUP()
        self.ui.setupUi(self)  

        self.ui.pushButton_3.clicked.connect(self.signUp2)
        self.ui.pushButton_4.clicked.connect(self.signUp3)
        self.ui.pushButton_6.clicked.connect(self.back)

    def back(self):
        self.close()
        dialog = StartUpDialog(self)  
        dialog.exec_() 

    def signUp2(self):
        self.close()
        dialog = SignUp2Dialog(self)
        dialog.exec_() 

    def signUp3(self):
        self.close()
        dialog = SignUp3Dialog(self)
        dialog.exec_() 




class LogInDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LogIN()
        self.ui.setupUi(self)  

        self.ui.pushButton_3.clicked.connect(self.logIn2)
        self.ui.pushButton_4.clicked.connect(self.logIn3)
        self.ui.pushButton_6.clicked.connect(self.back)

    def back(self):
        self.close()
        dialog = StartUpDialog(self)  
        dialog.exec_() 

    def logIn2(self):
        self.close()
        dialog = LogIn2Dialog(self)
        dialog.exec_()   

    def logIn3(self):
        self.close()
        dialog = LogIn3Dialog(self)
        dialog.exec_()   

class LogIn2Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LogIN2()
        self.ui.setupUi(self)  

        self.ui.pushButton_4.clicked.connect(self.logInTeacher)
        self.ui.pushButton_6.clicked.connect(self.back)

    def back(self):
        self.close()
        dialog = StartUpDialog(self)  
        dialog.exec_() 

    def logInTeacher(self):
        username = self.ui.ltu1.text().lower()  # Convert entered username to lowercase
        password = self.ui.ltp1.text()

        # Check if the username exists in the teachers' data (case insensitive)
        if username in teachers and teachers[username]["password"] == password:
            self.close()
            # Pass the post count as 0 initially
            self.launchHome(teachers[username])  # Pass user data to the launchHome method
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def launchHome(self, user_data):
        home_dialog = HomeDialog(user_data, parent=self)  # Pass user data and parent to HomeDialog
        home_dialog.exec_()

class LogIn3Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LogIN3()
        self.ui.setupUi(self)    

        self.ui.pushButton_4.clicked.connect(self.logInStudent)
        self.ui.pushButton_6.clicked.connect(self.back)

    def back(self):
        self.close()
        dialog = StartUpDialog(self)  
        dialog.exec_() 

    def logInStudent(self):
        username = self.ui.lsu1.text().lower()  # Convert entered username to lowercase
        password = self.ui.lsp1.text()

        # Check if the username exists in the students' data (case insensitive)
        if username in students and students[username]["password"] == password:
            self.close()
            # Pass the post count as 0 initially
            self.launchHome(students[username])  # Pass user data to the launchHome method
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password")

    def launchHome(self, user_data):
        home_dialog = HomeDialog(user_data, parent=self)  # Pass user data and parent to HomeDialog
        home_dialog.exec_()




class SignUp2Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignUP2()
        self.ui.setupUi(self)  

        self.ui.pushButton_4.clicked.connect(self.startUp)  
        self.ui.pushButton_6.clicked.connect(self.back)

    def back(self):
        self.close()
        dialog = StartUpDialog(self)  
        dialog.exec_() 

    def startUp(self):
        name = self.ui.stn1.text()
        birthday = self.ui.stb1.text()
        gender = self.ui.stg1.text()
        username = self.ui.stu1.text()
        password = self.ui.stp1.text()

        if name and birthday and gender and username and password:  # Check if all fields are filled
            name_pattern = r'^[A-Z][a-z]+\s[A-Z]\.\s[A-Z][a-z]+$'  # Regular expression pattern for name format
            birthday_pattern = r'^(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$'  # Regular expression pattern for birthday format
            password_pattern = r'^.{6,}$'  # Regular expression pattern for password length (at least 6 characters)
            username_pattern = r'^[a-z0-9]+$'  # Regular expression pattern for username format (lowercase letters and digits only)

            if (re.match(name_pattern, name) and
                re.match(birthday_pattern, birthday) and
                re.match(password_pattern, password) and
                re.match(username_pattern, username)):

                teacher_data = {
                    "name": name,
                    "birthday": birthday,
                    "gender": gender,
                    "username": username,
                    "password": password,
                    "status": "teacher",
                }
                global teachers
                teachers[username] = teacher_data  # Save data in the teachers dictionary using the username as key

                self.close()
                dialog = StartUpDialog(self)  
                dialog.exec_()
            else:
                error_messages = []
                if not re.match(name_pattern, name):
                    error_messages.append("Please enter the name in the format: Firstname MiddleInitial Lastname")
                if not re.match(birthday_pattern, birthday):
                    error_messages.append("Please enter the birthday in the format: Month Day, Year (e.g., July 21, 2005)")
                if not re.match(password_pattern, password):
                    error_messages.append("Password must be at least 6 characters long")
                if not re.match(username_pattern, username):
                    error_messages.append("Username must be in lowercase letters and digits only")
                
                QMessageBox.warning(self, "Invalid Input", "\n".join(error_messages))
        else:
            QMessageBox.warning(self, "Incomplete Information", "Please fill in all fields")

class SignUp3Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignUP3()
        self.ui.setupUi(self)     

        self.ui.pushButton_4.clicked.connect(self.startUp)   
        self.ui.pushButton_6.clicked.connect(self.back)

    def back(self):
        self.close()
        dialog = StartUpDialog(self)  
        dialog.exec_() 

    def startUp(self):
        name = self.ui.ssn1.text()
        birthday = self.ui.ssb1.text()
        gender = self.ui.ssg1.text()
        username = self.ui.stu1.text()
        password = self.ui.ssp1.text()
        email = self.ui.sse1.text()

        if name and birthday and gender and username and password and email:  # Check if all fields are filled
            name_pattern = r'^[A-Z][a-z]+\s[A-Z]\.\s[A-Z][a-z]+$'  # Regular expression pattern for name format
            birthday_pattern = r'^(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$'  # Regular expression pattern for birthday format
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  # Regular expression pattern for email format
            password_pattern = r'^.{6,}$'  # Regular expression pattern for password length (at least 6 characters)
            username_pattern = r'^[a-z0-9]+$'  # Regular expression pattern for username format (lowercase letters and digits only)

            if (re.match(name_pattern, name) and
                re.match(birthday_pattern, birthday) and
                re.match(password_pattern, password) and
                re.match(username_pattern, username) and
                re.match(email_pattern, email)):

                student_data = {
                    "name": name,
                    "birthday": birthday,
                    "gender": gender,
                    "username": username,
                    "password": password,
                    "email": email,
                    "status": "student",
                }
                global students
                students[username] = student_data  # Save data in the students dictionary using the username as key

                self.close()
                dialog = StartUpDialog(self)  
                dialog.exec_()
            else:
                error_messages = []
                if not re.match(name_pattern, name):
                    error_messages.append("Please enter the name in the format: Firstname MiddleInitial Lastname")
                if not re.match(birthday_pattern, birthday):
                    error_messages.append("Please enter the birthday in the format: Month Day, Year (e.g., July 21, 2005)")
                if not re.match(password_pattern, password):
                    error_messages.append("Password must be at least 6 characters long")
                if not re.match(username_pattern, username):
                    error_messages.append("Username must be in lowercase letters and digits only")
                if not re.match(email_pattern, email):
                    error_messages.append("Please enter a valid email address")
                
                QMessageBox.warning(self, "Invalid Input", "\n".join(error_messages))
        else:
            QMessageBox.warning(self, "Incomplete Information", "Please fill in all fields")




def get_weather():
    api_key = "a77f2ef1d95f695092242042a413088b"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    city = "Dasmariñas,PH"  # Default location
    
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        temperature = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        
        if "rain" in weather_desc:
            weather_msg = "It's raining on campus!"
        elif temperature > 30:
            weather_msg = "It's hot! Bring an umbrella."
        elif temperature < 15:
            weather_msg = "It's cold! Bring a jacket."
        else:
            weather_msg = "Weather is moderate."
        
        return f"It's {temperature}°C today. {weather_msg}"
    else:
        return "Weather information not available."

class PostPopDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_postpop()
        self.ui.setupUi(self)
        self.user_data = user_data
        
        # Connect button clicks to methods
        self.ui.ppdb1.clicked.connect(self.doneAction)
        self.ui.ppb1.clicked.connect(self.goBack)

    def doneAction(self):
        # Get the text from the QLineEdit widgets
        post_text = self.ui.stn1.text()
        deadline_text = self.ui.dl1.text()

        # Add the user inputs to the user_data dictionary
        if 'posts' not in self.user_data:
            self.user_data['posts'] = []

        if not re.match(r'^(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$', deadline_text):
            QMessageBox.warning(self, "Invalid Deadline", "Please enter the deadline in the format: Month Day, Year (e.g., July 21, 2005)")
            return

        self.user_data['posts'].append({'post': post_text, 'deadline': deadline_text})

        # Close the dialog
        self.close()
        # Open the home dialog
        self.goBack()

    def goBack(self):
        # Close the current dialog
        self.close()
        # Open the home dialog
        dialog = HomeDialog(self.user_data, parent=self.parent())
        dialog.exec_()

class ViewPostDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_viewpost()
        self.ui.setupUi(self)
        self.user_data = user_data

        # Connect button clicks to methods
        self.ui.vpbb1.clicked.connect(self.goBack)
        self.ui.vprb1.clicked.connect(self.removePost)

        # Populate QTreeWidget with user_data
        self.populateTreeWidget()

    def populateTreeWidget(self):
        posts = self.user_data.get('posts', [])
        for post_data in posts:
            post_item = QTreeWidgetItem(self.ui.treeWidget)
            post_item.setText(0, post_data.get('deadline', ''))
            post_item.setText(1, post_data.get('post', ''))

    def removePost(self):
        selected_items = self.ui.treeWidget.selectedItems()
        if selected_items:
            for item in selected_items:
                index = self.ui.treeWidget.indexOfTopLevelItem(item)
                self.ui.treeWidget.takeTopLevelItem(index)
                
                # Remove the corresponding post from user_data
                deadline = item.text(0)
                post = item.text(1)
                posts = self.user_data.get('posts', [])
                updated_posts = [p for p in posts if (p['deadline'] != deadline) or (p['post'] != post)]
                self.user_data['posts'] = updated_posts

    def goBack(self):
        # Close the current dialog
        self.close()
        # Open the home dialog
        dialog = HomeDialog(self.user_data, parent=self.parent())
        dialog.exec_()

class HomeDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        self.user_data = user_data
        
        # Update labels with user information
        self.update_user_info()
        
        # Update weather label
        self.update_weather_info()

        self.num_posts = self.count_posts()
        self.update_post_status()

        self.ui.hh1.clicked.connect(self.goHome)
        self.ui.tn1.clicked.connect(self.goToDo)
        self.ui.op1.clicked.connect(self.goOptions)
        self.ui.pushButton_4.clicked.connect(self.gotopostpop)
        self.ui.pushButton_8.clicked.connect(self.gotoviewpost)

    def gotopostpop(self):
        self.close()
        dialog = PostPopDialog(self.user_data, parent=self.parent())
        dialog.exec_()

    def gotoviewpost(self):
        self.close()
        dialog = ViewPostDialog(self.user_data, parent=self.parent())
        dialog.exec_()

    def update_post_status(self):
        if self.num_posts == 0:
            self.ui.namelabel_2.setText("There are no posts yet!")
        else:
            self.ui.namelabel_2.setText(f"There are {self.num_posts} post{'s' if self.num_posts > 1 else ''} posted.")

    def count_posts(self):
        posts_data = self.user_data.get('posts', [])  # Get the list of posts from user_data
        return len(posts_data) 

    def update_user_info(self):
        # Update greetings label
        name = self.user_data['name']
        first_name = name.split()[0].capitalize()  # Extract the first name from the full name
        self.ui.grettingslabel.setText(f"Hi, {first_name}!")

        # Update name label
        self.ui.namelabel.setText(name)

        # Update birthday label with current age
        birthday = self.user_data['birthday']
        birth_date = datetime.strptime(birthday, '%B %d, %Y')
        age = (datetime.now() - birth_date).days // 365
        birthday_text = f"{birthday} / {age} years old"
        self.ui.birthdaylabel.setText(birthday_text)

        # Update gender label with status
        gender = self.user_data['gender']
        status = self.user_data['status']
        gender_status = f"{gender.capitalize()} / {status.capitalize()}"
        self.ui.genderlabel.setText(gender_status)
        
    def update_weather_info(self):
        weather_info = get_weather()
        self.ui.weatherlabel.setAlignment(QtCore.Qt.AlignCenter)  # Align text to center
        self.ui.weatherlabel.setText(weather_info)

        
    def goHome(self):
        self.close()
        dialog = HomeDialog(self.user_data, self.parent())
        dialog.exec_()

    def goToDo(self):
        self.close()
        dialog = ToDoNotiDialog(self.user_data, self.parent())
        dialog.exec_()

    def goOptions(self):
        self.close()
        dialog = OptionsDialog(self.user_data, self.parent())
        dialog.exec_()




class TodoPopDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_todopop()
        self.ui.setupUi(self)
        self.user_data = user_data
        self.ui.backbutton2.clicked.connect(self.goBack)
        self.ui.addpostbutton2.clicked.connect(self.addPost)

    def goBack(self):
        self.close()
        dialog = ViewToDoDialog(self.user_data, parent=self.parent())
        dialog.exec_()

    def addPost(self):
        task = self.ui.taskinput.text()
        progress = self.ui.progressinput.text()
        tags = self.ui.tagsinput.text()

        # Save the inputs to user_data
        if 'todos' not in self.user_data:
            self.user_data['todos'] = []

        self.user_data['todos'].append({'task': task, 'progress': progress, 'tags': tags})

        # Go back to ViewToDoDialog to update the TreeWidget
        self.goBack()
    
class ViewToDoDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_viewtodo()
        self.ui.setupUi(self)
        self.user_data = user_data
        self.ui.vprb1.clicked.connect(self.removeToDo)
        self.ui.vpbb1.clicked.connect(self.goBack)
        self.ui.vprb1_2.clicked.connect(self.gotodopop)

        # Populate QTreeWidget with user_data
        self.populateTreeWidget()

    def populateTreeWidget(self):
        todos = self.user_data.get('todos', [])
        for todo_data in todos:
            todo_item = QTreeWidgetItem(self.ui.treeWidget)
            todo_item.setText(0, todo_data.get('task', ''))
            todo_item.setText(1, todo_data.get('progress', ''))
            todo_item.setText(2, todo_data.get('tags', ''))

    def removeToDo(self):
        selected_items = self.ui.treeWidget.selectedItems()
        if selected_items:
            for item in selected_items:
                index = self.ui.treeWidget.indexOfTopLevelItem(item)
                self.ui.treeWidget.takeTopLevelItem(index)
                
                # Remove the corresponding todo from user_data
                task = item.text(0)
                progress = item.text(1)
                tags = item.text(2)
                todos = self.user_data.get('todos', [])
                updated_todos = [t for t in todos if (t['task'] != task) or (t['progress'] != progress) or (t['tags'] != tags)]
                self.user_data['todos'] = updated_todos

    def gotodopop(self):
        self.close()
        dialog = TodoPopDialog(self.user_data, parent=self.parent())
        dialog.exec_()

    def goBack(self):
        self.close()
        dialog = ToDoNotiDialog(self.user_data, parent=self.parent())
        dialog.exec_()

class SendNotifDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_sendnotif()
        self.ui.setupUi(self)
        self.user_data = user_data

        # Connect button clicks to methods
        self.ui.snbb1.clicked.connect(self.goBack)
        self.ui.notifypost.clicked.connect(self.notifyPost)
        self.ui.sndb1_2.clicked.connect(self.notifyTodoList)

        # Populate tree widget with student data
        self.populateTreeWidget()

    def goBack(self):
        # Close the current dialog
        self.close()
        # Open the home dialog
        dialog = ToDoNotiDialog(self.user_data, parent=self.parent())
        dialog.exec_()

    def notifyPost(self):
        # Get the posts data
        posts_data = self.user_data.get('posts', [])
        # Send the posts data via email
        self.sendEmail(posts_data)

    def notifyTodoList(self):
        # Get the todos data
        todos_data = self.user_data.get('todos', [])
        # Send the todos data via email
        self.sendEmail(todos_data)

    def populateTreeWidget(self):
        students = self.user_data.get('students', [])
        for student in students:
            student_item = QTreeWidgetItem(self.ui.treeWidget)
            student_item.setText(0, student.get('name', ''))
            student_item.setText(1, student.get('email', ''))

    def sendEmail(self, data):
        # Configure email settings
        sender_email = "notionboard.tupc@gmail.com"
        password = "yourpassword"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join([student['email'] for student in self.user_data.get('students', [])])
        msg['Subject'] = "Notification"

        # Create the message body
        body = "\n".join([f"{index + 1}. {post['task']}: {post['progress']}, Tags: {post['tags']}" for index, post in enumerate(data)])
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, msg['To'], msg.as_string())
            
    def populateTreeWidget(self):
        students = self.user_data.get('students', [])
        for student in students:
            student_item = QTreeWidgetItem(self.ui.treeWidget)
            student_item.setText(0, student.get('name', ''))
            student_item.setText(1, student.get('email', ''))

class StudPopDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_studpop()
        self.ui.setupUi(self)
        self.user_data = user_data

        # Connect button clicks to methods
        self.ui.spdb1.clicked.connect(self.addStudent)
        self.ui.spb1.clicked.connect(self.goBack)

    def validateInputs(self):
        name = self.ui.nbb1.text()
        birthday = self.ui.bb1.text()
        email = self.ui.seb1.text()

        if name and birthday and email:
            name_pattern = r'^[A-Z][a-z]+\s[A-Z]\.\s[A-Z][a-z]+$'  
            birthday_pattern = r'^(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$'
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            if (re.match(name_pattern, name) and
                re.match(birthday_pattern, birthday) and
                re.match(email_pattern, email)):
                return True
            else:
                error_messages = []
                if not re.match(name_pattern, name):
                    error_messages.append("Please enter the name in the format: Firstname MiddleInitial Lastname")
                if not re.match(birthday_pattern, birthday):
                    error_messages.append("Please enter the birthday in the format: Month Day, Year (e.g., July 21, 2005)")
                if not re.match(email_pattern, email):
                    error_messages.append("Please enter a valid email address")
                
                QMessageBox.warning(self, "Invalid Input", "\n".join(error_messages))
                return False
        else:
            QMessageBox.warning(self, "Incomplete Information", "Please fill in all fields")
            return False

    def addStudent(self):
        if self.validateInputs():
            name = self.ui.nbb1.text()
            birthday = self.ui.bb1.text()
            email = self.ui.seb1.text()

            # Add student data to user_data
            student_data = {'name': name, 'birthday': birthday, 'email': email}
            students = self.user_data.get('students', [])
            students.append(student_data)
            self.user_data['students'] = students

            # Show pop-up message
            QMessageBox.information(self, "Success", "Student added successfully!")

            # Clear input fields
            self.ui.nbb1.clear()
            self.ui.bb1.clear()
            self.ui.seb1.clear()
    def goBack(self):
        self.close()
        dialog = ToDoNotiDialog(self.user_data, parent=self.parent())
        dialog.exec_()

class ReStudPopDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_restudpop()
        self.ui.setupUi(self)
        self.user_data = user_data

        # Connect button clicks to methods
        self.ui.rspdb1.clicked.connect(self.removeStudent)
        self.ui.rspb1.clicked.connect(self.goBack)

    def removeStudent(self):
        name = self.ui.rnbb1.text()
        confirm_name = self.ui.bb1.text()

        if name and name == confirm_name:
            # Retrieve the students' data
            students = self.user_data.get('students', [])
            # Check if the student exists
            for student in students:
                if student['name'] == name:
                    students.remove(student)
                    QMessageBox.information(self, "Student Removed", f"{name} has been successfully removed.")
                    break
            else:
                QMessageBox.warning(self, "Student Not Found", f"No student named {name} exists.")
        else:
            QMessageBox.warning(self, "Invalid Input", "Names do not match or are empty.")

    def goBack(self):
        self.close()
        dialog = ToDoNotiDialog(self.user_data, parent=self.parent())
        dialog.exec_()

class ViewStudDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_viewstud()
        self.ui.setupUi(self)
        self.user_data = user_data

        # Connect button clicks to methods
        self.ui.vsbb1_2.clicked.connect(self.goBack)

        # Populate QTreeWidget with student data
        self.populateTreeWidget()

    def populateTreeWidget(self):
        students = self.user_data.get('students', [])
        for student_data in students:
            student_item = QTreeWidgetItem(self.ui.treeWidget_2)
            student_item.setText(0, student_data.get('name', ''))
            student_item.setText(1, self.calculate_age(student_data.get('birthday', '')))
            student_item.setText(2, student_data.get('email', ''))

    def calculate_age(self, birthday):
        birth_date = datetime.strptime(birthday, '%B %d, %Y')
        age = (datetime.now() - birth_date).days // 365
        return str(age) if age >= 0 else 'N/A'

    def goBack(self):
        self.close()
        dialog = ToDoNotiDialog(self.user_data, parent=self.parent())
        dialog.exec_()

class ToDoNotiDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_todonoti()
        self.ui.setupUi(self)
        self.user_data = user_data

        self.ui.hh2.clicked.connect(self.goHome)
        self.ui.tn2.clicked.connect(self.goToDo)
        self.ui.pushButton_15.clicked.connect(self.goOptions)
        self.ui.viewtodobutton.clicked.connect(self.goToViewToDo)
        self.ui.sendnotifbutton.clicked.connect(self.goToSendNotif)
        self.ui.removestudentbutton.clicked.connect(self.goToReStudPop)
        self.ui.viewstudentbutton.clicked.connect(self.goToViewStud)
        self.ui.addstudentbutton.clicked.connect(self.goToStudPop)

        self.update_todo_status()

    def goToViewToDo(self):
        self.close()
        dialog = ViewToDoDialog(self.user_data, self.parent())
        dialog.exec_()

    def goToSendNotif(self):
        self.close()
        dialog = SendNotifDialog(self.user_data, self.parent())
        dialog.exec_()

    def goToStudPop(self):
        self.close()
        dialog = StudPopDialog(self.user_data, self.parent())
        dialog.exec_()

    def goToReStudPop(self):
        self.close()
        dialog = ReStudPopDialog(self.user_data, self.parent())
        dialog.exec_()

    def goToViewStud(self):
        self.close()
        dialog = ViewStudDialog(self.user_data, self.parent())
        dialog.exec_()

    def goHome(self):
        self.close()
        dialog = HomeDialog(self.user_data, self.parent())
        dialog.exec_()

    def goToDo(self):
        self.close()
        dialog = ToDoNotiDialog(self.user_data, self.parent())
        dialog.exec_()

    def goOptions(self):
        self.close()
        dialog = OptionsDialog(self.user_data, self.parent())
        dialog.exec_()

    def update_todo_status(self):
        num_todos = self.count_todos()
        if num_todos == 0:
            self.ui.label_22.setText("No todos yet")
        else:
            self.ui.label_22.setText(f"{num_todos} todo{'s' if num_todos > 1 else ''} posted")

    def count_todos(self):
        todos = self.user_data.get('todos', [])
        return len(todos)



class OptionsDialog(QDialog):
    def __init__(self, user_data, parent=None):
        super().__init__(parent)
        self.ui = Ui_Options()
        self.ui.setupUi(self)
        self.user_data = user_data

        self.ui.applychangebutton.clicked.connect(self.apply_changes)
        self.ui.delaccbutton.clicked.connect(self.delete_account)
        self.ui.pushButton_2.clicked.connect(self.exit_app)

        self.ui.hh3.clicked.connect(self.goHome)
        self.ui.tn3.clicked.connect(self.goToDo)
        self.ui.op3.clicked.connect(self.goOptions)

    def apply_changes(self):
        new_name = self.ui.lineEdit.text()
        new_birthday = self.ui.lineEdit_2.text()

        # Validate the new name format
        name_pattern = r'^[A-Z][a-z]+\s[A-Z]\.\s[A-Z][a-z]+$'
        if new_name and not re.match(name_pattern, new_name):
            QMessageBox.warning(self, "Invalid Name Format", "Please enter the name in the format: Firstname MiddleInitial Lastname")
            return

        # Validate the new birthday format
        birthday_pattern = r'^(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}$'
        if new_birthday and not re.match(birthday_pattern, new_birthday):
            QMessageBox.warning(self, "Invalid Birthday Format", "Please enter the birthday in the format: Month Day, Year (e.g., July 21, 2005)")
            return

        # Apply the changes to the user data
        if new_name:
            self.user_data['name'] = new_name
        if new_birthday:
            self.user_data['birthday'] = new_birthday

        # Display a message indicating that changes have been applied
        QMessageBox.information(self, "Changes Applied", "Changes have been applied successfully.")

    def delete_account(self):
        # Delete the current user's account data
        username = self.user_data['username']
        if self.user_data['status'] == 'teacher':
            del teachers[username]
        else:
            del students[username]

        # Display a message indicating that the account has been deleted
        QMessageBox.information(self, "Account Deleted", "Your account has been deleted.")
        self.close()
        # Go back to the landing page
        start_up_dialog = StartUpDialog(self.parent())
        start_up_dialog.exec_()

    def exit_app(self):
        # Close the application
        QApplication.quit()

    def goHome(self):
        self.close()
        dialog = HomeDialog(self.user_data, self.parent())
        dialog.exec_()

    def goToDo(self):
        self.close()
        dialog = ToDoNotiDialog(self.user_data, self.parent())
        dialog.exec_()

    def goOptions(self):
        self.close()
        dialog = OptionsDialog(self.user_data, self.parent())
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
