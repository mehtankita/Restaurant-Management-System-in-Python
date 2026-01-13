class Menu:
    
    @staticmethod
    def main_menu():
        print("\n=== MAIN MENU ===")
        print("1. Login")
        print("2. Signup")
        print("3. Exit")

    @staticmethod
    def admin_menu():
        print("\n======== ADMIN DASHBOARD ========")
        print("1. View Menu")
        print("2. Manage Menu")
        print("3. Manage Staff")
        print("4. Manage Tables")
        print("5. View Reports")
        print("6. Logout")
        choice = input("Please enter your choice: ")
        return choice

    @staticmethod
    def manage_menu():
        print("\n------ MANAGE MENU ------")
        print("1. View Menu") 
        print("2. Add new Item")
        print("3. Delete Menu Item")
        print("4. Update Menu Item")
        print("5. Exit")
        choice = input("Please enter your choice: ")
        return choice

    @staticmethod
    def staff_menu():
        print("\n========== STAFF DASHBOARD ==========")
        print("1. View Menu")
        print("2. Take Orders")
        print("3. View Orders")
        print("4. Update Order Status")
        print("5. Generate Bill")
        print("6. Table Booking")
        print("7. Logout")
        choice = input("Please enter your choice: ")
        return choice
