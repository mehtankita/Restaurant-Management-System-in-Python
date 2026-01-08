from app.menu.allmenu import Menu
from app.auth.authentication import AuthSystem
from app.domain.read_write import Read_Write
from app.auth.login import Login

class Dashboard:
    @staticmethod
    def run():
        while True:
            Menu.main_menu()
            choice = input("Choose: ")

            if choice == "1":
                users = Read_Write.load_users()
                Login.login_user(users)

            elif choice == "2":
                ob=AuthSystem()
                ob.signup()

            elif choice == "3":
                print("Thank you, exiting...")
                break
            else:
                print("Wrong choice")