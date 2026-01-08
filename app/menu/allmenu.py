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
        print("1. manage menu")
        print("2.manage staff")
        print("3.manage orders")
        print("4.manage tables")
        print("5.view reports")
        print("6.back")
        choice=input("plese enter your choice")
        return choice
    @staticmethod
    def staff_menu():
        while True:
            print("==========staff deshboard==========")
            print("1.take orders")
            print("2.view orders")
            print("3.update order status")
            print("4.generate bill")
            print("5.table booking")
            print("6. back")
            choice=input("plese enter your choice")
            return choice







        
            

                    