# Sistema
# By: Amador, Javier, Roleda & Tapa
# BET-CPET-2A

sistema_logo = """                                                                                                                                                                                                                               
                                                                                          
                                        .:.::---:::...                                    
                                 .:-=++==-:+***+++=-:-++==-:                              
                             .-*##****++++%%########%%*+-+***+=:                          
                          .=#%%%+#%%#####%%%%%%%%%%%%%%%#+++***##+:                       
                        -*%#%%%%+**%%%%%%#**+++*+***#%%%%%%%##%#*#%#+.                    
                      =#%*#*+*%%#%%#+-:. ..    :  :   .-+#%%%%##+%%%#%*.                  
                    -#%%%#+**#%%*=.        :  .   .   ..   :=#%%%%#*#%%%+                 
                  .*%*##%%##%#=:  ..        : .. :   .        :+%%#%%%**##-               
                 :#%%%*+*%%#-   ..  .       :  :.   :         ..:*%%##+%%%%+              
                -%**%%%%%%=       .. :      :....  .        ..  : .*%%%%%#+#*             
               -%###**%%*.:          .:. . .:    ..-       : ...    =%%#*#%#%#            
              :%#%%%%%%*   .          :    :        :.....-..        :%%%%%%*%*           
              #%****%%#.    ..       :   ...--::--  .     :          :-%%#*+##%-          
             =%%%%%%%#:...::.... ...::.   =:      =. ..   :    ....::. +%%#%%%%#          
             ##***#%%=.      : .. ..      +       .-    ..:..:: ...     #%%**+#%-         
            :%%%%%%%%   .... .:..-        =:      =.       ::           +%%#+**%*         
            =%****%%*          :  :        :=.  --        .  .. ...    .=%%#*#%%#         
            =%%%%%%%*          :  .          :++          :   .:... . ..:%%#*%%%#         
            =#####%%*.. ..:::.:- ..         -- :-.        :  -.....     -%%#*=+##         
            :******%#  ..     .:. -.      :=     :=       :::        .. =%%##%%%*         
             **#**+%%-.      ..  -  ..    +       :-    .. .-          .#%##****-         
             =*##-+%%#    ...  .. :   :   +       =:   :    :..        -%***+*+*.         
             .%%#-#%%%+:::. .. ...:.. :.   --:.:--.    :.....:.:: . ..:#%++=**#=          
              -+-%%%%%%=    ...   :    -..    ..     .:      ..  ..  .#%%#==#%#           
               =+*****##+  .      :   .   -..    . ::  :       ..  .:#%%#**+++.           
                =#######%*-      :   .. : .:. .....:...:.         .=%%%%*+**+.            
                 =######%%%=  ..    .  :..  :     :  ...:.       -#%%%%%-=++.             
                  :*###%%%%%#+. . .   -.    :     :    .: .....-#%%%%%#=+#+               
                    =#%%%%%%%%%#=.    -     :     .     :.  :+%%%%%%*=+*+:                
                     .*%%%%%##%%%%#+-::    :       :   .-+*%%%%%%%%****-                  
                       .+%%%+**#%%%%%%%#*++---:---==**#%%%%%%%%%%%%#*-                    
                          -**#%%%+#*##%%%%%%%%%%%%%%%%%%%###%%%%%#+:                      
                            .-+#%+#+*%%##+%%%*%%%###%%+#%%*+#%*=:                         
                                .-+*%%%#**%%%+%%%%**%%#+%#*=:                             
                                     .:-==++++++**===-:.            

                                     
                ███████╗██╗███████╗████████╗███████╗███╗   ███╗ █████╗     
                ██╔════╝██║██╔════╝╚══██╔══╝██╔════╝████╗ ████║██╔══██╗    
                ███████╗██║███████╗   ██║   █████╗  ██╔████╔██║███████║    
                ╚════██║██║╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║██╔══██║    
                ███████║██║███████║   ██║   ███████╗██║ ╚═╝ ██║██║  ██║    
                ╚══════╝╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝                                                                
"""

