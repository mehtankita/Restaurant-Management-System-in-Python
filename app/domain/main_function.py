from app.menu.allmenu import Menu
from app.auth.authentication import AuthSystem
from app.auth.login import Login

class MainFunction:
    @staticmethod
    def run():
        while True:
            Menu.main_menu()
            choice = input("Choose: ")
            
            if choice == "1":
                Login.login_user()
            elif choice == "2":
                AuthSystem.signup()
            elif choice == "3":
                print("Bye")
                break
            else:
                print("Invalid option")
