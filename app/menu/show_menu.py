from app.domain.read_write import Read_Write

class Menu_show:

    @staticmethod
    def show_menu_restaurant():
        menu = Read_Write.load_menu()

        print("\n========== RESTAURANT MENU ==========")

        for category, items in menu.items():
            print(f"\n--- {category} ---")
            for idx, item in enumerate(items, start=1):
                print(
                    f"{idx}. {item['name']} | "
                    f"{item['type']} | "
                    f"Half ₹{item['half_price']} | "
                    f"Full ₹{item['full_price']}"
                )

        print("\n====================================\n")

