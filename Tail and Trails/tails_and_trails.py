# Sporsor by Raven , made by Maeven
# Tails and Trails: Pet Clinic
# Dona Palacios
# Raven Orlino
# John Godfdrey RoledaSS

import sys
import json
import random
import time
import os
import re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5 import uic

# Constants
PROGRAM_TITLE = "Tails and Trails: Pet Clinic"
ICON_PATH = os.path.join('ui', 'icon.ico')

def get_ui_path(filename):
    return os.path.join('ui', filename)

def get_sound_path(filename):
    return QUrl.fromLocalFile(os.path.abspath(os.path.join('sound', filename)))

def is_valid_name(name):
    pattern = r'^[A-Za-z\s\'\-\.]+$'
    return bool(re.match(pattern, name)) and len(name.strip()) > 0

class SoundManager:
    def __init__(self):
        self.bg_playlist = QMediaPlaylist()
        self.bg_playlist.addMedia(QMediaContent(get_sound_path('bgmusic.mp3')))
        self.bg_playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.bg_music = QMediaPlayer()
        self.bg_music.setPlaylist(self.bg_playlist)
        self.bg_music.setVolume(50)
        self.click_player = QMediaPlayer()
        self.click_player.setMedia(QMediaContent(get_sound_path('click.mp3')))
        self.click_player.setVolume(70)
        self.type_player = QMediaPlayer()
        self.type_player.setMedia(QMediaContent(get_sound_path('type.mp3')))
        self.type_player.setVolume(60)
    
    def start_background_music(self):
        self.bg_music.play()
    
    def play_click(self):
        self.click_player.setPosition(0)
        self.click_player.play()
    
    def play_type(self):
        self.type_player.setPosition(0)
        self.type_player.play()

class Queue:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.items = []
    
    def enqueue(self, item):
        if not self.isFull():
            self.items.append(item)
            return True
        return False
    
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        return None
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def isFull(self):
        return len(self.items) >= self.capacity