"""
What is Sistema?

Sistem  is a voting system program developed in Python, utilizing various data structures
such as arrays, linked lists, stacks, and queues. The program is specifically designed for
use within a campus setting, enabling students and faculty members to cast votes for various
elections or decisions.

This program addresses these challenges by automating the voting process, making it faster,
more efficient, and accurate. The system uses arrays to store candidate information, linked
lists to keep track of the order in which votes are cast, stacks to temporarily hold data 
during the voting process, and queues to manage voter registration and verification in an
orderly manner. The program not only ensures accuracy and speed in the voting process but
also provides a streamlined and user-friendly interface for campus members to participate 
in elections.
"""

import sys
import json
import datetime
import re
import array
from typing import Any, Optional, TypeVar, Generic
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QIcon

T = TypeVar('T')

JSON_FILE = "sistema_data.json"

class Array:
    def __init__(self, size: int):
        self.size = size
        self.length = 0
        self._data = array.array('i', [0] * size)
    
    def insert(self, index: int, value: int) -> bool:
        if self.length >= self.size or index < 0 or index > self.length:
            return False
        for i in range(self.length, index, -1):
            self._data[i] = self._data[i-1]
        self._data[index] = value
        self.length += 1
        return True
    
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        for i in range(index, self.length - 1):
            self._data[i] = self._data[i+1]
        self.length -= 1
        return True
    
    def get(self, index: int) -> Optional[int]:
        if 0 <= index < self.length:
            return self._data[index]
        return None
    
    def __str__(self) -> str:
        return str([self._data[i] for i in range(self.length)])

class VoteArray:
    def __init__(self, max_candidates: int):
        self.max_candidates = max_candidates
        self.candidate_names = array.array('u', ' ' * (max_candidates * 50))  # 50 chars per name
        self.vote_counts = array.array('i', [0] * max_candidates)
        self.num_candidates = 0
        
    def add_candidate(self, name: str) -> bool:
        if self.num_candidates >= self.max_candidates:
            return False
        start_pos = self.num_candidates * 50
        name_padded = name.ljust(50)[:50] 
        for i, char in enumerate(name_padded):
            self.candidate_names[start_pos + i] = char
        self.num_candidates += 1
        return True
    
    def increment_vote(self, candidate_index: int) -> bool:
        if 0 <= candidate_index < self.num_candidates:
            self.vote_counts[candidate_index] += 1
            return True
        return False
    
    def get_votes(self, candidate_index: int) -> Optional[tuple[str, int]]:
        if 0 <= candidate_index < self.num_candidates:
            start_pos = candidate_index * 50
            name = ''.join(self.candidate_names[start_pos:start_pos + 50]).rstrip()
            return (name, self.vote_counts[candidate_index])
        return None

class SenatorArray:
    def __init__(self, max_senators: int = 7):
        self.max_senators = max_senators
        self.names = array.array('u', ' ' * (max_senators * 50))
        self.vote_counts = array.array('i', [0] * max_senators)
        self.num_senators = 0
        
    def add_senator(self, name: str) -> bool:
        if self.num_senators >= self.max_senators:
            return False
        start_pos = self.num_senators * 50
        name_padded = name.ljust(50)[:50]
        for i, char in enumerate(name_padded):
            self.names[start_pos + i] = char
        self.num_senators += 1
        return True
    
    def get_senator(self, index: int) -> Optional[str]:
        if 0 <= index < self.num_senators:
            start_pos = index * 50
            return ''.join(self.names[start_pos:start_pos + 50]).rstrip()
        return None
    
    def increment_vote(self, index: int) -> bool:
        if 0 <= index < self.num_senators:
            self.vote_counts[index] += 1
            return True
        return False

