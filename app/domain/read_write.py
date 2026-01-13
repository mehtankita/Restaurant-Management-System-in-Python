import json
from app.model.json import Path

class Read_Write:

    @staticmethod
    def load_users():
        try:
            with open(Path.file, "r") as f:
                return json.load(f) 
        except:
            return {}

    @staticmethod
    def load_menu():
        try:
            with open(Path.food, "r") as f:
                return json.load(f) 
        except:
            return {}

    @staticmethod
    def save_users(data):
        with open(Path.file, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def save_menu(menu):
        with open(Path.food, "w") as f:
            json.dump(menu, f, indent=4)        
