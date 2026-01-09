class Menu:
    @staticmethod
    def main_menu():
         print("\n=== MAIN MENU ===")
         print("1. Login")
         print("2. Signup")
         print("3. Exit")
    @staticmethod
    def admin_menu():
        print("========Admin Dashbord========")
        print("1. view menu")
        print("2. manage menu")
        print("3.manage staff")
        print("4.manage orders")
        print("5.manage tables")
        print("6.view reports")
        print("7.logout")
        choice=input("plese enter your choice")
        return choice
    @staticmethod
    def staff_menu():
        while True:
            print("==========staff deshboard==========")
            print("1. view menu")
            print("2.take orders")
            print("3.view orders")
            print("4.update order status")
            print("5.generate bill")
            print("6.table booking")
            print("7. logout")
            choice=input("plese enter your choice")
            return choice







        
            

                    