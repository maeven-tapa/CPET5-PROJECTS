import sys
import random
import json
import time
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, QTimer

# Paths to resources
MUSIC_PATH = "resource/music.mp3"
DATA_FILE = "data.json"


try:
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    data = {"users": {}, "leaderboard": []}
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Helper functions
def load_words():
    categories = {
        "space": ["stars", "orbit", "comet", "pluto", "alien"],
        "technology": ["robot", "laser", "phone", "chips", "apple"],
        "mythology": ["hydra", "zeus", "hera", "apollo", "venus"],
        "color": ["white", "black", "green", "blue", "brown"],
        "job": ["actor", "nurse", "pilot", "judge", "coach"],
        "fruits": ["mango", "apple", "berry", "peach", "grape"],
        "animal": ["horse", "tiger", "shark", "zebra", "eagle"],
        "sports": ["tenis", "golf", "rugby", "hockey", "crick"],
    }
    return categories

class LeaderboardDialog(QtWidgets.QDialog):
    def __init__(self, parent, leaderboard_data):
        super().__init__(parent)
        uic.loadUi("leaderboard.ui", self)
        self.leaderboard_data = leaderboard_data if leaderboard_data else []
        print(f"Leaderboard data: {self.leaderboard_data}")
        self.populate_leaderboard()
        self.back_btn.clicked.connect(self.close)
        self.search_box.textChanged.connect(self.search_leaderboard)

    def populate_leaderboard(self):
        self.leaderboard_tbl.setRowCount(0)
        self.leaderboard_tbl.setRowCount(len(self.leaderboard_data))
        for row, entry in enumerate(self.leaderboard_data):
            name = entry.get('name', 'Unknown')
            score = str(entry.get('score', 0))
            time_played = entry.get('time', 'N/A')
            self.leaderboard_tbl.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
            self.leaderboard_tbl.setItem(row, 1, QtWidgets.QTableWidgetItem(score))
            self.leaderboard_tbl.setItem(row, 2, QtWidgets.QTableWidgetItem(time_played))
        self.leaderboard_tbl.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    def search_leaderboard(self):
        search_term = self.search_box.text().strip().lower()
        
        if not search_term:
            self.populate_leaderboard()
            return
        filtered_data = [
            entry for entry in self.leaderboard_data 
            if search_term in entry['name'].lower()
        ]
        if not filtered_data:
            QtWidgets.QMessageBox.information(
                self, 
                "Search Result", 
                f"No players found matching '{search_term}'."
            )
            self.populate_leaderboard()
            return
        self.leaderboard_tbl.setRowCount(0)
        self.leaderboard_tbl.setRowCount(len(filtered_data))
        
        for row, entry in enumerate(filtered_data):
            name = entry.get('name', 'Unknown')
            score = str(entry.get('score', 0))
            time_played = entry.get('time', 'N/A')
            self.leaderboard_tbl.setItem(row, 0, QtWidgets.QTableWidgetItem(name))
            self.leaderboard_tbl.setItem(row, 1, QtWidgets.QTableWidgetItem(score))
            self.leaderboard_tbl.setItem(row, 2, QtWidgets.QTableWidgetItem(time_played))

    def jump_search(self, data, target):
        n = len(data)
        step = int(n**0.5)  
        prev = 0
        while prev < n and data[min(step, n) - 1]['name'].lower() < target:
            prev = step
            step += int(n**0.5)
            if prev >= n:
                return None
        for i in range(prev, min(step, n)):
            if data[i]['name'].lower() == target:
                return i
        return None

    def highlight_row(self, name):
        self.populate_leaderboard()
        for row in range(self.leaderboard_tbl.rowCount()):
            item = self.leaderboard_tbl.item(row, 0)  
            if item and item.text().strip().lower() == name.strip().lower():
                self.leaderboard_tbl.selectRow(row) 
                break


