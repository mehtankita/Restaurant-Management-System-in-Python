import json
from app.model.json import Path

class Read_Write:

    @staticmethod
    def load_users():
        try:
            with open(Path.file, "r") as f:
                return json.load(f) 
        except:
            return []  

    @staticmethod
    def save_users(users):
        with open(Path.file, "w") as f:
            json.dump(users, f, indent=4)
