import uuid
from app.domain.read_write import Read_Write
from app.validation.check import Validation

class AuthSystem:

    @staticmethod
    def signup():
        userslist = Read_Write.load_users()

        name = input("Enter username: ")
        email = input("Enter email: ")
        contact = Validation.contact()
        password = input("Enter password: ")

        user = {
            "id": uuid.uuid4().hex[:5],
            "name": name,
            "email": email,
            "contact": contact,
            "password": password,
            "role": "staff"
        }
        userslist.append(user) 
        Read_Write.save_users(userslist)

        print("Signup successful")