class PartyListArray:
    def __init__(self, max_parties: int):
        self.max_parties = max_parties
        self.party_names = array.array('u', ' ' * (max_parties * 50))
        self.motos = array.array('u', ' ' * (max_parties * 100))
        self.presidents = array.array('u', ' ' * (max_parties * 50))
        self.vice_presidents = array.array('u', ' ' * (max_parties * 50))
        self.num_parties = 0
        self.senators = [SenatorArray() for _ in range(max_parties)]
        
    def add_party(self, name: str, moto: str, president: str, vice_president: str) -> bool:
        if self.num_parties >= self.max_parties:
            return False
        start_pos = self.num_parties * 50
        moto_start = self.num_parties * 100
        name_padded = name.ljust(50)[:50]
        for i, char in enumerate(name_padded):
            self.party_names[start_pos + i] = char 
        moto_padded = moto.ljust(100)[:100]
        for i, char in enumerate(moto_padded):
            self.motos[moto_start + i] = char  
        pres_padded = president.ljust(50)[:50]
        for i, char in enumerate(pres_padded):
            self.presidents[start_pos + i] = char
        vp_padded = vice_president.ljust(50)[:50]
        for i, char in enumerate(vp_padded):
            self.vice_presidents[start_pos + i] = char
        self.num_parties += 1
        return True
    
    def get_party(self, index: int) -> Optional[dict]:
        if 0 <= index < self.num_parties:
            start_pos = index * 50
            moto_start = index * 100
            return {
                'name': ''.join(self.party_names[start_pos:start_pos + 50]).rstrip(),
                'moto': ''.join(self.motos[moto_start:moto_start + 100]).rstrip(),
                'president': ''.join(self.presidents[start_pos:start_pos + 50]).rstrip(),
                'vice_president': ''.join(self.vice_presidents[start_pos:start_pos + 50]).rstrip(),
                'senators': [
                    self.senators[index].get_senator(i) 
                    for i in range(self.senators[index].num_senators)
                ]
            }
        return None

class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next: Optional[Node[T]] = None

class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None
        self.size = 0

    def append(self, data: T) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def remove(self, data: T) -> bool:
        if not self.head:
            return False
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return True
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next
        return False

    def get_all(self) -> list[T]:
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

class Stack(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> Optional[T]:
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self) -> Optional[T]:
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

    def clear(self) -> None:
        self.items.clear()

class Queue(Generic[T]):
    def __init__(self):
        self.items: list[T] = []

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> Optional[T]:
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self) -> Optional[T]:
        if not self.is_empty():
            return self.items[0]
        return None

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)

    def clear(self) -> None:
        self.items.clear()

partylist_data: list[dict] = []
votes: dict = {}
voter_queue = Queue[dict]()
nominees_stack = Stack[dict]()
voter_history = LinkedList[dict]()
total_voter_count = 0