# Main Application
class WordleGame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.words = load_words()
        self.current_word = ""
        self.selected_category = ""
        self.name = ""
        self.password = ""
        self.score = 0
        self.music_on = True
        self.init_ui()
        self.setup_music()

    def init_ui(self):
        uic.loadUi("start.ui", self)
        self.play_btn.clicked.connect(self.open_credentials)
        self.music_btn.clicked.connect(self.toggle_music)
        self.leaderboard_btn.clicked.connect(self.show_leaderboard)

    def show_start_ui(self):

        self.init_ui()
        self.show()

    def show_category_ui(self):

        category_window = CategoryWindow(self)
        category_window.show()
        
    def setup_music(self):
        self.music_player = QMediaPlayer()
        self.music_player.setMedia(QMediaContent(QUrl.fromLocalFile(MUSIC_PATH)))
        self.music_player.play()

    def show_leaderboard(self):
        sorted_leaderboard = sorted(
            data.get("leaderboard", []), 
            key=lambda x: x['score'], 
            reverse=True
        )
        
        leaderboard_dialog = LeaderboardDialog(self, sorted_leaderboard)
        leaderboard_dialog.exec_()

    def toggle_music(self):
        if self.music_on:
            self.music_player.pause()
            self.music_btn.setText("Music FX: Off")
        else:
            self.music_player.play()
            self.music_btn.setText("Music FX: On")
        self.music_on = not self.music_on

    def open_credentials(self):
        dialog = CredentialsDialog(self)
        dialog.exec_()

    def start_game(self, category):
        self.selected_category = category
        word_list = self.words[category]  # Get the word list for the selected category
        game_window = GameWindow(self, category, word_list)  # Pass category and word_list
        game_window.show()
        self.close()

class CredentialsDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        uic.loadUi("credentials.ui", self)
        self.parent = parent
        self.back_btn.clicked.connect(self.close)
        self.continue_btn.clicked.connect(self.handle_continue)

    def handle_continue(self):
        name = self.name_box.text().strip()
        password = self.pass_box.text().strip()
        if not name:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Name cannot be empty!")
            return
        one_time_play = not bool(password)
        if password:
            if name in data["users"] and data["users"][name]["password"] == password:
                self.parent.score = data["users"][name]["score"]
            elif name in data["users"]:
                QtWidgets.QMessageBox.warning(self, "Invalid Credentials", "Incorrect password!")
                return
            else:
                data["users"][name] = {"password": password, "score": 0}
        elif name not in data["users"]:
            self.parent.score = 0

        self.parent.name = name
        self.parent.password = password
        self.parent.one_time_play = one_time_play
        self.save_data()
        self.close()
        category_window = CategoryWindow(self.parent)
        category_window.show()

    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(data, file)


