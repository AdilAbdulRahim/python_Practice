import json
import os

FILE_NAME = "user_data.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []
        
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_user(user):
    data = load_data()
    data.append(user)
    save_data(data)

def get_all_users():
    return load_data()