def save_data_to_json():
    """Save all data structures to JSON file"""
    data = {
        "partylist_data": partylist_data,
        "votes": votes,
        "voter_queue": voter_queue.items,
        "nominees_stack": nominees_stack.items,
        "voter_history": voter_history.get_all(),
        "total_voter_count": total_voter_count
    }
    
    try:
        with open(JSON_FILE, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except Exception as e:
        print(f"Error saving data: {str(e)}")
        return False

def load_data_from_json():
    """Load data from JSON file into data structures"""
    global partylist_data, votes, total_voter_count
    
    try:
        with open(JSON_FILE, "r") as file:
            data = json.load(file)
            
            # Clear existing data
            partylist_data.clear()
            votes.clear()
            voter_queue.clear()
            nominees_stack.clear()
            
            # Load basic data
            partylist_data.extend(data.get("partylist_data", []))
            votes.update(data.get("votes", {}))
            total_voter_count = data.get("total_voter_count", 0)
            
            # Load queue data
            for voter in data.get("voter_queue", []):
                voter_queue.enqueue(voter)
                
            # Load stack data
            for nominee in data.get("nominees_stack", []):
                nominees_stack.push(nominee)
                
            # Load voter history
            for voter in data.get("voter_history", []):
                voter_history.append(voter)
                
        return True
    except FileNotFoundError:
        # If file doesn't exist, create it with empty data
        save_data_to_json()
        return True
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return False

def add_nominee(nominee: dict):
    """Add a nominee to both partylist data and nominees stack"""
    partylist_data.append(nominee)
    nominees_stack.push(nominee)
    save_data_to_json()

def add_voter(voter: dict) -> bool:
    try:
        required_fields = ['name', 'section', 'email']
        if not all(field in voter for field in required_fields):
            return False
        existing_voters = voter_history.get_all()
        if any(v.get('email') == voter['email'] for v in existing_voters):
            return False
        if 'timestamp' not in voter:
            voter['timestamp'] = datetime.datetime.now().isoformat()
        if 'voter_id' not in voter:
            voter['voter_id'] = len(existing_voters) + 1
        voter_queue.enqueue(voter)
        voter_history.append(voter)
        save_data_to_json()
        return True
    except Exception as e:
        print(f"Error adding voter: {str(e)}")
        return False

load_data_from_json()

total_voter_count = 0

class DateManager:
    def __init__(self, json_file: str = "voting_data.json"):
        self.json_file = json_file
        self.first_nomination_date: Optional[datetime.datetime] = None
        self.load_first_nomination_date()

    def load_first_nomination_date(self) -> None:
        try:
            with open(self.json_file, "r") as file:
                data = json.load(file)
                date_str = data.get("first_nomination_date")
                if date_str:
                    self.first_nomination_date = datetime.datetime.fromisoformat(date_str)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

    def save_first_nomination_date(self) -> None:
        try:
            with open(self.json_file, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        data["first_nomination_date"] = self.first_nomination_date.isoformat()
        
        with open(self.json_file, "w") as file:
            json.dump(data, file, indent=4)

    def update_first_nomination_date(self) -> None:
        if not self.first_nomination_date and partylist_data:
            self.first_nomination_date = datetime.datetime.now()
            self.save_first_nomination_date()

    def get_days_left(self) -> str:
        if not self.first_nomination_date:
            return "7 days left"
        deadline = self.first_nomination_date + datetime.timedelta(days=7)
        today = datetime.datetime.now()
        days_remaining = (deadline - today).days
        if days_remaining < 0:
            return "Voting period has ended"
        elif days_remaining == 0:
            hours_remaining = (deadline - today).seconds // 3600
            if hours_remaining > 0:
                return f"{hours_remaining} hours left"
            else:
                return "Less than 1 hour left"
        else:
            return f"{days_remaining} days left"

class Sistema(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/main_ui.ui", self)
        self.setWindowTitle("Sistema")
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon("image/sistema.ico"))

        self.home_btn.clicked.connect(self.launch_home)
        self.nominate_btn.clicked.connect(self.launch_nominate)
        self.voteui_btn.clicked.connect(self.launch_vote)
        self.editui_btn.clicked.connect(self.launch_edit)

    def launch_home(self):
        if not partylist_data:
            QtWidgets.QMessageBox.warning(self, "Error", "No nominees have been added yet. Please nominate candidates first.")
            return
        self.home_window = HomeUI()
        self.home_window.show()
        self.close()

    def launch_nominate(self):
        self.nominate_window = NominateUI()
        self.nominate_window.show()
        self.close()

    def launch_vote(self):
        if not partylist_data:
            QtWidgets.QMessageBox.warning(self, "Error", "No nominees have been added yet. Please nominate candidates first.")
            return
        
        self.vote_page1 = VotePage1()
        self.vote_page1.show()
        self.close()

    def launch_edit(self):
        if not partylist_data:
            QtWidgets.QMessageBox.warning(self, "Error", "No nominees have been added yet. Please nominate candidates first.")
            return
        self.edit_window = EditUI()
        self.edit_window.show()

class NominateUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/nominate.ui", self)
        self.setWindowIcon(QIcon("image/sistema.ico"))
        self.setWindowTitle("Sistema")
        self.setFixedSize(self.size()) 
        self.date_manager = DateManager()
        self.back_btn.clicked.connect(self.return_to_main)
        self.lockin_btn.clicked.connect(self.lock_in_nominees)

    def return_to_main(self):
        self.main_window = Sistema()
        self.main_window.show()
        self.close()

    def is_valid_name(self, name):
        if not name or len(name.strip()) < 2:
            return False
        name_pattern = r"^[A-Za-z\s\-']+$"
        
        return bool(re.match(name_pattern, name.strip()))

    def validate_nominee_name(self, name, position):
        if not name.strip():
            QtWidgets.QMessageBox.warning(self, "Validation Error", f"{position} name cannot be blank!")
            return False
        if not self.is_valid_name(name):
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                f"{position} name '{name}' is invalid!\nNames should only contain letters, spaces, hyphens, and apostrophes."
            )
            return False
        return True

    def lock_in_nominees(self):
        # Validate party list name
        partylist_name = self.enter_partylist_name.text().strip()
        if not partylist_name:
            QtWidgets.QMessageBox.warning(self, "Validation Error", "Party List Name cannot be blank!")
            return
        positions = {
            "President": self.enter_pres.text(),
            "Vice President": self.enter_vice_pres.text(),
            "Local Secretary": self.enter_local_sec.text(),
            "Assistant Secretary": self.enter_ass_sec.text(),
        }
        for position, name in positions.items():
            if not self.validate_nominee_name(name, position):
                return
        valid_senators = []
        for i in range(1, 8):
            senator_name = getattr(self, f"enter_senator{i}").text().strip()
            if senator_name:
                if not self.validate_nominee_name(senator_name, f"Senator {i}"):
                    return
                valid_senators.append(senator_name)
        if not valid_senators:
            QtWidgets.QMessageBox.warning(self, "Validation Error", "At least one Senator name is required!")
            return
        partylist = {
            "partylist_name": partylist_name,
            "moto": self.enter_moto.text().strip(),
            "pres": self.enter_pres.text().strip(),
            "vice_pres": self.enter_vice_pres.text().strip(),
            "local_sec": self.enter_local_sec.text().strip(),
            "ass_sec": self.enter_ass_sec.text().strip(),
            "senators": valid_senators,
        }
        add_nominee(partylist)
        QtWidgets.QMessageBox.information(self, "Success", "Nominees Locked In!")
        self.close()
        self.return_to_main()

class VotePage1(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/vote_page1.ui", self)
        self.setWindowIcon(QIcon("image/sistema.ico"))
        self.setWindowTitle("Sistema")
        self.setFixedSize(self.size()) 
        self.date_manager = DateManager()

        self.back_btn.clicked.connect(self.return_to_main)
        self.vote_now_btn.clicked.connect(self.validate_and_proceed)

        self.date_lbl.setText(datetime.datetime.now().strftime("%B %d, %Y"))
        self.days_left_lbl.setText(self.date_manager.get_days_left())
        self.total_vote_counts.setText(str(total_voter_count))

    def return_to_main(self):
        self.main_window = Sistema()
        self.main_window.show()
        self.close()

    def is_valid_email(self, email):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, email))

    def is_valid_name(self, name):
        if not name or len(name.strip()) < 2:
            return False
        name_pattern = r"^[A-Za-z\s\-']+$"
        return bool(re.match(name_pattern, name.strip()))

    def validate_and_proceed(self):
        voter_name = self.enter_name.text().strip()
        if not voter_name:
            QtWidgets.QMessageBox.warning(self, "Validation Error", "Please enter your name!")
            return
        if not self.is_valid_name(voter_name):
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                "Invalid name format! Name should only contain letters, spaces, hyphens, and apostrophes."
            )
            return
        section = self.enter_section.text().strip()
        if not section:
            QtWidgets.QMessageBox.warning(self, "Validation Error", "Please enter your section!")
            return
        email = self.enter_email.text().strip()
        if not email:
            QtWidgets.QMessageBox.warning(self, "Validation Error", "Please enter your email!")
            return
        if not self.is_valid_email(email):
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                "Invalid email format! Please enter a valid email address."
            )
            return
        voter = {
            "name": voter_name,
            "section": section,
            "email": email,
            "timestamp": datetime.datetime.now().isoformat()
        }
        if not add_voter(voter):
            QtWidgets.QMessageBox.warning(
                self,
                "Error",
                "This email has already been used to vote. Each person may only vote once."
            )
            return
        self.vote_page2 = VotePage2(voter)  
        self.vote_page2.show()
        self.close()

