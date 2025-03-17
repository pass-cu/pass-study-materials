'''
PASS Week 10 Mini-Assignment.

This program represents a basic university database. It allows the user to add, remove, and view people in the database.
It also allows the ability to save the database into a file.
'''

import os   # Just used to clear the console, if you are on mac/linux, this might not work.

# These will be our global variables for the program. Although not good practice, it is not the focus of this demo so you
# may, if you want, try to get rid of the non-constants.
database = {}
DATABASE_FILE = "database.txt"

def add_person() -> None:
    pass

def remove_person() -> None:
    pass

def print_database() -> None:
    pass

def save_database() -> None:
    pass

def load_database() -> None:
    pass

def print_menu() -> int:
    os.system('cls')    # Clears the console, see comment at import.
    print("===== UNIVERSITY DATABASE =====")
    print("[1] Add Person")
    print("[2] Remove Person")
    print("[3] View Database")
    print("[4] Save Database")
    print("[5] Load Database")
    print("[0] Exit")

    selection = int(input("Select an option: "))
    return selection

def main() -> None:
    while(True):
        # Get user input
        selection = print_menu()

        # Process user input
        if (selection < 0 or selection > 5):
            print("That is not a valid selection!")
        if (selection == 0):
            break

    print("Database Program Ended")

main()