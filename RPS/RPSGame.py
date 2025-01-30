import sys
import random
import pygame
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtCore import QTimer

#RFSG

class RPSGame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("rps_start.ui", self)
        self.center_window()  
        self.set_background_image("images/lobby.png")
        self.start_btn.clicked.connect(self.start_game)

    def center_window(self):
        screen_geometry = QtWidgets.QDesktopWidget().availableGeometry().center()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry)
        self.move(window_geometry.topLeft())

    def center_window_for_ui(self, window):
        screen_geometry = QtWidgets.QDesktopWidget().availableGeometry().center()
        window_geometry = window.frameGeometry()
        window_geometry.moveCenter(screen_geometry)
        window.move(window_geometry.topLeft())

    def set_background_image(self, bg_path):
        self.setAutoFillBackground(True)
        palette = self.palette()
        background_pixmap = QtGui.QPixmap(bg_path).scaled(self.size(), QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(background_pixmap))
        self.setPalette(palette)

    def start_game(self):
        uic.loadUi("rockpaperscissor.ui", self)
        self.center_window()  # Center the main game window
        self.set_background_image("images/background.png")
        self.init_game()
        self.rock_btn.mousePressEvent = lambda event: self.player_choice("rock")
        self.paper_btn.mousePressEvent = lambda event: self.player_choice("paper")
        self.scissor_btn.mousePressEvent = lambda event: self.player_choice("scissor")
        self.spock_btn.mousePressEvent = lambda event: self.player_choice("spock")
        self.lizard_btn.mousePressEvent = lambda event: self.player_choice("lizard")
        self.music_btn.clicked.connect(self.toggle_music)

    def init_game(self):
        pygame.mixer.init()
        self.music_on = True
        pygame.mixer.music.load("audio/soundtrack.mp3")
        pygame.mixer.music.play(-1)
        self.options = ["rock", "paper", "scissor", "spock", "lizard"]
        self.rules = {
            "rock": ["scissor", "lizard"], "paper": ["rock", "spock"], 
            "scissor": ["paper", "lizard"], "spock": ["scissor", "rock"], 
            "lizard": ["spock", "paper"]
        }
        self.player_score = 0
        self.computer_score = 0
        self.winning_streak = 0
        self.losing_streak = 0

    def toggle_music(self):
        if self.music_on:
            pygame.mixer.music.pause()
            self.music_btn.setStyleSheet("background-color: red; color: white; border-radius: 25px;")
        else:
            pygame.mixer.music.unpause()
            self.music_btn.setStyleSheet("background-color: rgb(0, 255, 127); border-radius: 25px;")
        self.music_on = not self.music_on

    def player_choice(self, choice):
        image_filenames = {
            "rock": "roooocckkko.png", "paper": "paper jsdnjhd.png", 
            "scissor": "sisorsbadi.png", "spock": "spoooccckkk.png", 
            "lizard": "lisard.png"
        }
        self.your_pick_img.setPixmap(QtGui.QPixmap(f"images/{image_filenames[choice]}"))
        computer_choice = random.choice(self.options)
        self.enemy_pic_img.setPixmap(QtGui.QPixmap(f"images/{image_filenames[computer_choice]}"))
        self.check_winner(choice, computer_choice)

    def check_winner(self, player, computer):
        if player == computer:
            result = "It's a tie!"
        elif computer in self.rules[player]:
            result = "You win!"
            self.player_score += 1
            self.winning_streak += 1
            self.losing_streak = 0
        else:
            result = "You lose!"
            self.computer_score += 1
            self.winning_streak = 0
            self.losing_streak += 1
        self.update_ui_scores()
        self.show_popup(result)
        if self.winning_streak == 5:
            self.show_win_ui()
        elif self.losing_streak == 5:
            self.show_lose_ui()

    def update_ui_scores(self):
        self.player_points_label.setText(f"Player Points: {self.player_score}")
        self.counter_points_label.setText(f"Counter Points: {self.computer_score}")
        self.winning_streak_label.setText(f"Winning Streak: {self.winning_streak}")

    def show_popup(self, message):
        popup = QtWidgets.QMessageBox(self)
        popup.setStyleSheet("""
            QMessageBox {background-color: #333333; color: white; border-radius: 10px; padding: 10px;}
            QMessageBox QLabel {color: #ffffff; font-size: 16px; font-family: 'Arial', sans-serif;}
            QMessageBox QPushButton {background-color: #65f7b6; color: white; border-radius: 8px; padding: 5px 15px;}
            QMessageBox QPushButton:hover {background-color: #e64a19;}""")
        popup.setText(message)
        popup.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        popup.show()
        QTimer.singleShot(1200, popup.close)

    def show_win_ui(self):
        self.win_ui = QtWidgets.QMainWindow()
        uic.loadUi("rps_win.ui", self.win_ui)
        self.set_background_for_ui(self.win_ui, "images/win.png")
        self.center_window_for_ui(self.win_ui) 
        self.win_ui.win_rtn_btn.clicked.connect(self.return_to_main_and_close_win)
        self.win_ui.show()

    def return_to_main_and_close_win(self):
        self.return_to_main()
        self.win_ui.close()  

    def show_lose_ui(self):
        self.lose_ui = QtWidgets.QMainWindow()
        uic.loadUi("rps_lose.ui", self.lose_ui)
        self.set_background_for_ui(self.lose_ui, "images/lose.png")
        self.center_window_for_ui(self.lose_ui)  
        self.lose_ui.lose_rtn_btn.clicked.connect(self.return_to_main_and_close_lose)
        self.lose_ui.show()

    def return_to_main_and_close_lose(self):
        self.return_to_main()
        self.lose_ui.close()  

    def return_to_main(self):
        self.player_score = 0
        self.computer_score = 0
        self.winning_streak = 0
        self.losing_streak = 0
        uic.loadUi("rps_start.ui", self)
        self.center_window()  # Center the main window
        self.set_background_image("images/lobby.png")
        self.start_btn.clicked.connect(self.start_game)


    def set_background_for_ui(self, window, bg_path):
        window.setAutoFillBackground(True)
        palette = window.palette()
        background_pixmap = QtGui.QPixmap(bg_path).scaled(window.size(), QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
        palette.setBrush(window.backgroundRole(), QtGui.QBrush(background_pixmap))
        window.setPalette(palette)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = RPSGame()
    game.show()
    sys.exit(app.exec_())


#ANG SARAP NI JARRED
