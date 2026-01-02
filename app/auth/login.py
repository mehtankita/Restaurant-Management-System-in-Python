import getpass
from app.menu.allmenu import Menu

class Login:

    def login_user(self, all_data):
        print("======== LOGIN MENU ========")

        email = input("Enter email: ")
        password = getpass.getpass("Enter password: ")

        menu = Menu() 

        for username, item in all_data.items():

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
