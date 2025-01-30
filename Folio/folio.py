# Folio
# By: Amador, Javier, Roleda & Tapa
# BET-CPET-2A

Folio_logo = """  
############################################################################
############################################################################
############################################################################
############################################################################
#######################*+==========#############+*##########################
###################*=========+++==+###########+==*##########################
###################===*#########+=###########++#+###+==#####################
##################+=+**########++###########=+*=####**######################
##############################==####*===+##+=*+###*==###*====*##############
########################*++++==+*#*===*==**==*##*==+##*===*+=+##############
######################=======++##*=+##+=+#==####==*###==*#*==*##############
#########################*=+#####*=*##+==+==*#++==*#=+=+##*==+##############
#######################*+=*#######*===*###*==+##*==+##*===*#################
####################*===*###################################################
###################+==*#####################################################
############################################################################
############################################################################
############################################################################
"""


import sys
import os
import json
import shutil
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QStackedWidget, QFileDialog, QMessageBox, QTreeView, QFileSystemModel, QListWidgetItem)
from PyQt5.QtCore import QDateTime, Qt, QDate, QEvent, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtGui import QTextCharFormat, QBrush, QColor
from PyQt5 import uic

def create_media_player():
    player = QMediaPlayer()
    return player


SOUND_PLAYER = create_media_player()


def play_sound(sound_name):
    try:
        sound_file = os.path.join(os.path.dirname(__file__), 'sfx', f'{sound_name}.mp3')
        SOUND_PLAYER.setMedia(QMediaContent(QUrl.fromLocalFile(sound_file)))
        SOUND_PLAYER.play()
    except Exception as e:
        print(f"Error playing sound {sound_name}: {e}")

HOME_UI = "ui/folio_home.ui"
MAIN_UI = "ui/folio_main.ui"

DEFAULT_HOME_UI = "ui/folio_home.ui"
AMADOR_HOME_UI = "ui/folio_home_amador.ui"
PRINCE_HOME_UI = "ui/folio_home_prince.ui"
JAY_HOME_UI = "ui/folio_home_jay.ui"

DEFAULT_MAIN_UI = "ui/folio_main.ui"
AMADOR_MAIN_UI = "ui/folio_main_amador.ui"
PRINCE_MAIN_UI = "ui/folio_main_prince.ui"
JAY_MAIN_UI = "ui/folio_main_jay.ui"
DATA_FILE = "data.json"
FILES_DIR = "files\\"

class ScheduleTreeNode:
    def __init__(self, task):
        self.task = task
        self.left = None
        self.right = None

class ScheduleBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, task, key):
        new_node = ScheduleTreeNode(task)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_recursive(self.root, new_node, key)

    def _insert_recursive(self, current, new_node, key):
        if key(new_node.task) < key(current.task):
            if current.left is None:
                current.left = new_node
            else:
                self._insert_recursive(current.left, new_node, key)
        else:
            if current.right is None:
                current.right = new_node
            else:
                self._insert_recursive(current.right, new_node, key)

    def build_tree(self, tasks, key=lambda x: x['datetime']):
        self.root = None  
        for task in tasks:
            self.insert(task, key)

    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.task)
            self.in_order_traversal(node.right, result)
        return result


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class FullBinaryTree:
    def __init__(self):
        self.root = None
        self.nodes = []

    def build_tree(self, files):
        self.nodes = [BinaryTreeNode(file) for file in files]
        n = len(self.nodes)
        for i in range(n):
            if 2 * i + 1 < n:
                self.nodes[i].left = self.nodes[2 * i + 1]
            if 2 * i + 2 < n:
                self.nodes[i].right = self.nodes[2 * i + 2]
        self.root = self.nodes[0] if self.nodes else None

    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.value)
            self.in_order_traversal(node.right, result)
        return result

if not os.path.exists(FILES_DIR):
    os.makedirs(FILES_DIR)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump({"tasks": [], "files": []}, f)
        

def load_data():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        if 'theme' not in data:
            data['theme'] = 'default'
            save_data(data)
        return data

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

