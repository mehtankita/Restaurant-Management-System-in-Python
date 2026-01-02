import json
from app.menu.allmenu import Menu
from app.auth.login import Login
import uuid
class AuthSystem:
    def __init__(self):
        self.file = r"app\database\users.json"
        self.menu = Menu()  

    def load_users(self):
        try:
            with open(self.file, "r") as f:
                return json.load(f)
        except:
            return {}

    def save_users(self, users):
        with open(self.file, "w") as f:
            json.dump(users, f, indent=4)

    def signup(self):
        users = self.load_users()
        name = input("Enter username: ")
        email = input("Enter email: ")
        contact = input("Enter contact number: ")
        password = input("Enter password: ")

        users[name] = {
            "id": uuid.uuid4().hex[:5],
            "email": email,
            "contact": contact,
            "password": password,
            "role": "staff"
        }
        self.save_users(users)
        print("Signup successful")  

    def run(self):
        while True:
            self.menu.main_menu()
            choice = input("Choose: ")
    
            if choice == "1":
                users = self.load_users()   
                ob = Login()
                ob.login_user(users)        
    
            elif choice == "2":
                self.signup()
    
            elif choice == "3":
                print("Thank you, exiting...")
                break
    
            else:
                print("Wrong choice")
    
