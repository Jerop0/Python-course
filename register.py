import uuid
from data import *
from valid import *
from login import *
def register():
    users = read_all_data()

    i = 0
    while i < 6:

        if i == 0:
            first_name = input("First name: ")
            if first_name.isalpha():
                i += 1
            else:
                print("First name must contain only letters")

        elif i == 1:
            last_name = input("Last name: ")
            if last_name.isalpha():
                i += 1
            else:
                print("Last name must contain only letters")

        elif i == 2:
            email = input("Email: ")
            if not valid_email(email):
                print("Invalid email")
            else:
                exists = False
                for user in users:
                    if user["email"] == email:
                        exists = True
                        break

                if exists:
                    print("Email already exists")
                else:
                    i += 1

        elif i == 3:
            password = input("Password: ")
            if len(password)>7:
                i += 1
            else:
                print("Password must be at least 8 chars")
        elif i == 4:    
            confirm_password = input("Confirm Password: ")

            valid_pass, msg = valid_password(password, confirm_password)
            if not valid_pass:
                print(msg)
            else:
                i += 1

        elif i == 5:
            phone = input("Phone: ")
            if not valid_phone(phone):
                print("Invalid phone number")
            else:
                i += 1

    new_user = {
        "id": str(uuid.uuid4()),
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "is_active": True
    }

    users.append(new_user)
    save_data(users)

    print("User registered successfully!")
    login()
