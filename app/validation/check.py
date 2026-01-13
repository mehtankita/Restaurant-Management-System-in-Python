class Validation:
    def contact():
        while True:
            contact=input("Enter your Contact: ")
            if len(contact)==10:
                return int(contact)
            else:
                print("Invalid contact! Enter 10 digit number.")    