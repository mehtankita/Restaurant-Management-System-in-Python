import getpass
from app.menu.allmenu import Menu
from app.domain.read_write import Read_Write
from app.menu.show_menu import Menu_show
from app.menu.allmenu import Menu

class Login:
    @staticmethod
    def login_user():
        all_data= Read_Write.load_users()
        print("======== LOGIN MENU ========")

        email = input("Enter email: ")
        password = getpass.getpass("Enter password: ")

        menu = Menu() 
        for item in all_data:
            if item["email"] == email:

                if item["password"] == password:
                    print("Login successful")

                    if item["role"] == "admin":
                        while True:
                            choice=Menu.admin_menu()
                            if choice=="1":
                                Menu_show.show_menu_restaurant()
                            elif choice=="2":
                                Menu.manage_menu()
                            elif choice=="7":
                                print("Logout Successfull")
                                break
                            else:
                                print("Invalid Choice.")

                    elif item["role"] == "staff":
                        while True:
                            choice=Menu.staff_menu()
                            if choice=="1":
                                Menu_show.show_menu_restaurant()
                            elif choice=="7":
                                print("Logout Successfull")
                                break    
                    else:
                        print("User dashboard")

                    return

                else:
                    print("Incorrect password")
                    return

        print("Email not found")