class tails_and_trails(QMainWindow):
    def __init__(self):
        super().__init__()
        self.general_queue = Queue()
        self.priority_queue = Queue()
        self.doctors = [
            "Dr. Raven Orlino (Room 1)",
            "Dr. Dona Palacios (Room 2)",
            "Dr. John Godfrey Roleda (Room 3)"
        ]
        self.current_page = None
        self.sound_manager = SoundManager()
        self.sound_manager.start_background_music()
        self.load_data()
        self.setup_window()
        self.show_page1()

    def setup_window(self):
        icon = QIcon(ICON_PATH)
        self.setWindowIcon(icon)
        app = QApplication.instance()
        app.setWindowIcon(icon)

    def load_data(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                self.general_queue.items = data.get('general_queue', [])
                self.priority_queue.items = data.get('priority_queue', [])
        except FileNotFoundError:
            self.paki_save_daw_sabi_ni_Raven()

    def paki_save_daw_sabi_ni_Raven(self):
        data = {
            'general_queue': self.general_queue.items,
            'priority_queue': self.priority_queue.items
        }
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def show_page1(self):
        self.current_page = uic.loadUi(get_ui_path('Page1.ui'))
        self.current_page.setWindowTitle(PROGRAM_TITLE)
        self.current_page.setWindowIcon(QIcon(ICON_PATH))
        self.setup_page1_buttons()
        self.current_page.show()

    def setup_page1_buttons(self):
        self.current_page.learnmore_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.show_page2()])
        self.current_page.GeneralQ_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.show_page3()])
        self.current_page.PriorityQ_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.show_page4()])
        self.current_page.BookAppoint_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.show_page8()])

    def show_page2(self):
        self.current_page = uic.loadUi(get_ui_path('Page2.ui'))
        self.current_page.setWindowTitle(PROGRAM_TITLE)
        self.current_page.setWindowIcon(QIcon(ICON_PATH))
        self.current_page.back_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.show_page1()])
        self.current_page.show()

    def show_page3(self):
        self.current_page = uic.loadUi(get_ui_path('Page3.ui'))
        self.current_page.setWindowTitle(PROGRAM_TITLE)
        self.current_page.setWindowIcon(QIcon(ICON_PATH))
        self.setup_page3()
        self.current_page.show()

    def setup_page3(self):
        self.current_page.forward_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.process_queue_entry('general')])
        self.current_page.back_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.show_page1()])
        self.current_page.enter_name_bar.textChanged.connect(
            self.sound_manager.play_type)
        self.current_page.enter_pet_name_bar.textChanged.connect(
            self.sound_manager.play_type)

    def show_page4(self):
        self.current_page = uic.loadUi(get_ui_path('Page4.ui'))
        self.current_page.setWindowTitle(PROGRAM_TITLE)
        self.current_page.setWindowIcon(QIcon(ICON_PATH))
        self.setup_page4()
        self.current_page.show()

    def setup_page4(self):
        self.current_page.forward_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.process_queue_entry('priority')])
        self.current_page.back_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.show_page1()])
        self.current_page.enter_name_bar.textChanged.connect(
            self.sound_manager.play_type)
        self.current_page.enter_pet_name_bar.textChanged.connect(
            self.sound_manager.play_type)

    def process_queue_entry(self, queue_type):
        owner_name = self.current_page.enter_name_bar.text().strip()
        pet_name = self.current_page.enter_pet_name_bar.text().strip()
        
        if not owner_name or not pet_name:
            QMessageBox.warning(self, "Input Error", "Please fill all fields")
            return
            
        if not is_valid_name(owner_name):
            QMessageBox.warning(self, "Input Error", "Please enter a valid name (letters only)")
            return
            
        self.temp_data = {
            'owner_name': owner_name,
            'pet_name': pet_name,
            'queue_type': queue_type
        }
        self.show_page5()

    def show_page5(self):
        self.current_page = uic.loadUi(get_ui_path('Page5.ui'))
        self.current_page.setWindowTitle(PROGRAM_TITLE)
        self.current_page.setWindowIcon(QIcon(ICON_PATH))
        self.setup_page5()
        self.current_page.show()

    def setup_page5(self):
        self.current_page.forward_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.process_page5()])
        self.current_page.back_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), 
                    self.show_page3() if self.temp_data['queue_type'] == 'general' 
                    else self.show_page4()])
        self.current_page.enterbreed_bar.textChanged.connect(
            self.sound_manager.play_type)
        self.current_page.pet_concer_bar.textChanged.connect(
            self.sound_manager.play_type)

    def process_page5(self):
        breed = self.current_page.enterbreed_bar.text().strip()
        concerns = self.current_page.pet_concer_bar.text().strip()
        if not breed or not concerns:
            QMessageBox.warning(self, "Input Error", "Please fill all fields")
            return
        queue_entry = {
            'owner_name': self.temp_data['owner_name'],
            'pet_name': self.temp_data['pet_name'],
            'breed': breed,
            'concerns': concerns,
            'room': random.choice(self.doctors)
        }
        if self.temp_data['queue_type'] == 'general':
            self.general_queue.enqueue(queue_entry)
        else:
            self.priority_queue.enqueue(queue_entry)
        self.paki_save_daw_sabi_ni_Raven()
        self.show_page6()

    def show_page6(self):
        self.current_page = uic.loadUi(get_ui_path('Page6.ui'))
        self.current_page.setWindowTitle(PROGRAM_TITLE)
        self.current_page.setWindowIcon(QIcon(ICON_PATH))
        self.setup_page6()
        self.current_page.show()

    def setup_page6(self):
        current_queue = (self.priority_queue if self.temp_data['queue_type'] == 'priority' 
                        else self.general_queue)
        
        queue_number = len(current_queue.items)
        self.current_page.queue_lbl.setText(f"{queue_number}")
        self.current_page.attend_lbl.setText(
            f"{current_queue.items[-1]['room']}")
        next_in_line = current_queue.peek()
        next_text = (f"{next_in_line['owner_name']}" 
                    if next_in_line else "None")
        self.current_page.nextinline_lbl.setText(next_text)
        self.current_page.forward_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.show_page7()])
        self.current_page.back_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.show_page5()])

    def show_page7(self):
        self.current_page = uic.loadUi(get_ui_path('Page7.ui'))
        self.current_page.setWindowTitle(PROGRAM_TITLE)
        self.current_page.setWindowIcon(QIcon(ICON_PATH))
        QTimer.singleShot(2000, self.show_page1)
        self.current_page.show()

    def show_page8(self):
        self.current_page = uic.loadUi(get_ui_path('Page8.ui'))
        self.current_page.setWindowTitle(PROGRAM_TITLE)
        self.current_page.setWindowIcon(QIcon(ICON_PATH))
        self.setup_page8()
        self.current_page.show()

    def setup_page8(self):
        with open('table_style.qss', 'r') as f:
            style = f.read()
        self.current_page.general_tbl.setStyleSheet(style)
        self.current_page.priority_tbl.setStyleSheet(style)
        for table in [self.current_page.general_tbl, self.current_page.priority_tbl]:
            table.setShowGrid(True)
            table.setAlternatingRowColors(True)
            table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            table.verticalHeader().setVisible(False)
            table.setSelectionBehavior(QTableWidget.SelectRows)
            table.setSelectionMode(QTableWidget.SingleSelection)
        self.update_table(self.current_page.general_tbl, self.general_queue.items)
        self.update_table(self.current_page.priority_tbl, self.priority_queue.items)
        self.current_page.back_btn.clicked.connect(
            lambda: [self.sound_manager.play_click(), self.show_page1()])

    def update_table(self, table, items):
        table.setRowCount(len(items))
        for row, item in enumerate(items):
            table.setItem(row, 0, QTableWidgetItem(item['owner_name']))
            table.setItem(row, 1, QTableWidgetItem(
                f"{item['pet_name']} ({item['breed']})"))
            table.setItem(row, 2, QTableWidgetItem(item['room']))
            table.setItem(row, 3, QTableWidgetItem(item['concerns']))

# Sporsor by Raven , made by Maeven

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName(PROGRAM_TITLE)
    window = tails_and_trails()
    sys.exit(app.exec_())