def add_notes():
    note = input("Enter your note : ")
    with open("notes.txt", "a") as f:
        f.writelines(note + "\n")
    print("Note saved successfully")


def display_note():
    with open("notes.txt", "r") as f:
        notes = f.readlines()
        for line in notes:
            data = line.strip("\n")
            print(data)


def clear_notes():
    c = input("Are you sure you want to delete all notes?\nEnter yes/no : ")
    if c == "yes":
        with open("notes.txt", "w") as f:
            f.truncate(0)
        print("All notes deleted successfully.\n")
    else:
        print("Operation Cancelled.\n")


while True:
    o = int(input(
        "Enter 1 to Add Note\n"
        "Enter 2 to Display All Notes\n"
        "Enter 3 to Clear All Notes\n"
        "Enter 4 to Exit\n"
        "Enter number : "
    ))

    if o == 1:
        add_notes()
    elif o == 2:
        display_note()
    elif o == 3:
        clear_notes()
    elif o == 4:
        print("Program exited.\n")
        break
    else:
        print("Invalid input.\n")
