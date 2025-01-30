# Sneku
# By: Amador, Javier, Roleda & Tapa
# BET-CPET-2A

"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣄⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡖⣻⠉⢿⣿⠆⠈⠙⢶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡚⠒⠊⠙⠂⠀⠀⢆⣱⡘⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡟⠛⠳⣖⠒⠒⢙⡤⣿⣷⠃⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢻⠆⠤⠤⡗⣿⢻⣼⢀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠸⣼⣏⡒⢲⠟⡟⣾⡾⣎⢾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⢸⡴⢻⠃⠀⡜⢸⣻⠴⠛⠁⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣰⣰⣷⠏⠀⢰⠃⣿⣷⢳⣰⣤⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠹⣯⣿⣟⠢⢤⣇⣸⣿⡽⣧⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⣭⠓⠌⠉⡛⠉⣿⣼⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⣰⠁⣼⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⠀⠐⠁⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⣼⠏⢰⢦⡀⠀⠀⠀⠀⠀⣀⡠⠤⠤⠤⠤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠀⡀⠀⠀⣸⡟⠀⠈⢯⡓⠦⢤⡤⠴⠚⠁⠀⠀⠀⠀⠀⢘⠍⠳⡄⠀⠀⠀⠀
⠀⠀⢀⣠⠤⠖⠒⡒⠒⠢⢤⡗⢤⡉⢺⠒⣿⡃⣀⣀⣠⠽⠷⠒⠛⠉⠉⣉⣉⣛⣛⣛⣛⡉⠀⠀⣸⠀⠀⠀⠀
⢀⡴⠋⠀⠀⢠⠊⠀⠀⠀⢸⡇⢄⡈⠛⣏⣿⠉⠁⠀⢀⣠⠤⠖⠚⠉⠉⠀⠀⠀⠓⠦⣄⠉⠙⠚⠯⣄⡀⠀⠀
⡜⠀⠀⠀⠀⢸⣤⡶⠦⢤⣼⣇⠀⠈⢉⣧⢿⣧⠴⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠉⢦⠀
⣇⠀⠀⠀⠀⠈⠳⣄⣀⣀⣈⣿⠑⠢⠤⠼⡞⣿⡄⠀⠀⠀⠀⠀⢀⣀⣠⡤⠴⠶⠶⠒⠒⢿⡇⠀⠀⠀⠀⠸⡆
⠘⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠈⠐⠂⠙⣖⠻⣤⣠⣤⡶⠞⠋⠉⠀⠀⠀⠀⠀⠀⢀⡼⠃⠀⠀⠀⠀⢸⠇
⠀⠈⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⠘⢧⡀⠀⠀⠈⠢⠀⠉⠓⠦⠤⢤⣀⣠⠤⠤⠤⠒⠚⠉⠀⠀⠀⠀⠀⣠⡟⠁
⠀⠀⠀⠀⠈⠙⠓⠲⠶⠶⠶⠶⠞⠛⠓⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣤⠴⠞⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀

        ██████  ███▄    █ ▓█████  ██ ▄█▀ █    ██ 
      ▒██    ▒  ██ ▀█   █ ▓█   ▀  ██▄█▒  ██  ▓██▒
      ░ ▓██▄   ▓██  ▀█ ██▒▒███   ▓███▄░ ▓██  ▒██░
        ▒   ██▒▓██▒  ▐▌██▒▒▓█  ▄ ▓██ █▄ ▓▓█  ░██░
      ▒██████▒▒▒██░   ▓██░░▒████▒▒██▒ █▄▒▒█████▓ 
      ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░░ ▒░ ░▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ 
      ░ ░▒  ░ ░░ ░░   ░ ▒░ ░ ░  ░░ ░▒ ▒░░░▒░ ░ ░ 
      ░  ░  ░     ░   ░ ░    ░   ░ ░░ ░  ░░░ ░ ░ 
            ░           ░    ░  ░░  ░      ░                                                                           
"""


"""
So what do we use queue on this code for?

On Leaderboard: We implement a LeaderboardQueue class that maintains a fixed-
size (default 10) ordered collection of high scores. When a new score is added 
via add_score(), it's appended to the queue and then the entire queue is sorted in 
descending order based on the scores. The queue is then trimmed to maintain only 
the top scores up to the maximum size. This implementation ensures that only the 
highest scores are kept and displayed, while automatically removing lower scores 
when new higher scores are achieved. The queue's contents can be saved to and 
loaded from a file for persistence between game sessions.