class CategoryWindow(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi("category.ui", self)
        self.parent = parent
        self.tech_btn.clicked.connect(lambda: self.start_game("technology"))
        self.space_btn.clicked.connect(lambda: self.start_game("space"))
        self.color_btn.clicked.connect(lambda: self.start_game("color"))
        self.fruits_btn.clicked.connect(lambda: self.start_game("fruits"))
        self.animal_btn.clicked.connect(lambda: self.start_game("animal"))
        self.jobs_btn.clicked.connect(lambda: self.start_game("job"))
        self.myth_btn.clicked.connect(lambda: self.start_game("mythology"))
        self.sports_btn.clicked.connect(lambda: self.start_game("sports"))
        self.back_btn.clicked.connect(self.go_back)
        self.music_btn.clicked.connect(self.parent.toggle_music)

    def go_back(self):
        self.close()
        self.parent.show()

    def start_game(self, category):
        self.parent.selected_category = category
        self.parent.start_game(category)
        self.close()

class GameWindow(QtWidgets.QMainWindow):
    def __init__(self, parent, category, word_list):
        super().__init__()
        uic.loadUi("main.ui", self)

        self.parent = parent
        self.category = category
        self.word_list = word_list
        self.target_word = random.choice(self.word_list).upper() 
        self.current_row = 0
        self.current_col = 0  
        self.entered_words = []  
        self.start_time = time.time()  
        self.init_keyboard()
        self.update_timer()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)
        self.backspace_btn.clicked.connect(self.handle_backspace)
        self.enter_btn.clicked.connect(self.handle_enter)
        self.back_btn.clicked.connect(self.go_back)

    def init_keyboard(self):
        keyboard_buttons = [
            self.q_btn, self.w_btn, self.e_btn, self.r_btn, self.t_btn, self.y_btn,
            self.u_btn, self.i_btn, self.o_btn, self.p_btn, self.a_btn, self.s_btn,
            self.d_btn, self.f_btn, self.g_btn, self.h_btn, self.j_btn, self.k_btn,
            self.l_btn, self.z_btn, self.x_btn, self.c_btn, self.v_btn, self.b_btn,
            self.n_btn, self.m_btn
        ]
        for btn in keyboard_buttons:
            btn.clicked.connect(lambda _, b=btn: self.handle_key_input(b.text().upper()))

    def handle_key_input(self, letter):
        if self.current_col < 5:  
            label_name = f"row{self.current_row + 1}_col{self.current_col + 1}_lbl"
            label = self.findChild(QtWidgets.QLabel, label_name)
            if label:
                label.setText(letter)
                self.current_col += 1

    def handle_backspace(self):
        """Handle backspace key."""
        if self.current_col > 0: 
            self.current_col -= 1
            label_name = f"row{self.current_row + 1}_col{self.current_col + 1}_lbl"
            label = self.findChild(QtWidgets.QLabel, label_name)
            if label:
                label.clear()

    def handle_enter(self):
        if self.current_col < 5:  
            QtWidgets.QMessageBox.warning(self, "Incomplete Word", "Complete the row before submitting!")
            return
        entered_word = "".join(
            self.findChild(QtWidgets.QLabel, f"row{self.current_row + 1}_col{i + 1}_lbl").text()
            for i in range(5)
        )
        self.entered_words.append(entered_word)

        if entered_word == self.target_word:
            self.end_game(True)
            return

        # Highlight letters
        for i, char in enumerate(entered_word):
            label_name = f"row{self.current_row + 1}_col{i + 1}_lbl"
            label = self.findChild(QtWidgets.QLabel, label_name)
            if char == self.target_word[i]:
                label.setStyleSheet(
                    "border-radius: 33px; background-color: rgb(170, 255, 127); "
                    "border: 2px solid rgb(198, 201, 204); font: 18pt 'Franklin Gothic Heavy';"
                )
            elif char in self.target_word:
                label.setStyleSheet(
                    "border-radius: 33px; background-color: rgb(255, 228, 87); "
                    "border: 2px solid rgb(198, 201, 204); font: 18pt 'Franklin Gothic Heavy';"
                )
            else:
                label.setStyleSheet(
                    "border-radius: 33px; background-color: rgb(211, 214, 218); "
                    "border: 2px solid rgb(198, 201, 204); font: 18pt 'Franklin Gothic Heavy';"
                )
        self.current_row += 1
        self.current_col = 0
        if self.current_row == 6:
            self.end_game(False)

    def update_timer(self):
        elapsed_time = time.time() - self.start_time
        self.time_lbl.setText(time.strftime("%M:%S", time.gmtime(elapsed_time)))

    def end_game(self, won):
        self.timer.stop()
        dialog = QtWidgets.QDialog(self)
        uic.loadUi("game_notif.ui", dialog)
        elapsed_time = time.time() - self.start_time
        time_taken = time.strftime("%M:%S", time.gmtime(elapsed_time))
        if won:
            notif_text = f"You Win! You took {time_taken} to finish the game."
            self.parent.score += 1
            if not self.parent.one_time_play:
                data["users"][self.parent.name]["score"] = self.parent.score
            leaderboard_entry = {
                "name": self.parent.name if self.parent.name else "Anonymous",
                "score": self.parent.score,
                "time": time_taken
            }
            existing_entry = next(
                (entry for entry in data.get("leaderboard", []) 
                if entry["name"] == leaderboard_entry["name"]), 
                None
            )
            if existing_entry:
                if leaderboard_entry["score"] > existing_entry["score"]:
                    existing_entry.update(leaderboard_entry)
            else:
                if "leaderboard" not in data:
                    data["leaderboard"] = []
                data["leaderboard"].append(leaderboard_entry)
            with open(DATA_FILE, "w") as file:
                json.dump(data, file)
        else:
            notif_text = f"You Lose! The correct word was {self.target_word}. It took you {time_taken}."

        dialog.notif_lbl.setText(notif_text)
        dialog.word_lbl.setText(self.target_word)

        # Handle back button
        dialog.back_btn.clicked.connect(self.handle_game_end)
        dialog.exec_()

    def handle_game_end(self):
        dialog = self.sender().parent() 
        dialog.close()
        self.close()
        
        if self.parent.one_time_play:
            self.parent.show_start_ui()
            self.close()
        else:

            category_window = CategoryWindow(self.parent)
            category_window.show()
            self.close()

    def go_back(self):
        self.timer.stop()
        self.close()
        category_window = CategoryWindow(self.parent)
        category_window.show()

# Run the application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = WordleGame()
    main_window.show()
    sys.exit(app.exec_())
