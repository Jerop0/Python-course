import json

FILE_NAME = "users.json"

def read_all_data():
    try:
        with open(FILE_NAME, "r") as f:
            users = json.load(f)
    except:
        users = []
    return users


def save_data(users: list):
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(users, f, indent=4)
    except:
        return []