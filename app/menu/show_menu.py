from app.domain.read_write import Read_Write

class Menu_show:

    @staticmethod
    def show_menu_restaurant():
        menu = Read_Write.load_menu()

        print("\n" + "=" * 70)
        print(" " * 20 + "RESTAURANT MENU")
        print("=" * 70)

        for category, items in menu.items():
            print(f"\n{category.upper()}")
            print("-" * 70)
            print(f"{'No':<5}{'Item Name':<30}{'Type':<10}{'Half Price':<12}{'Full Price':<12}")
            print("-" * 70)

            for idx, item in enumerate(items, start=1):
                print(
                    f"{idx:<5}"
                    f"{item['name']:<30}"
                    f"{item['type']:<10}"
                    f"Rs {item['half_price']:<9}"
                    f"Rs {item['full_price']:<9}"
                )

        print("\n" + "=" * 70)
        print(" " * 18 + "PLEASE PLACE YOUR ORDER")
        print("=" * 70 + "\n")
