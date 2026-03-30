from login import *
from register import *
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()