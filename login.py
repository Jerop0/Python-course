from data import *

def login():
    users = read_all_data()
    print("-*Enter your data to login*-")
    email = input("Email: ")
    password = input("Password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"Welcome {user['first_name']}!")
            return user

    print("Invalid email or password")
