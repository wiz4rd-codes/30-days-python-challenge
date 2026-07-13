o = int(input("Enter 1 for Storing Student Record\nEnter 2 for Display Student Record\nEnter your number : "))


def store_data():
    n = int(input("Enter total number of students : "))

    for i in range(n):
        name = input(f"Enter name of student {i + 1} : ")
        roll = int(input(f"Enter roll number of student {i + 1} : "))
        marks = int(input(f"Enter marks of student {i + 1} : "))

        record = f"{name},{roll},{marks}"

        with open("Student.txt", "a") as f:
            f.writelines(record + "\n")

    print("Student record saved successfully")


def display_data():
    with open("Student.txt", "r") as f:
        f.seek(0)

        full_data = f.readlines()

        for line in full_data:
            data = line.strip("\n")
            print(data)

        print(f"\nFile pointer is at {f.tell()} (End of File)")


if o == 1:
    store_data()
elif o == 2:
    display_data()
else:
    print("Invalid input")
