from app.domain.read_write import Read_Write

class MenuManage:

    @staticmethod
    def add_item():
        menu = Read_Write.load_menu()

        category = input("Enter category name: ").title()

        name = input("Enter item name: ")
        type_ = input("Enter type (Veg / Non-Veg or -): ")
        half_price = int(input("Enter half price: "))
        full_price = int(input("Enter full price: "))

        new_item = {
            "name": name,
            "type": type_,
            "half_price": half_price,
            "full_price": full_price
        }

        if category in menu:
            menu[category].append(new_item)
        else:
            menu[category] = [new_item]

        Read_Write.save_menu(menu)
        print("\nItem added successfully\n")
