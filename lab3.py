from login import *
from register import *
from projects import *

def project_menu(user):
    while True:
        print("\n--- Project Menu ---")
        print("1. Create Project")
        print("2. View Projects")
        print("3. Edit Project")
        print("4. Delete Project")
        print("5. Search by Date")
        print("6. Logout")

        choice = input("Choose: ")

        if choice == "1":
            create_project(user)
        elif choice == "2":
            view_projects()
        elif choice == "3":
            edit_project(user)
        elif choice == "4":
            delete_project(user)
        elif choice == "5":
            search_by_date()
        elif choice == "6":
            break


def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                project_menu(user)   
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