class Folio(QMainWindow):
    def __init__(self):
        super().__init__()
        data = load_data()
        current_theme = data.get('theme', 'default')
        home_ui_map = {
            'default': HOME_UI,
            'amador': AMADOR_HOME_UI,
            'prince': PRINCE_HOME_UI,
            'jay': JAY_HOME_UI
        }
        uic.loadUi(home_ui_map.get(current_theme, HOME_UI), self)
        self.setWindowTitle("Folio")
        self.home_stackedwidget.setCurrentWidget(self.home_page_1)
        self.theme_btn.clicked.connect(lambda: [play_sound('button'), self.change_theme('default')])
        self.theme1_btn.clicked.connect(lambda: [play_sound('button'), self.change_theme('amador')])
        self.theme2_btn.clicked.connect(lambda: [play_sound('button'), self.change_theme('prince')])
        self.theme3_btn.clicked.connect(lambda: [play_sound('button'), self.change_theme('jay')])
        self.home_stackedwidget.setCurrentWidget(self.home_page_1)
        self.continue_btn.installEventFilter(self)
        self.continue_btn.clicked.connect(lambda: [play_sound('button'), self.launch_main()])
        self.faqs_btn.clicked.connect(lambda: [play_sound('button'),self.home_stackedwidget.setCurrentWidget(self.home_page_2)])
        self.home_btn.clicked.connect(lambda: [play_sound('button'),self.home_stackedwidget.setCurrentWidget(self.home_page_1)])
        self.max_btn.clicked.connect(self.toggle_maximize)
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.is_dragging = False
        self.drag_start_position = None
        self.is_maximized = False
        self.normal_geometry = self.geometry()

    def eventFilter(self, obj, event):
        if obj == self.continue_btn:
            if event.type() == QEvent.HoverEnter:
                self.continue_btn.setText("Continue")  # Change text when hovering
            elif event.type() == QEvent.HoverLeave:
                self.continue_btn.setText("Folio")  # Revert text when not hovering
        return super().eventFilter(obj, event)

    def change_theme(self, theme):
        data = load_data()
        if data['theme'] == theme:
            QMessageBox.information(self, "Theme Selection", f"{theme.capitalize()} theme is already selected.")
            return
        data['theme'] = theme
        save_data(data)
        QApplication.instance().setStyleSheet(get_message_box_style(theme))  # Update stylesheet
        QMessageBox.information(self, "Theme Change", f"Theme changed to {theme.capitalize()}. The application will restart.")
        self.close()
        new_window = Folio()
        play_sound('chime')
        new_window.show()

    def toggle_maximize(self):
        if not self.is_maximized:
            self.normal_geometry = self.geometry()
            self.showMaximized()
            self.is_maximized = True
        else:
            self.showNormal()
            self.setGeometry(self.normal_geometry)
            self.is_maximized = False

    def launch_main(self):
        self.main_window = FolioMain()
        self.main_window.show()
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if not self.is_maximized:
                self.is_dragging = True
                self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.is_dragging and not self.is_maximized:
            self.move(event.globalPos() - self.drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False
            event.accept()

class FolioMain(QMainWindow):
    def __init__(self):
        super().__init__()
        data = load_data()
        current_theme = data.get('theme', 'default')
        main_ui_map = {
            'default': MAIN_UI,
            'amador': AMADOR_MAIN_UI,
            'prince': PRINCE_MAIN_UI,
            'jay': JAY_MAIN_UI
        }
        uic.loadUi(main_ui_map.get(current_theme, MAIN_UI), self)
        self.setWindowTitle("Folio")
        self.main_stackwidget.setCurrentWidget(self.page_1)
        self.schedule_btn.clicked.connect(lambda: [play_sound('button'),self.main_stackwidget.setCurrentWidget(self.page_1), self.update_button_styles(self.schedule_btn)])
        self.fm_btn.clicked.connect(lambda: [play_sound('button'),self.main_stackwidget.setCurrentWidget(self.page_2), self.update_button_styles(self.fm_btn)])
        self.quit_btn.clicked.connect(lambda: [play_sound('button'), self.return_home()])
        self.max_btn.clicked.connect(self.toggle_maximize)
        self.min_btn.clicked.connect(self.showMinimized)
        self.close_btn.clicked.connect(self.close)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.is_dragging = False
        self.drag_start_position = None
        self.is_maximized = False
        self.normal_geometry = self.geometry()
        self.init_schedule_manager()
        self.init_file_manager()
        self.update_button_styles(self.schedule_btn)
        self.center_window()

    def center_window(self):
        screen = QApplication.desktop().screenGeometry()
        window_size = self.geometry()
        center_x = (screen.width() - window_size.width()) // 2
        center_y = (screen.height() - window_size.height()) // 2
        self.move(center_x, center_y)

    def update_button_styles(self, selected_button):
        self.schedule_btn.setStyleSheet("font-family: Arial; font-weight: normal; border: none;")
        self.fm_btn.setStyleSheet("font-family: Arial; font-weight: normal; border: none;")
        selected_button.setStyleSheet("font-family: Arial Black; font-weight: bold; border: none;")

    def toggle_maximize(self):
        if not self.is_maximized:
            self.normal_geometry = self.geometry()
            self.showMaximized()
            self.is_maximized = True
        else:
            self.showNormal()
            self.setGeometry(self.normal_geometry)
            self.is_maximized = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if not self.is_maximized:
                self.is_dragging = True
                self.drag_start_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self.is_dragging and not self.is_maximized:
            self.move(event.globalPos() - self.drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False
            event.accept()

    def return_home(self):
        self.home_window = Folio()
        self.home_window.show()
        self.close()

    ##########################
    # Schedule Manager (Page 1)
    ##########################
    def init_schedule_manager(self):
        self.sched_add_btn.clicked.connect(lambda: [play_sound('button'), self.add_schedule()])
        self.sched_sort_btn.clicked.connect(lambda: [play_sound('button'), self.sort_schedule()])
        self.sched_del_btn.clicked.connect(lambda: [play_sound('button'), self.delete_schedule()])
        self.sched_edit_btn.clicked.connect(lambda: [play_sound('button'), self.edit_schedule()])
        self.guide1_btn.clicked.connect(lambda: [play_sound('button'), self.go_to_guide_page()])
        self.guide1_back_btn.clicked.connect(lambda: [play_sound('button'), self.return_to_page_1()])
        self.sched_list_wdgt.itemChanged.connect(self.mark_done)
        self.sched_search_box.textChanged.connect(self.filter_sched_list)
        self.load_schedules()

    def load_schedules(self):
        data = load_data()
        tasks = data['tasks']
        self.sched_list_wdgt.clear()
        for task in tasks:
            item = QListWidgetItem(f"{task['name']} - {task['datetime']}")
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Checked if task['status'] == 'done' else Qt.Unchecked)
            self.sched_list_wdgt.addItem(item)
        self.highlight_unchecked_dates()

    def edit_schedule(self):
        selected_items = self.sched_list_wdgt.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Edit Error", "Please select a task to edit.")
            return
        if len(selected_items) > 1:
            QMessageBox.warning(self, "Edit Error", "Please select only one task to edit.")
            return
        selected_item = selected_items[0]
        task_text = selected_item.text()
        data = load_data()
        for task in data['tasks']:
            if f"{task['name']} - {task['datetime']}" == task_text:
                self.sched_task_box.setText(task['name'])
                self.sched_datetimeedit.setDateTime(QDateTime.fromString(task['datetime'], "yyyy-MM-dd HH:mm"))
                data['tasks'].remove(task)
                save_data(data)
                self.load_schedules()
                break

    def add_schedule(self):
        name = self.sched_task_box.text().strip()
        datetime = self.sched_datetimeedit.dateTime().toString("yyyy-MM-dd HH:mm")
        if not name:
            QMessageBox.warning(self, "Invalid Input", "Task name cannot be empty.")
            return
        data = load_data()
        for task in data['tasks']:
            if task['name'] == name and task['datetime'] == datetime:
                QMessageBox.warning(self, "Duplicate Task", "A task with the same name and time already exists.")
                return
        new_task = {"name": name, "datetime": datetime, "status": "pending"}
        tree = ScheduleBinaryTree()
        tree.build_tree(data['tasks'] + [new_task])
        data['tasks'] = tree.in_order_traversal(tree.root)
        save_data(data)
        self.load_schedules()
        self.sched_task_box.clear()

    def filter_sched_list(self):
        search_text = self.sched_search_box.text().lower()  
        self.sched_list_wdgt.clear()  
        data = load_data() 
        if not data['tasks']:
            QMessageBox.information(self, "Why Searching", "Please add a schedule first before finding something.")
            self.sched_task_box.setFocus()
            return 
        for task in data['tasks']:
            task_name = task['name'].lower()
            task_datetime = task['datetime'].lower()
            task_status = task['status']  
            if search_text in task_name or search_text in task_datetime:
                item_text = f"{task['name']} - {task['datetime']}"
                item = QListWidgetItem(item_text)
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                item.setCheckState(Qt.Checked if task_status == 'done' else Qt.Unchecked)
                self.sched_list_wdgt.addItem(item)

    def sort_schedule(self):
        data = load_data()
        if not data['tasks']:
            QMessageBox.information(self, "No Schedule", "Please add a schedule first before sorting.")
            self.sched_task_box.setFocus()
            return
        criteria = self.sched_sort_box.currentText()
        if criteria == "By Name:":
            sort_key = lambda x: x['name']
        elif criteria == "By Date/Time:":
            sort_key = lambda x: x['datetime']
        elif criteria == "By Status:":
            sort_key = lambda x: x['status']
        else:
            QMessageBox.warning(self, "Invalid Sort", "Unknown sort criteria.")
            return
        tree = ScheduleBinaryTree()
        tree.build_tree(data['tasks'], key=sort_key)
        sorted_tasks = tree.in_order_traversal(tree.root)
        data['tasks'] = sorted_tasks
        save_data(data)
        self.load_schedules()

        
    def delete_schedule(self):
        data = load_data()
        if not data['tasks']:
            QMessageBox.information(self, "No Schedule", "Please add a schedule first before deleting something.")
            self.sched_task_box.setFocus()
            return
        for item in self.sched_list_wdgt.selectedItems():
            task_text = item.text()
            data = load_data()
            data['tasks'] = [task for task in data['tasks'] if f"{task['name']} - {task['datetime']}" != task_text]
            save_data(data)
            self.load_schedules()

    def highlight_unchecked_dates(self):
        calendar = self.sched_calendar_wdgt
        unchecked_dates = []
        for index in range(self.sched_list_wdgt.count()):
            item = self.sched_list_wdgt.item(index)
            if item.checkState() == Qt.Unchecked:
                task_text = item.text()
                try:
                    date_str = task_text.split(' - ')[1].split()[0] 
                    task_date = QDate.fromString(date_str, "yyyy-MM-dd")
                    unchecked_dates.append(task_date)
                except IndexError:
                    continue  
        calendar.setDateTextFormat(QDate(), QTextCharFormat())
        highlight_format = QTextCharFormat()
        highlight_format.setBackground(QBrush(QColor("#6B6C76")))  
        for date in unchecked_dates:
            calendar.setDateTextFormat(date, highlight_format)

    def mark_done(self, item):
        data = load_data()
        for task in data['tasks']:
            if f"{task['name']} - {task['datetime']}" == item.text():
                task['status'] = 'done' if item.checkState() == Qt.Checked else 'pending'
        save_data(data)
        self.load_schedules()
        self.highlight_unchecked_dates()  

    def go_to_guide_page(self):
        self.main_stackwidget.setCurrentWidget(self.page_3)

    def return_to_page_1(self):
        self.main_stackwidget.setCurrentWidget(self.page_1)




    ##########################
    # File Manager (Page 2)
    ##########################
    def init_file_manager(self):
        self.file_tree = FullBinaryTree()
        files = [f for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]
        self.file_tree.build_tree(files)
        self.display_files_as_tree()
        self.fm_add_btn.clicked.connect(lambda: [play_sound('button'), self.add_file()])
        self.fm_del_btn.clicked.connect(lambda: [play_sound('button'), self.delete_file()])
        self.fm_open_btn.clicked.connect(lambda: [play_sound('button'), self.open_file()])
        self.fm_sort_btn.clicked.connect(lambda: [play_sound('button'), self.sort_files()])
        self.guide2_btn.clicked.connect(lambda: [play_sound('button'), self.go_to_guide_page4()])
        self.guide2_back_btn.clicked.connect(lambda: [play_sound('button'), self.return_to_page_2()])
        self.fm_openfolder_btn.clicked.connect(lambda: [play_sound('button'), self.open_folder_and_select_file()])
        self.fm_search_box.textChanged.connect(self.search_files)

    def display_files_as_tree(self):
        def recursive_add(node):
            if node:
                file_path = os.path.join(FILES_DIR, node.value)
                if os.path.exists(file_path):
                    file_name, file_extension = os.path.splitext(node.value)
                    save_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
                    formatted_data = f"{file_name}{file_extension} - {save_time}"
                    item = QListWidgetItem(formatted_data)
                    item.setData(Qt.UserRole, node.value) 
                    self.fm_listwidget.addItem(item)
                recursive_add(node.left)
                recursive_add(node.right)
        self.fm_listwidget.clear()
        recursive_add(self.file_tree.root)

    def add_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Add File")
        if file_path:
            original_filename = os.path.basename(file_path)
            filename, extension = os.path.splitext(original_filename)
            dest_path = os.path.join(FILES_DIR, original_filename)
            counter = 1
            while os.path.exists(dest_path):
                new_filename = f"{filename} ({counter}){extension}"
                dest_path = os.path.join(FILES_DIR, new_filename)
                counter += 1
            shutil.copy(file_path, dest_path)
            files = [f for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]
            self.file_tree.build_tree(files)
            self.display_files_as_tree()

    def delete_file(self):
        files = [f for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]
        if not files:
            QMessageBox.information(self, "No Files", "Why will you something if you don't have one?")
            self.add_file()
            return
        selected_item = self.fm_listwidget.currentItem()
        if selected_item:
            file_name = selected_item.data(Qt.UserRole)  
            file_path = os.path.join(FILES_DIR, file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
                files = [f for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]
                self.file_tree.build_tree(files)
                self.display_files_as_tree()

    def open_folder_and_select_file(self):
        selected_item = self.fm_listwidget.currentItem()
        if selected_item:
            file_name = selected_item.data(Qt.UserRole)
            file_path = os.path.join(FILES_DIR, file_name)
            if os.path.exists(file_path):
                import subprocess
                subprocess.run(f'explorer /select,"{file_path}"', shell=True)
            else:
                QMessageBox.warning(self, "File Not Found", f"The file {file_name} no longer exists.")
        else:
            QMessageBox.warning(self, "No File Selected", "Please select a file first.")

    def open_file(self):
        files = [f for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]
        if not files:
            QMessageBox.information(self, "No Files", "Why open one if you don't have one?")
            self.add_file()
            return
        selected_item = self.fm_listwidget.currentItem()
        if selected_item:
            file_name = selected_item.data(Qt.UserRole)  
            file_path = os.path.join(FILES_DIR, file_name)
            if os.path.exists(file_path):
                os.startfile(file_path)

    def search_files(self):
        files = [f for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]
        if not files:
            QMessageBox.information(self, "No Files to search", "Why will you search if you dont have file yet.")
            self.add_file()
            return
        search_text = self.fm_search_box.text().strip().lower()  
        for i in range(self.fm_listwidget.count()):  
            item = self.fm_listwidget.item(i)  
            item.setHidden(search_text not in item.text().lower())

    def sort_files(self):
        files = [f for f in os.listdir(FILES_DIR) if os.path.isfile(os.path.join(FILES_DIR, f))]
        if not files:
            QMessageBox.information(self, "No Files", "Please add files first before sorting.")
            self.add_file()
            return
        criteria = self.fm_sort_box.currentText()
        if criteria == "By Name:":
            files.sort()
        elif criteria == "By Type:":
            files.sort(key=lambda x: os.path.splitext(x)[1])
        elif criteria == "By Date:":
            files.sort(key=lambda x: os.path.getmtime(os.path.join(FILES_DIR, x)))
        self.file_tree.build_tree(files)
        self.display_files_as_tree()

    def go_to_guide_page4(self):
        self.main_stackwidget.setCurrentWidget(self.page_4)

    def return_to_page_2(self):
        self.main_stackwidget.setCurrentWidget(self.page_2)

def get_message_box_style(theme='default'):
    if theme == 'default':
        return """
            QMessageBox {
                background-color: #2b2b2b; 
                color: white; 
                font-size: 14px; 
                border: 1px solid #444444; 
            }
            QMessageBox QLabel {
                color: white; 
            }
            QMessageBox QPushButton {
                background-color: #444444; 
                color: white; 
                border: 1px solid #888888; 
                padding: 5px;
                border-radius: 3px;
            }
            QMessageBox QPushButton:hover {
                background-color: #666666;
            }
        """
    else:  
        return """
            QMessageBox {
                background-color: white; 
                color: black; 
                font-size: 14px; 
                border: 1px solid #444444; 
            }
            QMessageBox QLabel {
                color: black; 
            }
            QMessageBox QPushButton {
                background-color: #444444; 
                color: black; 
                border: 1px solid #888888; 
                padding: 5px;
                border-radius: 3px;
            }
            QMessageBox QPushButton:hover {
                background-color: #666666;
            }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    data = load_data()
    current_theme = data.get('theme', 'default')
    app.setStyleSheet(get_message_box_style(current_theme))
    window = Folio()
    window.show()
    print(Folio_logo)
    play_sound('chime')
    sys.exit(app.exec_())
