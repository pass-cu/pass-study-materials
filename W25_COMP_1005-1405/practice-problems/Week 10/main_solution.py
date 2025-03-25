'''
PASS Week 10 Mini-Assignment.

This program represents a basic university database. It allows the user to add, remove, and view people in the database.
It also allows the ability to save the database into a file.
'''

import os   # Just used to clear the console, if you are on mac/linux, this might not work.
import pprint

# These will be our global variables for the program. Although not good practice, it is not the focus of this demo so you
# may, if you want, try to get rid of the non-constants.
database = {}
DATABASE_FILE = "database.txt"

nextID = 101000000

def add_person() -> None:
    global nextID

    firstName = input("Person First Name: ")
    lastName = input("Person Last Name: ")
    id = nextID
    personelType = input("Personel Type (student/staff): ")

    key = firstName + lastName

    person = {
        "firstName" : firstName,
        "lastName" : lastName,
        "id" : id,
        "personelType" : personelType
        }  

    if (not (key in database.keys())):
        database[key] = []
        database[key].append(person)
    else:
        database[key].append(person)

    nextID += 1

def remove_person() -> None:
    print_database()
    deleteId = int(input("Who do you want to delete by ID?: "))

    keys = database.keys()

    for key in keys:
        person = database[key]
        i = 0
        for duplicate in person:
            if (duplicate["id"] == deleteId):
                person.pop(i)
            i += 1


    input("Press any key to continue..")

def print_database() -> None:
    pprint.pprint(database)
    input("Press any key to continue...")

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
        if (selection == 1):
            add_person()
        if (selection == 2):
            remove_person()
        if (selection == 3):
            print_database()
        if (selection == 0):
            break

    print("Database Program Ended")

main()