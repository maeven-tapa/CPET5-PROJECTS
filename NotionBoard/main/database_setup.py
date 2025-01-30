import sqlite3

def create_connection():
    conn = sqlite3.connect('notionboard.db')
    return conn

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            birthday TEXT NOT NULL,
            gender TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            usertype TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teacher_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER,
            post TEXT NOT NULL,
            deadline TEXT NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teacher_todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER,
            task TEXT NOT NULL,
            progress TEXT NOT NULL,
            tags TEXT NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER,
            name TEXT NOT NULL,
            birthday TEXT NOT NULL,
            gender TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            usertype TEXT NOT NULL,
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            post TEXT NOT NULL,
            deadline TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER,
            task TEXT NOT NULL,
            progress TEXT NOT NULL,
            tags TEXT NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    ''')
    
    conn.commit()
    conn.close()


def load_teacher_data(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teachers WHERE username=?", (username,))
    teacher_data = cursor.fetchone()
    conn.close()
    if teacher_data:
        return {
            'username': teacher_data[1],
            'name': teacher_data[2],
            'birthday': teacher_data[3],
            'gender': teacher_data[4],
            'password': teacher_data[5],
            'email': teacher_data[6],
            'usertype': teacher_data[7]
        }
    else:
        return None

def load_teacher_posts(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teacher_posts WHERE teacher_id=(SELECT id FROM teachers WHERE username=?)", (username,))
    posts = cursor.fetchall()
    conn.close()
    return [{'post': post[2], 'deadline': post[3]} for post in posts]

def load_teacher_todos(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teacher_todos WHERE teacher_id=(SELECT id FROM teachers WHERE username=?)", (username,))
    todos = cursor.fetchall()
    conn.close()
    return [{'task': todo[2], 'progress': todo[3], 'tags': todo[4]} for todo in todos]

def load_students(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE teacher_id=(SELECT id FROM teachers WHERE username=?)", (username,))
    students = cursor.fetchall()
    conn.close()
    return [{'name': student[2], 'birthday': student[3], 'email': student[4]} for student in students]

def save_teacher_data(username, name, birthday, gender, password, email, usertype):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teachers (username, name, birthday, gender, password, email, usertype) VALUES (?, ?, ?, ?, ?, ?, ?)", (username, name, birthday, gender, password, email, usertype))
    conn.commit()
    conn.close()

def save_teacher_post(username, post, deadline):
    conn = create_connection()
    cursor = conn.cursor()
    teacher_id = load_teacher_data(username)['id']
    cursor.execute("INSERT INTO teacher_posts (teacher_id, post, deadline) VALUES (?, ?, ?)", (teacher_id, post, deadline))
    conn.commit()
    conn.close()

def save_teacher_todos(username, todos):
    conn = create_connection()
    cursor = conn.cursor()
    teacher_id = load_teacher_data(username)['id']
    cursor.execute("DELETE FROM teacher_todos WHERE teacher_id=?", (teacher_id,))
    for todo in todos:
        cursor.execute("INSERT INTO teacher_todos (teacher_id, task, progress, tags) VALUES (?, ?, ?, ?)", (teacher_id,) + todo)
    conn.commit()
    conn.close()

def save_student(username, teacher_username, name, birthday, gender, password, email, usertype):
    conn = create_connection()
    cursor = conn.cursor()
    teacher_id = load_teacher_data(teacher_username)['id']
    cursor.execute("INSERT INTO students (teacher_id, username, name, birthday, gender, password, email, usertype) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (teacher_id, username, name, birthday, gender, password, email, usertype))
    conn.commit()
    conn.close()


def load_student_data(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE username=?", (username,))
    student_data = cursor.fetchone()
    conn.close()
    if student_data:
        return {
            'username': student_data[1],
            'name': student_data[2],
            'birthday': student_data[3],
            'gender': student_data[4],
            'password': student_data[5],
            'email': student_data[6],
            'usertype': student_data[7]
        }
    else:
        return None

def load_student_posts(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_posts WHERE student_id=(SELECT id FROM students WHERE username=?)", (username,))
    posts = cursor.fetchall()
    conn.close()
    return [{'post': post[2], 'deadline': post[3]} for post in posts]

def load_student_todos(username):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student_todos WHERE student_id=(SELECT id FROM students WHERE username=?)", (username,))
    todos = cursor.fetchall()
    conn.close()
    return [{'task': todo[2], 'progress': todo[3], 'tags': todo[4]} for todo in todos]


def save_student_data(username, name, birthday, gender, password, email, usertype):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (username, name, birthday, gender, password, email, usertype) VALUES (?, ?, ?, ?, ?, ?, ?)", (username, name, birthday, gender, password, email, usertype))
