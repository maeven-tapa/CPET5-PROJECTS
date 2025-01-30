# Re - Sistema
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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Any, Optional, TypeVar, Generic, List, Dict
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

T = TypeVar('T')

JSON_FILE = "sistema_data.json"

def merge_sort_voters(voters: List[Dict], key: str) -> List[Dict]:
    """
    Merge sort implementation for sorting voters by a specific key
    """
    if len(voters) <= 1:
        return voters

    mid = len(voters) // 2
    left = merge_sort_voters(voters[:mid], key)
    right = merge_sort_voters(voters[mid:], key)
    
    return merge_voters(left, right, key)

def merge_voters(left: List[Dict], right: List[Dict], key: str) -> List[Dict]:
    """
    Merge two sorted lists of voters
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i].get(key, '').upper() <= right[j].get(key, '').upper():
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def binary_search_voter(voters: List[Dict], search_value: str, key: str) -> bool:
    """
    Binary search implementation to find a voter by a specific key
    """
    left = 0
    right = len(voters) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value = voters[mid].get(key, '').upper()
        search_value = search_value.upper()
        
        if mid_value == search_value:
            return True
        elif mid_value < search_value:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

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

def send_email(voter_email, voter_name, votes_cast):
    try:
        sender_email = "sistematupc@gmail.com"  # Replace with your email
        sender_password = "guus mcdm anfp rpca"  # Replace with your email password
        subject = "Your Voting Receipt - Thank You for Voting!"
        smtp_server = "smtp.gmail.com"  # Change if not using Gmail
        smtp_port = 587

        # Prepare the email content
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = voter_email
        message["Subject"] = subject

        # Create the email body
        votes_summary = "\n".join(
            [f"{vote['position']}: {vote['candidate']}" for vote in votes_cast]
        )
        body = f"""
        Dear {voter_name},

        Thank you for participating in the election process. Here is a summary of your votes:

        {votes_summary}

        If you have any questions or concerns, please contact the election committee.

        Best regards,
        Election Committee
        """
        message.attach(MIMEText(body, "plain"))

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

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

        self.update_notes()


    def update_notes(self):
        """Show or hide notes based on the existence of nominations"""
        if not partylist_data:  # No nominations yet
            self.note_1.setText("Note: Voting doesnt start yet, nominate first!")
            self.note_2.setText("before going to Vote and Home")
        else:  # Nominations exist
            self.note_1.setText("")
            self.note_2.setText("")

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

    def is_valid_name_format(self, name):
        """Validate name format (SURNAME, FIRSTNAME M.I.)"""
        name_pattern = r'^[A-Z][a-zA-Z\s\-\']+,\s[A-Z][a-zA-Z\s\-\']+(?:\s[A-Z]\.)?$'
        return bool(re.match(name_pattern, name.strip()))

    def is_candidate_already_nominated(self, candidate_name):
        """Check if candidate is already nominated in any party list"""
        for party in partylist_data:
            # Check president
            if party['pres'].upper() == candidate_name.upper():
                return True, 'President', party['partylist_name']
            
            # Check vice president
            if party['vice_pres'].upper() == candidate_name.upper():
                return True, 'Vice President', party['partylist_name']
            
            # Check local secretary
            if party['local_sec'].upper() == candidate_name.upper():
                return True, 'Local Secretary', party['partylist_name']
            
            # Check assistant secretary
            if party['ass_sec'].upper() == candidate_name.upper():
                return True, 'Assistant Secretary', party['partylist_name']
            
            # Check senators
            for senator in party['senators']:
                if senator.upper() == candidate_name.upper():
                    return True, 'Senator', party['partylist_name']
        
        return False, '', ''

    def validate_nominee_name(self, name, position):
        if not name.strip():
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                f"{position} name cannot be blank!"
            )
            return False
            
        if not self.is_valid_name_format(name):
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                f"{position} name '{name}' is invalid!\nUse format: SURNAME, FIRSTNAME M.I.\nExample: Cruz, Zyaire D."
            )
            return False
            

        is_nominated, existing_position, existing_party = self.is_candidate_already_nominated(name)
        if is_nominated:
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                f"'{name}' is already nominated as {existing_position} in {existing_party}!\n" +
                "A candidate can only be nominated once."
            )
            return False
            
        return True

    def lock_in_nominees(self):

        partylist_name = self.enter_partylist_name.text().strip()
        if not partylist_name:
            QtWidgets.QMessageBox.warning(self, "Validation Error", "Party List Name cannot be blank!")
            return
        

        if any(party['partylist_name'].upper() == partylist_name.upper() for party in partylist_data):
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                "This Party List name already exists! Please choose a different name."
            )
            return


        positions = {
            "President": self.enter_pres.text().strip(),
            "Vice President": self.enter_vice_pres.text().strip(),
            "Local Secretary": self.enter_local_sec.text().strip(),
            "Assistant Secretary": self.enter_ass_sec.text().strip(),
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
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                "At least one Senator name is required!"
            )
            return

        partylist = {
            "partylist_name": partylist_name,
            "moto": self.enter_moto.text().strip(),
            "pres": positions["President"],
            "vice_pres": positions["Vice President"],
            "local_sec": positions["Local Secretary"],
            "ass_sec": positions["Assistant Secretary"],
            "senators": valid_senators,
        }

        add_nominee(partylist)
        QtWidgets.QMessageBox.information(
            self, 
            "Success", 
            "Nominees successfully locked in!"
        )
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
        # Pattern for "SURNAME, FIRSTNAME M." or "SURNAME, FIRSTNAME" format
        name_pattern = r'^[A-Z][a-zA-Z\s\-\']+,\s[A-Z][a-zA-Z\s\-\']+(?:\s[A-Z]\.)?$'
        return bool(re.match(name_pattern, name.strip()))

    def is_valid_section(self, section):
        # Pattern for "PROGRAM-COURSE-YEAR" format (e.g., BET-COET-2A)
        section_pattern = r'^[A-Z]{2,4}-[A-Z]{2,4}-[1-4][A-Z]$'
        return bool(re.match(section_pattern, section.strip()))

    def is_valid_student_id(self, student_id):
        # Pattern for "TUPC-YY-NNNN" format (e.g., TUPC-23-0256)
        student_id_pattern = r'^TUPC-\d{2}-\d{4}$'
        return bool(re.match(student_id_pattern, student_id.strip()))

    def has_voted_before(self, name: str, student_id: str, email: str) -> bool:
        """
        Check if a student has voted before using sorting and binary search
        """
        previous_voters = voter_history.get_all()
        
        # Sort voters by different keys and check each
        # By Name
        voters_by_name = merge_sort_voters(previous_voters, 'name')
        if binary_search_voter(voters_by_name, name, 'name'):
            return True
            
        # By Student ID
        voters_by_id = merge_sort_voters(previous_voters, 'student_id')
        if binary_search_voter(voters_by_id, student_id, 'student_id'):
            return True
            
        # By Email
        voters_by_email = merge_sort_voters(previous_voters, 'email')
        if binary_search_voter(voters_by_email, email, 'email'):
            return True
            
        return False

    def validate_and_proceed(self):
        # Get and clean input values
        voter_name = self.enter_name.text().strip().upper()
        section = self.enter_section.text().strip().upper()
        email = self.enter_email.text().strip()
        student_id = self.enter_studentid.text().strip().upper()

        # Validation for name format
        if not voter_name:
            QtWidgets.QMessageBox.warning(self, "Validation Error", "Please enter your name!")
            return
        if not self.is_valid_name(voter_name):
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                "Invalid name format! Please use format: SURNAME, FIRSTNAME M.I.\nExample: AMADOR, SIEGMOND B."
            )
            return

        # Validation for section
        if not section:
            QtWidgets.QMessageBox.warning(self, "Validation Error", "Please enter your section!")
            return
        if not self.is_valid_section(section):
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                "Invalid section format! Please use format: PROGRAM-COURSE-YEAR\nExample: BET-COET-2A"
            )
            return

        # Validation for student ID
        if not student_id:
            QtWidgets.QMessageBox.warning(self, "Validation Error", "Please enter your Student ID!")
            return
        if not self.is_valid_student_id(student_id):
            QtWidgets.QMessageBox.warning(
                self, 
                "Validation Error", 
                "Invalid Student ID format! Please use format: TUPC-YY-NNNN\nExample: TUPC-23-0256"
            )
            return

        # Validation for email
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

        # Check for duplicate votes using merge sort and binary search
        if self.has_voted_before(voter_name, student_id, email):
            QtWidgets.QMessageBox.warning(
                self,
                "Error",
                "This student has already voted. Each student may only vote once."
            )
            return

        # Create voter record
        voter = {
            "name": voter_name,
            "section": section,
            "student_id": student_id,
            "email": email,
            "timestamp": datetime.datetime.now().isoformat()
        }

        # Add voter and proceed
        if not add_voter(voter):
            QtWidgets.QMessageBox.warning(
                self,
                "Error",
                "An error occurred while recording your information. Please try again."
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
            voter_email = self.voter["email"]
            voter_name = self.voter["name"]
            send_email(voter_email, voter_name, votes_cast)
        
        total_voter_count += 1
        save_data_to_json()
        
        QtWidgets.QMessageBox.information(self, "Vote Cast", "Your vote has been submitted successfully! A confirmation email has been sent to your email address.")
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
        
        # Initialize search functionality
        self.setup_search()
        
        # Setup UI elements
        self.back_btn.clicked.connect(self.return_to_main)
        self.date_lbl.setText(datetime.datetime.now().strftime("%B %d, %Y"))
        self.days_left_lbl.setText(self.date_manager.get_days_left())
        self.total_vote_counts.setText(str(total_voter_count))
        
        # Create data structures for efficient searching
        self.candidate_tree = self.build_candidate_tree()
        self.partylist_tree = self.build_partylist_tree()
        
        # Populate tables
        self.populate_tables()

    def setup_search(self):
        """Setup search box connections"""
        self.search_box1.textChanged.connect(self.search_candidates)
        self.search_box2.textChanged.connect(self.search_partylist)
        
        # Style for highlighted items
        self.highlight_style = "background-color: yellow;"
        self.normal_style = ""

    class TreeNode:
        """Binary Search Tree Node"""
        def __init__(self, key, data):
            self.key = key
            self.data = data
            self.left = None
            self.right = None

    def insert_to_tree(self, root, key, data):
        """Insert node into binary search tree"""
        if not root:
            return self.TreeNode(key, data)
        
        if key < root.key:
            root.left = self.insert_to_tree(root.left, key, data)
        else:
            root.right = self.insert_to_tree(root.right, key, data)
        return root

    def build_candidate_tree(self):
        """Build BST for candidate data"""
        root = None
        for partylist in partylist_data:
            # Add executive positions
            for position, candidate in [
                ("President", partylist["pres"]),
                ("Vice President", partylist["vice_pres"]),
                ("Local Secretary", partylist["local_sec"]),
                ("Assistant Secretary", partylist["ass_sec"])
            ]:
                data = {
                    "name": candidate,
                    "position": position,
                    "partylist": partylist["partylist_name"],
                    "votes": votes.get(candidate, 0)
                }
                root = self.insert_to_tree(root, candidate.upper(), data)
            
            # Add senators
            for senator in partylist["senators"]:
                data = {
                    "name": senator,
                    "position": "Senator",
                    "partylist": partylist["partylist_name"],
                    "votes": votes.get(senator, 0)
                }
                root = self.insert_to_tree(root, senator.upper(), data)
        return root

    def build_partylist_tree(self):
        """Build BST for partylist data"""
        root = None
        for partylist in partylist_data:
            data = {
                "name": partylist["partylist_name"],
                "moto": partylist["moto"]
            }
            root = self.insert_to_tree(root, partylist["partylist_name"].upper(), data)
        return root

    def search_tree(self, root, search_text):
        """Search BST and return matching nodes"""
        results = []
        def inorder_search(node):
            if not node:
                return
            inorder_search(node.left)
            if search_text in node.key:
                results.append(node.data)
            inorder_search(node.right)
        
        inorder_search(root)
        return results

    def search_candidates(self):
        """Search and highlight candidate matches in tables"""
        search_text = self.search_box1.text().strip().upper()
        
        # Reset all highlighting
        self.reset_table_highlighting(self.president_table)
        self.reset_table_highlighting(self.secretary_tbl)
        self.reset_table_highlighting(self.senator_tbl)
        
        if not search_text:
            return
            
        # Search using BST
        matches = self.search_tree(self.candidate_tree, search_text)
        
        if not matches:
            self.show_notice("No candidates found matching your search.")
            return
        
        # Highlight matches in appropriate tables
        for match in matches:
            table = self.get_table_for_position(match["position"])
            self.highlight_table_rows(table, match["name"])

    def search_partylist(self):
        """Search and highlight partylist matches"""
        search_text = self.search_box2.text().strip().upper()
        
        # Reset highlighting
        self.reset_table_highlighting(self.partylist_tbl)
        
        if not search_text:
            return
            
        # Search using BST
        matches = self.search_tree(self.partylist_tree, search_text)
        
        if not matches:
            self.show_notice("No partylist found matching your search.")
            return
        
        # Highlight matches
        for match in matches:
            self.highlight_table_rows(self.partylist_tbl, match["name"])

    def show_notice(self, message):
        """Show a message box for 'Not Found' notices"""
        QMessageBox.information(self, "Search Result", message)

    def get_table_for_position(self, position):
        """Return appropriate table based on position"""
        if position in ["President", "Vice President"]:
            return self.president_table
        elif position in ["Local Secretary", "Assistant Secretary"]:
            return self.secretary_tbl
        else:
            return self.senator_tbl

    def reset_table_highlighting(self, table):
        """Reset highlighting in a table"""
        for row in range(table.rowCount()):
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item:
                    item.setBackground(QtGui.QColor("white"))

    def highlight_table_rows(self, table, search_text):
        """Highlight rows containing search text in a multi-column table"""
        highlight_color = QtGui.QColor("#fcb3b3")  # Matching the stylesheet background color
        default_color = QtGui.QColor("white")  # Default background color

        search_text = search_text.strip().lower()  # Normalize the search text
        for row in range(table.rowCount()):
            row_matches = False
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item:
                    # Normalize the text for comparison
                    cell_text = item.text().strip().lower()
                    if search_text in cell_text:
                        row_matches = True

            # Highlight entire row if any cell matches
            for col in range(table.columnCount()):
                item = table.item(row, col)
                if item:
                    if row_matches:
                        item.setBackground(highlight_color)
                    else:
                        item.setBackground(default_color)
                        
    def populate_tables(self):
        """Populate all tables with data"""
        # Clear existing data
        self.president_table.setRowCount(0)
        self.secretary_tbl.setRowCount(0)
        self.senator_tbl.setRowCount(0)
        self.partylist_tbl.setRowCount(0)
        
        # Populate tables using the same logic as before
        for partylist in partylist_data:
            # President table
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
            
            # Vice President
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
            
            # Secretary table
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
            
            # Assistant Secretary
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
            
            # Senator table
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
            
            # Partylist table
            self.partylist_tbl.insertRow(self.partylist_tbl.rowCount())
            self.partylist_tbl.setItem(
                self.partylist_tbl.rowCount() - 1, 0, QtWidgets.QTableWidgetItem(partylist["partylist_name"])
            )
            self.partylist_tbl.setItem(
                self.partylist_tbl.rowCount() - 1, 1, QtWidgets.QTableWidgetItem(partylist["moto"])
            )

    def return_to_main(self):
        self.main_window = Sistema()
        self.main_window.show()
        self.close()

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