On the Sneku Movement: The snake's movement uses a direction_queue implemented 
as a deque (double-ended queue) to handle player input more smoothly. When a player 
presses a direction key, the new direction is added to the queue (if it's not opposite
to the current direction), and during each game update, the next direction is taken from
the front of the queue using popleft(). This queuing system prevents the snake from making
impossible turns (like immediately reversing direction) and allows for more responsive
controls by buffering rapid directional inputs, ensuring that no player moves are lost
even if they're input faster than the snake's update rate.
"""


import sys
import os
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFrame
from PyQt5.QtCore import QTimer
import pygame
import random
from collections import deque
from enum import Enum, auto

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

class AppleType(Enum):
    REGULAR = auto()
    POISON = auto()
    GOLDEN = auto()
    TELEPORTATION = auto()

class GameState(Enum):
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()

class MovableWindowMixin:
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

class Sneku(QFrame):
    score_updated = QtCore.pyqtSignal(int)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.game_over_signal = QtCore.pyqtSignal()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(100)
        self.apple_positions = []  
        self.apple_types = []
        self.apple_spawn_times = []
        self.apple_rot_time = 7000
        self.apples_eaten_total = 0
        self.regular_apples_eaten = 0
        self.init_game()

    def init_game(self):
        self.block_size = 20
        self.snake_body = [(300, 300), (280, 300), (260, 300)]
        self.direction = Direction.RIGHT
        self.direction_queue = deque([self.direction])
        self.score = 0
        self.regular_apples_eaten = 0
        self.game_state = GameState.PLAYING
        self.speed_multiplier = 1.0
        self.wall_count = 0
        self.walls = []
        self.load_images()
        self.score_updated.emit(self.score)
        if hasattr(self, 'timer'):
            self.timer.start(100)
        self.apple_positions = []
        self.apple_types = []
        self.apple_spawn_times = []
        self.apples_eaten_count = 0 
        self.apples_eaten_total = 0
        self.regular_apples_eaten = 0
        self.add_new_apple() 
        self.setFocus()

    def get_current_time(self):
        return QtCore.QDateTime.currentDateTime().toMSecsSinceEpoch()

    def add_special_apple(self):
        new_position = self.random_grid_position()
        new_type = random.choice([AppleType.GOLDEN, AppleType.TELEPORTATION, AppleType.POISON])
        while (new_position in self.snake_body or 
               new_position in self.walls or 
               new_position in self.apple_positions):
            new_position = self.random_grid_position()
        self.apple_positions.append(new_position)
        self.apple_types.append(new_type)
        self.apple_spawn_times.append(self.get_current_time())
        window = self.window()
        if window and hasattr(window, 'game_manager'):
            window.game_manager.sound_manager.play('pop')

    def add_new_apple(self):
        new_position = self.random_grid_position()
        new_type = AppleType.REGULAR
        while (new_position in self.snake_body or 
               new_position in self.walls or 
               new_position in self.apple_positions):
            new_position = self.random_grid_position()
        self.apple_positions.append(new_position)
        self.apple_types.append(new_type)
        self.apple_spawn_times.append(self.get_current_time())

    def check_apple_rot(self):
        current_time = self.get_current_time()
        i = 0
        while i < len(self.apple_spawn_times):
            spawn_time = self.apple_spawn_times[i]
            elapsed = current_time - spawn_time
            if elapsed >= self.apple_rot_time:
                self.apple_positions.pop(i)
                self.apple_types.pop(i)
                self.apple_spawn_times.pop(i)
                self.add_new_apple() 
            else:
                i += 1

    def focusInEvent(self, event):
        super().focusInEvent(event)
        self.setFocus()

    def load_images(self):
        def load_and_scale(path):
            try:
                image = pygame.image.load(path)
                return pygame.transform.scale(image, (self.block_size, self.block_size))
            except pygame.error:
                surface = pygame.Surface((self.block_size, self.block_size))
                surface.fill((255, 0, 0)) 
                return surface
        
        self.images = {
            'apple': load_and_scale('images/apple.png'),
            'poison_apple': load_and_scale('images/poison_apple.png'),
            'golden_apple': load_and_scale('images/golden_apple.png'),
            'teleporting_apple': load_and_scale('images/teleporting_apple.png'),
            'wall': load_and_scale('images/wall.png'),
            'snake_head': load_and_scale('images/snake.png'),
            'snake_body': load_and_scale('images/body.png'),
            'snake_tail': load_and_scale('images/tail.png')
        }

    def random_grid_position(self):
        return (
            random.randint(0, (self.width() // self.block_size) - 1) * self.block_size,
            random.randint(0, (self.height() // self.block_size) - 1) * self.block_size
        )

    def get_random_apple_type(self):
        if self.apples_eaten_total < 5:
            return AppleType.REGULAR
        else:
            weights = {
                AppleType.REGULAR: 70,
                AppleType.GOLDEN: 15,
                AppleType.TELEPORTATION: 10,
                AppleType.POISON: 5
            }
            types, weights = zip(*weights.items())
            return random.choices(types, weights=weights)[0]

    def keyPressEvent(self, event):
        
        key_actions = {
            QtCore.Qt.Key_P: self.toggle_pause,
            QtCore.Qt.Key_R: self.handle_restart,
            QtCore.Qt.Key_Escape: self.handle_escape
        }
        
        if event.key() in key_actions:
            key_actions[event.key()]()
            return

        if self.game_state != GameState.PLAYING:
            return

        direction_keys = {
            QtCore.Qt.Key_Left: (Direction.LEFT, Direction.RIGHT),
            QtCore.Qt.Key_Right: (Direction.RIGHT, Direction.LEFT),
            QtCore.Qt.Key_Up: (Direction.UP, Direction.DOWN),
            QtCore.Qt.Key_Down: (Direction.DOWN, Direction.UP)
        }

        if event.key() in direction_keys:
            new_direction, opposite = direction_keys[event.key()]
            if self.direction != opposite and (not self.direction_queue or self.direction_queue[-1] != opposite):
                self.direction_queue.append(new_direction)

    def toggle_pause(self):
        if self.game_state == GameState.PLAYING:
            self.pause_game()
        elif self.game_state == GameState.PAUSED:
            self.resume_game()

    def pause_game(self):
        self.game_state = GameState.PAUSED
        self.timer.stop()
        self.special_apple_timer.stop()
        window = self.window()
        if window and hasattr(window, 'game_manager'):
            window.game_manager.show_pause_window(self.score)

    def resume_game(self):
        head_x, head_y = self.snake_body[0]
        direction_updates = {
            Direction.UP: (0, -self.block_size),
            Direction.DOWN: (0, self.block_size),
            Direction.LEFT: (-self.block_size, 0),
            Direction.RIGHT: (self.block_size, 0)
        }
        dx, dy = direction_updates[self.direction]
        next_position = (head_x + dx, head_y + dy)
        if (next_position in self.snake_body[1:] or
            next_position[0] < 0 or next_position[0] >= self.width() or
            next_position[1] < 0 or next_position[1] >= self.height() or
            next_position in self.walls):
            self.game_over()
            return
        self.game_state = GameState.PLAYING
        self.timer.start()
        self.special_apple_timer.start()  

    def handle_restart(self):
        if self.game_state == GameState.GAME_OVER:
            self.init_game()
            self.timer.start()
            self.setFocus()
            self.game_state = GameState.PLAYING
            self.direction_queue.clear()
            self.direction = Direction.RIGHT

    def handle_escape(self):
        self.close()

    def update_game(self):
        if self.game_state != GameState.PLAYING:
            return
        self.check_apple_rot()
        if self.direction_queue:
            self.direction = self.direction_queue.popleft()
        head_x, head_y = self.snake_body[0]
        direction_updates = {
            Direction.UP: (0, -self.block_size),
            Direction.DOWN: (0, self.block_size),
            Direction.LEFT: (-self.block_size, 0),
            Direction.RIGHT: (self.block_size, 0)
        }
        dx, dy = direction_updates[self.direction]
        new_head = (head_x + dx, head_y + dy)
        if self.check_collision(new_head):
            self.game_over()
            return
        self.snake_body = [new_head] + self.snake_body[:-1]
        for i, apple_pos in enumerate(self.apple_positions):
            if self.snake_body[0] == apple_pos:
                self.handle_apple_collision(i)
                break     
        self.update()

    def check_collision(self, position):
        x, y = position
        max_x = ((self.width() // self.block_size) * self.block_size) - self.block_size
        max_y = ((self.height() // self.block_size) * self.block_size) - self.block_size
        if (x < 0 or x > max_x or
            y < 0 or y > max_y):
            return True
        if position in self.snake_body[1:]:
            return True  
        if position in self.walls:
            return True
            
        return False

    def update_score(self, points):
            self.score += points
            self.score_updated.emit(self.score)

    def handle_apple_collision(self, apple_index):
        apple_type = self.apple_types[apple_index]
        window = self.window()
        if window and hasattr(window, 'game_manager'):
            if apple_type == AppleType.REGULAR:
                window.game_manager.sound_manager.play('eat')
                self.regular_apples_eaten += 1
                if self.regular_apples_eaten % 5 == 0:
                    self.add_special_apple()
            elif apple_type == AppleType.GOLDEN:
                window.game_manager.sound_manager.play('golden_apple')
            elif apple_type == AppleType.TELEPORTATION:
                window.game_manager.sound_manager.play('teleport')
        apple_effects = {
            AppleType.REGULAR: self.handle_regular_apple,
            AppleType.GOLDEN: self.handle_golden_apple,
            AppleType.POISON: self.handle_poison_apple,
            AppleType.TELEPORTATION: self.handle_teleportation_apple
        }
        effect_func = apple_effects.get(apple_type)
        if effect_func:
            effect_func()

        self.apple_positions.pop(apple_index)
        self.apple_types.pop(apple_index)
        self.apple_spawn_times.pop(apple_index)
        self.apples_eaten_total += 1
        self.apples_eaten_count += 1
        self.manage_apple_count()
        if self.apples_eaten_count >= 10:
            self.update_walls()
        self.add_new_apple()

    def manage_apple_count(self):
        target_apple_count = (self.apples_eaten_total // 5) + 1
        current_apple_count = len(self.apple_positions)
        while current_apple_count < target_apple_count:
            self.add_new_apple()
            current_apple_count += 1

    def handle_regular_apple(self):
        self.update_score(1) 
        self.regular_apples_eaten += 1
        self.snake_body.append(self.snake_body[-1])
        self.speed_multiplier = min(2.0, self.speed_multiplier + 0.02)

    def handle_golden_apple(self):
        self.update_score(2) 
        self.snake_body.append(self.snake_body[-1])
        self.snake_body.append(self.snake_body[-1])

    def handle_poison_apple(self):
        self.game_over()

    def handle_teleportation_apple(self):
        self.update_score(3)
        new_head = self.random_grid_position()
        while new_head in self.walls or new_head in self.snake_body:
            new_head = self.random_grid_position()
        self.snake_body.insert(0, new_head)
        self.snake_body.pop()

    def update_walls(self):
        self.walls.clear()
        self.wall_count += 1
        self.walls = self.generate_walls()
        self.apples_eaten_count = 0

    def generate_walls(self):
        walls = set()
        for _ in range(self.wall_count):
            wall_type = random.choice(['horizontal', 'vertical', 'diagonal'])
            
            if wall_type == 'horizontal':
                x = random.randint(0, (self.width() // self.block_size) - 5) * self.block_size
                y = random.randint(0, (self.height() // self.block_size) - 1) * self.block_size
                for i in range(random.randint(3, 5)):
                    walls.add((x + (i * self.block_size), y))
            elif wall_type == 'vertical':
                x = random.randint(0, (self.width() // self.block_size) - 1) * self.block_size
                y = random.randint(0, (self.height() // self.block_size) - 5) * self.block_size
                for i in range(random.randint(3, 5)):
                    walls.add((x, y + (i * self.block_size)))
            else: 
                x = random.randint(0, (self.width() // self.block_size) - 5) * self.block_size
                y = random.randint(0, (self.height() // self.block_size) - 5) * self.block_size
                for i in range(random.randint(3, 5)):
                    walls.add((x + (i * self.block_size), y + (i * self.block_size)))  
        return list(walls)

    def game_over(self):
        if self.game_state == GameState.PLAYING:
            self.game_state = GameState.GAME_OVER
            self.timer.stop()
            main_window = self.window()
            if isinstance(main_window, MainWindow) and hasattr(main_window, 'game_manager'):
                main_window.game_manager.sound_manager.play('crash')
                
                if main_window.isVisible():
                    player_name = main_window.game_manager.start_window.name_bar.text() or "Unknown"
                    time_str = main_window.time_lbl.text()
                    main_window.update_leaderboard(self.score, time_str, player_name)
                    QtCore.QTimer.singleShot(100, lambda: main_window.game_manager.show_notification(self.score))

    def show_game_over_notification(self, main_window):
        if hasattr(main_window, 'game_manager'):
            main_window.game_manager.show_notification(self.score)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        self.draw_game(painter)

    def draw_game(self, painter):
        self.draw_background(painter)
        self.draw_snake(painter)
        self.draw_apple(painter)
        self.draw_walls(painter)
        if self.game_state == GameState.PAUSED:
            self.draw_pause_overlay(painter)

    def draw_background(self, painter):
        bg_color_1 = QtGui.QColor(179, 213, 90)
        bg_color_2 = QtGui.QColor(142, 204, 57)
        for row in range(self.height() // self.block_size):
            for col in range(self.width() // self.block_size):
                color = bg_color_1 if (row + col) % 2 == 0 else bg_color_2
                painter.fillRect(
                    col * self.block_size, 
                    row * self.block_size, 
                    self.block_size, 
                    self.block_size, 
                    color
                )

    def draw_snake(self, painter):
        for i, segment in enumerate(self.snake_body):
            if i == 0: 
                image = self.images['snake_head']
                angle = {
                    Direction.RIGHT: 0,
                    Direction.DOWN: 270,
                    Direction.LEFT: 180,
                    Direction.UP: 90
                }[self.direction]
                rotated = pygame.transform.rotate(image, angle)
            elif i == len(self.snake_body) - 1: 
                image = self.images['snake_tail']
                prev = self.snake_body[-2]
                curr = self.snake_body[-1]
                dx = prev[0] - curr[0]
                dy = prev[1] - curr[1]
                if dx > 0:     
                    angle = 0
                elif dx < 0:   
                    angle = 180
                elif dy > 0:   
                    angle = 270
                else:           
                    angle = 90
                rotated = pygame.transform.rotate(image, angle)
            else: 
                image = self.images['snake_body']
                prev = self.snake_body[i-1]
                curr = self.snake_body[i]
                next_seg = self.snake_body[i+1]
                dx1 = curr[0] - prev[0]
                dy1 = curr[1] - prev[1]
                dx2 = next_seg[0] - curr[0]
                dy2 = next_seg[1] - curr[1]
                is_corner = (dx1 != dx2 or dy1 != dy2) and not (dx1 == 0 and dy1 == 0) and not (dx2 == 0 and dy2 == 0)
                if is_corner:
                    if (dx1 > 0 and dy2 > 0) or (dy1 < 0 and dx2 < 0):
                        angle = 0
                    elif (dx1 > 0 and dy2 < 0) or (dy1 > 0 and dx2 < 0):
                        angle = 90
                    elif (dx1 < 0 and dy2 > 0) or (dy1 < 0 and dx2 > 0):
                        angle = 270
                    else:
                        angle = 180
                else:
                    if dx1 != 0:
                        angle = 90
                    else:
                        angle = 0
                rotated = pygame.transform.rotate(image, angle)     
            qt_image = self.pygame_surface_to_qt_image(rotated)
            painter.drawImage(
                QtCore.QRect(
                    segment[0], 
                    segment[1], 
                    self.block_size, 
                    self.block_size
                ),
                qt_image
            )

    def draw_apple(self, painter):
        apple_images = {
            AppleType.REGULAR: 'apple',
            AppleType.POISON: 'poison_apple',
            AppleType.GOLDEN: 'golden_apple',
            AppleType.TELEPORTATION: 'teleporting_apple'
        }
        current_time = self.get_current_time()
        for i, (pos, apple_type) in enumerate(zip(self.apple_positions, self.apple_types)):
            image = self.images[apple_images[apple_type]]
            elapsed = current_time - self.apple_spawn_times[i]
            remaining_time = max(0, self.apple_rot_time - elapsed)
            opacity = min(255, int((remaining_time / self.apple_rot_time) * 255))
            qt_image = self.pygame_surface_to_qt_image(image)
            if opacity < 255:
                transparent_image = QtGui.QImage(qt_image.size(), QtGui.QImage.Format_ARGB32)
                transparent_image.fill(QtCore.Qt.transparent)
                painter_temp = QtGui.QPainter(transparent_image)
                painter_temp.setOpacity(opacity / 255.0)
                painter_temp.drawImage(0, 0, qt_image)
                painter_temp.end()
                qt_image = transparent_image
            painter.drawImage(
                QtCore.QRect(
                    pos[0],
                    pos[1],
                    self.block_size,
                    self.block_size
                ),
                qt_image
            )

    def draw_walls(self, painter):
        wall_image = self.pygame_surface_to_qt_image(self.images['wall'])
        for wall in self.walls:
            painter.drawImage(
                QtCore.QRect(wall[0], wall[1], self.block_size, self.block_size),
                wall_image
            )

    def draw_pause_overlay(self, painter):
        overlay = QtGui.QColor(0, 0, 0, 128)
        painter.fillRect(self.rect(), overlay)
        painter.setPen(QtGui.QColor(255, 255, 255))
        painter.setFont(QtGui.QFont('Arial', 24))
        painter.drawText(
            self.rect(),
            QtCore.Qt.AlignCenter,
            'PAUSED\nPress P to continue'
        )

    def pygame_surface_to_qt_image(self, surface):
        try:
            if surface.get_bitsize() != 32:
                surface = surface.convert_alpha()
        except pygame.error:
            new_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
            new_surface.blit(surface, (0, 0))
            surface = new_surface
        
        image_data = pygame.image.tostring(surface, 'RGBA')
        image = QtGui.QImage(
            image_data,
            surface.get_width(),
            surface.get_height(),
            surface.get_width() * 4,
            QtGui.QImage.Format_RGBA8888
        )
        return image

class LeaderboardQueue:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.queue = []
        
    def extract_score(self, entry):
        score_part = entry.split(' / ')[0] 
        score = int(score_part.split(': ')[1])
        return score
        
    def add_score(self, entry):
        self.queue.append(entry)
        self.queue.sort(key=self.extract_score, reverse=True)
        self.queue = self.queue[:self.max_size]
    
    def get_entries(self):
        return self.queue

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for entry in self.queue:
                f.write(f"{entry}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            entries = [line.strip() for line in f if line.strip()]
            self.queue = []
            for entry in entries:
                self.add_score(entry)

class MainWindow(QMainWindow, MovableWindowMixin):
    def __init__(self, game_manager):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        uic.loadUi("ui/main.ui", self)
        self.game_manager = game_manager
        self.game_time = 0
        self.leaderboard = LeaderboardQueue(max_size=10)
        self.setup_ui()
        self.setup_game()
        self.setup_leaderboard()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def setup_ui(self):
        gif_path = os.path.join("gif", "tutorial.gif")
        self.movie = QtGui.QMovie(gif_path)
        self.gif_label = self.findChild(QLabel, "gif_lbl")
        self.gif_label.setMovie(self.movie)
        self.movie.start()
        self.sound_btn.clicked.connect(self.handle_sound_click)
        self.exit_btn.clicked.connect(self.handle_exit_click)
        self.back_btn.clicked.connect(self.handle_back_click)
        self.score_lbl = self.findChild(QLabel, "score_lbl")
        self.time_lbl = self.findChild(QLabel, "time_lbl")
        self.score_lbl.setText("0")
        self.time_lbl.setText("0:00")

    def setup_game(self):
        self.game_frame = self.findChild(QFrame, "game_frame")
        if self.game_frame:
            layout = QtWidgets.QVBoxLayout(self.game_frame)
            self.snake_game = Sneku(self)
            layout.addWidget(self.snake_game)
            self.game_frame.setLayout(layout)
            self.snake_game.score_updated.connect(self.update_score)
            self.snake_game.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.snake_game.setFocus()
            self.snake_game.game_state = GameState.PLAYING

    def reset_game(self):
        self.game_time = 0
        self.time_lbl.setText("0:00")
        self.score_lbl.setText("0")
        if hasattr(self, 'snake_game'):
            self.snake_game.init_game()
            self.snake_game.game_state = GameState.PLAYING
            self.snake_game.direction_queue.clear()
            self.snake_game.direction = Direction.RIGHT
            QtCore.QTimer.singleShot(100, self.snake_game.setFocus) 

    def showEvent(self, event):
        super().showEvent(event)
        if hasattr(self, 'snake_game'):
            self.snake_game.setFocus()

    def setup_leaderboard(self):
        self.leaderboard_tbl = self.findChild(QtWidgets.QTableWidget, "leaderboard_tbl")
        self.leaderboard_tbl.setColumnCount(1)
        self.leaderboard_tbl.setHorizontalHeaderLabels(["Leaderboard"])
        self.load_leaderboard()

    def load_leaderboard(self):
        self.leaderboard.load_from_file('leaderboard.txt')
        entries = self.leaderboard.get_entries()
        self.leaderboard_tbl.setRowCount(len(entries))
        for i, entry in enumerate(entries):
            item = QtWidgets.QTableWidgetItem(entry)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.leaderboard_tbl.setItem(i, 0, item)

    def update_leaderboard(self, score, time_str, player_name):
        try:
            entry = f"{player_name}: {score} / {time_str}"
            self.leaderboard.add_score(entry)
            self.leaderboard.save_to_file('leaderboard.txt')
            self.load_leaderboard()
            
        except Exception as e:
            print(f"Error updating leaderboard: {e}")

    def refresh_leaderboard_display(self):
        entries = self.leaderboard.get_entries()
        self.leaderboard_tbl.setRowCount(len(entries))
        for i, entry in enumerate(entries):
            item = QtWidgets.QTableWidgetItem(entry)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.leaderboard_tbl.setItem(i, 0, item)

    def update_score(self, score):
        self.score_lbl.setText(str(score))

    def update_time(self):
        if hasattr(self, 'snake_game') and self.snake_game.game_state == GameState.PLAYING:
            self.game_time += 1
            minutes = self.game_time // 60
            seconds = self.game_time % 60
            self.time_lbl.setText(f"{minutes}:{seconds:02d}")

    def reset_time(self):
        self.game_time = 0
        self.time_lbl.setText("0:00")

    def toggle_sound(self):
        self.game_manager.toggle_sound()
        self.update_sound_button()

    def update_sound_button(self):
        icon = QtGui.QIcon()
        if self.game_manager.sound_enabled:
            icon.addPixmap(QtGui.QPixmap("images/sound.png"))
        else:
            icon.addPixmap(QtGui.QPixmap("images/mute.png"))
        self.sound_btn.setIcon(icon)

    def go_back(self):
        self.game_manager.show_start_window()

    def handle_sound_click(self):
        self.game_manager.sound_manager.play('click')
        self.toggle_sound()

    def handle_exit_click(self):
        self.game_manager.sound_manager.play('click')
        self.close()

    def handle_back_click(self):
        self.game_manager.sound_manager.play('click')
        self.go_back()

class NotificationWindow(QMainWindow, MovableWindowMixin):
    def __init__(self, game_manager, score):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        uic.loadUi("ui/notification.ui", self)
        self.game_manager = game_manager
        self.setup_ui(score)

    def setup_ui(self, score):
        self.score_label = self.findChild(QLabel, "score_label")
        if self.score_label:
            player_name = self.game_manager.start_window.name_bar.text() or "Unknown"
            self.score_label.setText(f"{player_name}'s Score: {score}")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F:
            self.close()
            self.game_manager.show_start_window()

    def showEvent(self, event):
        super().showEvent(event)
        if self.game_manager.current_window:
            self.game_manager.current_window.setEnabled(False)
        
    def closeEvent(self, event):
        if self.game_manager.current_window:
            self.game_manager.current_window.setEnabled(True)
        event.accept()
        self.game_manager.show_start_window()

class StartWindow(QMainWindow, MovableWindowMixin):
    def __init__(self, game_manager):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        uic.loadUi("ui/start.ui", self)
        self.game_manager = game_manager
        self.setup_ui()
        self.name_bar = self.findChild(QtWidgets.QLineEdit, "name_bar")
        self.update_sound_button()

    def setup_ui(self):
        gif_path = os.path.join("gif", "logo.gif")
        self.movie = QtGui.QMovie(gif_path)
        self.gif_lbl = self.findChild(QLabel, "gif_lbl")
        self.gif_lbl.setMovie(self.movie)
        self.movie.start()
        self.sound_btn.clicked.connect(self.handle_sound_click)
        self.exit_btn.clicked.connect(self.handle_exit_click)
        if hasattr(self, 'name_bar'):
            self.name_bar.setPlaceholderText("Enter your name")

    def toggle_sound(self):
        self.game_manager.toggle_sound()
        self.update_sound_button()

    def update_sound_button(self):
        icon = QtGui.QIcon()
        if self.game_manager.sound_enabled:
            icon.addPixmap(QtGui.QPixmap("images/sound.png"))
        else:
            icon.addPixmap(QtGui.QPixmap("images/mute.png"))
        self.sound_btn.setIcon(icon)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            if not self.name_bar.text().strip():
                self.game_manager.show_name_notification()
            else:
                self.game_manager.show_main_window()

    def handle_sound_click(self):
        self.game_manager.sound_manager.play('click')
        self.toggle_sound()

    def handle_exit_click(self):
        self.game_manager.sound_manager.play('click')
        self.close()

class NameNotificationWindow(QMainWindow, MovableWindowMixin):
    def __init__(self, game_manager):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        uic.loadUi("ui/name_notif.ui", self)
        self.game_manager = game_manager

        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.close()
            self.game_manager.start_window.name_bar.setFocus()

    def showEvent(self, event):
        if self.game_manager.current_window:
            self.game_manager.current_window.setEnabled(False)
        super().showEvent(event)
        
    def closeEvent(self, event):
        if self.game_manager.current_window:
            self.game_manager.current_window.setEnabled(True)
        super().closeEvent(event)

class PauseWindow(QMainWindow, MovableWindowMixin):
    def __init__(self, game_manager, current_score):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        uic.loadUi("ui/pause.ui", self)
        self.game_manager = game_manager
        self.setup_ui(current_score)


    def setup_ui(self, current_score):
        self.current_score_lbl = self.findChild(QLabel, "current_score_lbl")
        if self.current_score_lbl:
            self.current_score_lbl.setText(f"Score: {current_score}")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_P:
            self.close()
            if isinstance(self.game_manager.current_window, MainWindow):
                self.game_manager.current_window.snake_game.resume_game()

    def showEvent(self, event):
        if self.game_manager.current_window:
            self.game_manager.current_window.setEnabled(False)
        super().showEvent(event)
        
    def closeEvent(self, event):
        if self.game_manager.current_window:
            self.game_manager.current_window.setEnabled(True)
        super().closeEvent(event)

class SoundManager:
    def __init__(self):
        self.sounds = {}
        self.load_sounds()
        self.enabled = True

    def load_sounds(self):
        sound_files = {
            'crash': 'sounds/crash.mp3',
            'eat': 'sounds/eat.mp3',
            'pop': 'sounds/pop.mp3',
            'teleport': 'sounds/teleport.mp3',
            'golden_apple': 'sounds/golden_apple.mp3',
            'click': 'sounds/click.mp3'
        }
        
        for name, path in sound_files.items():
            try:
                self.sounds[name] = pygame.mixer.Sound(path)
            except pygame.error as e:
                print(f"Error loading sound {name}: {e}")

    def play(self, sound_name):
        if self.enabled and sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except pygame.error as e:
                print(f"Error playing sound {sound_name}: {e}")

    def toggle_enabled(self):
        self.enabled = not self.enabled

class SnekuLauncher:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.sound_enabled = True
        pygame.init()
        pygame.mixer.init()
        self.sound_manager = SoundManager()
        self.main_window = None
        self.start_window = None
        self.notification_window = None
        self.current_window = None
        
        self.init_windows()

    def init_windows(self):
        self.start_window = StartWindow(self)
        self.main_window = MainWindow(self)
        self.name_notification_window = NameNotificationWindow(self)

    def run(self):
        try:
            self.play_background_music()
            self.show_start_window()
            sys.exit(self.app.exec_())
        except Exception as e:
            print(f"Error in run: {e}")

    def show_name_notification(self):
        self.name_notification_window.show()

    def show_pause_window(self, score):
        self.pause_window = PauseWindow(self, score)
        self.pause_window.show()

    def play_background_music(self):
        try:
            pygame.mixer.music.load("sounds/bgmusic.mp3")
            pygame.mixer.music.play(-1)
        except pygame.error as e:
            print(f"Error loading music: {e}")

    def show_notification(self, score):
        if (hasattr(self.main_window, 'snake_game') and 
            self.main_window.snake_game and 
            self.main_window.snake_game.game_state == GameState.GAME_OVER):
            self.notification_window = NotificationWindow(self, score)
            self.notification_window.show()

    def show_start_window(self):
        if self.notification_window:
            self.notification_window.close()
            self.notification_window = None
        
        if self.current_window:
            self.current_window.hide()
        
        self.current_window = self.start_window
        self.current_window.show()

    def show_main_window(self):
        if self.notification_window:
            self.notification_window.close()
            self.notification_window = None
        if self.current_window:
            self.current_window.hide()
        self.current_window = self.main_window
        self.main_window.reset_game()  
        self.current_window.show()

    def toggle_sound(self):
        self.sound_enabled = not self.sound_enabled
        self.sound_manager.toggle_enabled()
        if self.sound_enabled:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        if self.start_window:
            self.start_window.update_sound_button()
        if self.main_window:
            self.main_window.update_sound_button()


if __name__ == "__main__":
    game = SnekuLauncher()
    game.run()