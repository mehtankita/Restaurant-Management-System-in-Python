import getpass
from app.menu.allmenu import Menu

class Login:
    @staticmethod
    def login_user(all_data):
        print("======== LOGIN MENU ========")

        email = input("Enter email: ")
        password = getpass.getpass("Enter password: ")

        menu = Menu() 
        for item in all_data:
            if item["email"] == email:

                if item["password"] == password:
                    print("Login successful")

                    if item["role"] == "admin":
                        menu.admin_menu()

                    elif item["role"] == "staff":
                        menu.staff_menu()

                    else:
                        print("User dashboard")

                    return

                else:
                    print("Incorrect password")
                    return

        print("Email not found")