class VotePage2(QtWidgets.QMainWindow):
    def __init__(self, voter: dict = None):
        super().__init__()
        uic.loadUi("ui/vote_page2.ui", self)
        self.setWindowIcon(QIcon("image/sistema.ico"))
        self.setWindowTitle("Sistema")
        self.setFixedSize(self.size()) 
        self.voter = voter 
        self.back_btn.clicked.connect(self.back)
        self.vote_btn.clicked.connect(self.confirm_vote)
        self.populate_comboboxes()

    def back(self):
        self.main_window = VotePage1()
        self.main_window.show()
        self.close()

    def populate_comboboxes(self):
        self.partylist_box.addItem("None")
        self.pres_box.addItem("None")
        self.vice_pres_box.addItem("None")
        self.local_sec_box.addItem("None")
        self.ass_sec_box.addItem("None")
        for partylist in partylist_data:
            partylist_label = f"{partylist['partylist_name']} ({partylist['moto']})"
            self.partylist_box.addItem(partylist_label)
            self.pres_box.addItem(f"{partylist['pres']} / {partylist['partylist_name']}")
            self.vice_pres_box.addItem(f"{partylist['vice_pres']} / {partylist['partylist_name']}")
            self.local_sec_box.addItem(f"{partylist['local_sec']} / {partylist['partylist_name']}")
            self.ass_sec_box.addItem(f"{partylist['ass_sec']} / {partylist['partylist_name']}")
            for idx, senator in enumerate(partylist["senators"], start=1):
                getattr(self, f"senator{idx}_box").addItem("None")
                getattr(self, f"senator{idx}_box").addItem(f"{senator} / {partylist['partylist_name']}")

    def confirm_vote(self):
        global total_voter_count
        
        # Get selected votes
        selected_partylist = self.partylist_box.currentText()
        votes_cast = []
        
        if selected_partylist == "None":
            # Individual candidate voting logic
            positions = {
                'President': self.pres_box,
                'Vice President': self.vice_pres_box,
                'Local Secretary': self.local_sec_box,
                'Assistant Secretary': self.ass_sec_box
            }
            
            # Collect votes for main positions
            for position, box in positions.items():
                if box.currentText() != "None":
                    candidate = box.currentText().split(" / ")[0]
                    votes_cast.append({
                        'position': position,
                        'candidate': candidate
                    })
                    votes[candidate] = votes.get(candidate, 0) + 1
            
            # Collect senator votes
            for idx in range(1, 8):
                senator_vote = getattr(self, f"senator{idx}_box").currentText()
                if senator_vote != "None":
                    senator_name = senator_vote.split(" / ")[0]
                    votes_cast.append({
                        'position': 'Senator',
                        'candidate': senator_name
                    })
                    votes[senator_name] = votes.get(senator_name, 0) + 1
                    
            if not votes_cast:
                QtWidgets.QMessageBox.warning(self, "Invalid Vote", "Please vote for at least one candidate!")
                return
                
        else:
            # Straight party voting logic
            for partylist in partylist_data:
                if f"{partylist['partylist_name']} ({partylist['moto']})" == selected_partylist:
                    # Record votes for all positions
                    positions = {
                        'President': partylist['pres'],
                        'Vice President': partylist['vice_pres'],
                        'Local Secretary': partylist['local_sec'],
                        'Assistant Secretary': partylist['ass_sec']
                    }
                    
                    for position, candidate in positions.items():
                        votes_cast.append({
                            'position': position,
                            'candidate': candidate
                        })
                        votes[candidate] = votes.get(candidate, 0) + 1
                        
                    # Record senator votes
                    for senator in partylist['senators']:
                        votes_cast.append({
                            'position': 'Senator',
                            'candidate': senator
                        })
                        votes[senator] = votes.get(senator, 0) + 1

        # Update voter record with votes cast
        if self.voter:
            self.voter['votes_cast'] = votes_cast
            voter_history.append(self.voter)
        
        total_voter_count += 1
        save_data_to_json()
        
        QtWidgets.QMessageBox.information(self, "Vote Cast", "Your vote has been submitted successfully!")
        self.main_window = Sistema()
        self.main_window.show()
        self.close()

class HomeUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/home.ui", self)
        self.setWindowIcon(QIcon("image/sistema.ico"))
        self.setWindowTitle("Sistema")
        self.setFixedSize(self.size()) 
        self.date_manager = DateManager()   
        self.back_btn.clicked.connect(self.return_to_main)
        self.date_lbl.setText(datetime.datetime.now().strftime("%B %d, %Y"))
        self.days_left_lbl.setText(self.date_manager.get_days_left())
        self.total_vote_counts.setText(str(total_voter_count))
        self.populate_tables()

    def return_to_main(self):
        self.main_window = Sistema()
        self.main_window.show()
        self.close()

    def populate_tables(self):
        for partylist in partylist_data:
            pres_votes = votes.get(partylist["pres"], 0)
            self.president_table.insertRow(self.president_table.rowCount())
            self.president_table.setItem(
                self.president_table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(partylist["pres"])
            )
            self.president_table.setItem(
                self.president_table.rowCount() - 1, 1, QtWidgets.QTableWidgetItem("President")
            )
            self.president_table.setItem(
                self.president_table.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(partylist["partylist_name"])
            )
            self.president_table.setItem(
                self.president_table.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(str(pres_votes))
            )
            vice_pres_votes = votes.get(partylist["vice_pres"], 0)
            self.president_table.insertRow(self.president_table.rowCount())
            self.president_table.setItem(
                self.president_table.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(partylist["vice_pres"])
            )
            self.president_table.setItem(
                self.president_table.rowCount() - 1, 1, QtWidgets.QTableWidgetItem("Vice President")
            )
            self.president_table.setItem(
                self.president_table.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(partylist["partylist_name"])
            )
            self.president_table.setItem(
                self.president_table.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(str(vice_pres_votes))
            )
        for partylist in partylist_data:
            # Local Secretary
            local_sec_votes = votes.get(partylist["local_sec"], 0)
            self.secretary_tbl.insertRow(self.secretary_tbl.rowCount())
            self.secretary_tbl.setItem(
                self.secretary_tbl.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(partylist["local_sec"])
            )
            self.secretary_tbl.setItem(
                self.secretary_tbl.rowCount() - 1, 1, QtWidgets.QTableWidgetItem("Local Secretary")
            )
            self.secretary_tbl.setItem(
                self.secretary_tbl.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(partylist["partylist_name"])
            )
            self.secretary_tbl.setItem(
                self.secretary_tbl.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(str(local_sec_votes))
            )
            ass_sec_votes = votes.get(partylist["ass_sec"], 0)
            self.secretary_tbl.insertRow(self.secretary_tbl.rowCount())
            self.secretary_tbl.setItem(
                self.secretary_tbl.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(partylist["ass_sec"])
            )
            self.secretary_tbl.setItem(
                self.secretary_tbl.rowCount() - 1, 1, QtWidgets.QTableWidgetItem("Assistant Secretary")
            )
            self.secretary_tbl.setItem(
                self.secretary_tbl.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(partylist["partylist_name"])
            )
            self.secretary_tbl.setItem(
                self.secretary_tbl.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(str(ass_sec_votes))
            )
        for partylist in partylist_data:
            for senator in partylist["senators"]:
                senator_votes = votes.get(senator, 0)
                self.senator_tbl.insertRow(self.senator_tbl.rowCount())
                self.senator_tbl.setItem(
                    self.senator_tbl.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(senator)
                )
                self.senator_tbl.setItem(
                    self.senator_tbl.rowCount() - 1, 1, QtWidgets.QTableWidgetItem("Senator")
                )
                self.senator_tbl.setItem(
                    self.senator_tbl.rowCount() - 1, 2, QtWidgets.QTableWidgetItem(partylist["partylist_name"])
                )
                self.senator_tbl.setItem(
                    self.senator_tbl.rowCount() - 1, 3, QtWidgets.QTableWidgetItem(str(senator_votes))
                )
        for partylist in partylist_data:
            self.partylist_tbl.insertRow(self.partylist_tbl.rowCount())
            self.partylist_tbl.setItem(
                self.partylist_tbl.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(partylist["partylist_name"])
            )
            self.partylist_tbl.setItem(
                self.partylist_tbl.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(partylist["moto"])
            )

class EditUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/edit.ui", self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  
        self.setWindowModality(QtCore.Qt.ApplicationModal)  
        self.setFixedSize(self.size()) 
        self.back_btn.clicked.connect(self.close)
        self.edit_btn.clicked.connect(self.launch_edit_nominate)

        for partylist in partylist_data:
            self.partylist_box.addItem(partylist["partylist_name"])

    def launch_edit_nominate(self):
        selected_partylist = self.partylist_box.currentText()
        for partylist in partylist_data:
            if partylist["partylist_name"] == selected_partylist:
                self.close()
                self.edit_nominate_window = EditNominateUI(partylist)
                self.edit_nominate_window.show()
                break

class EditNominateUI(QtWidgets.QMainWindow):
    def __init__(self, partylist):
        super().__init__()
        uic.loadUi("ui/edit_nominate.ui", self)
        self.setWindowIcon(QIcon("image/sistema.ico"))
        self.setWindowTitle("Sistema")
        self.setFixedSize(self.size()) 
        self.partylist = partylist
        self.original_partylist = partylist.copy()  
        self.fill_data()
        self.back_btn.clicked.connect(self.return_to_main)
        self.save_btn.clicked.connect(self.save_changes)

    def return_to_main(self):
        self.main_window = Sistema()
        self.main_window.show()
        self.close()

    def fill_data(self):
        self.enter_partylist_name.setText(self.partylist["partylist_name"])
        self.enter_moto.setText(self.partylist["moto"])
        self.enter_pres.setText(self.partylist["pres"])
        self.enter_vice_pres.setText(self.partylist["vice_pres"])
        self.enter_local_sec.setText(self.partylist["local_sec"])
        self.enter_ass_sec.setText(self.partylist["ass_sec"])
        
        # Fill senator fields
        for idx, senator in enumerate(self.partylist["senators"], start=1):
            if idx <= 7:  # Ensure we don't exceed the UI fields
                getattr(self, f"enter_senator{idx}").setText(senator)

    def validate_changes(self):
        required_fields = {
            "Party List Name": self.enter_partylist_name.text().strip(),
            "President": self.enter_pres.text().strip(),
            "Vice President": self.enter_vice_pres.text().strip(),
            "Local Secretary": self.enter_local_sec.text().strip(),
            "Assistant Secretary": self.enter_ass_sec.text().strip(),
        }
        for field_name, value in required_fields.items():
            if not value:
                QtWidgets.QMessageBox.warning(
                    self,
                    "Validation Error",
                    f"{field_name} cannot be blank! Changes not saved."
                )
                return False
        new_partylist_name = self.enter_partylist_name.text().strip()
        if new_partylist_name.lower() != self.original_partylist["partylist_name"].lower():
            for party in partylist_data:
                if party["partylist_name"].lower() == new_partylist_name.lower():
                    QtWidgets.QMessageBox.warning(
                        self,
                        "Validation Error",
                        "Party List name already exists! Please choose a different name."
                    )
                    return False
        senators = []
        for idx in range(1, 8):
            senator_text = getattr(self, f"enter_senator{idx}").text().strip()
            if senator_text:
                senators.append(senator_text)
        
        if not senators:
            QtWidgets.QMessageBox.warning(
                self,
                "Validation Error",
                "At least one Senator is required! Changes not saved."
            )
            return False

        return True

    def save_changes(self):
        if not self.validate_changes():
            self.fill_data()
            return
        try:
            senators = [
                getattr(self, f"enter_senator{idx}").text().strip()
                for idx in range(1, 8)
                if getattr(self, f"enter_senator{idx}").text().strip()
            ]
            self.partylist.update({
                "partylist_name": self.enter_partylist_name.text().strip(),
                "moto": self.enter_moto.text().strip(),
                "pres": self.enter_pres.text().strip(),
                "vice_pres": self.enter_vice_pres.text().strip(),
                "local_sec": self.enter_local_sec.text().strip(),
                "ass_sec": self.enter_ass_sec.text().strip(),
                "senators": senators
            })
            save_data_to_json()
            
            QtWidgets.QMessageBox.information(
                self,
                "Success",
                "Changes saved successfully!"
            )
            self.close()
            
        except Exception as e:
            QtWidgets.QMessageBox.critical(
                self,
                "Error",
                f"Failed to save changes: {str(e)}"
            )
            self.fill_data()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = Sistema()
    main_window.show()
    sys.exit(app.exec_())
