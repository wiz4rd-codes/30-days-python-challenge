o = int(input("Enter 1 for Storing student record\nEnter 2 for Display student record\nEnter your number : "))
def store_data():
n = int(input("Enter total number of students : "))
for i in range (0,n):
name = input(f"Enter name of the student number {i+1} : ")
roll = int(input(f"Enter roll no. of the student number {i+1} : "))
marks = int(input(f"Enter marks of the student number {i+1} : "))
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
   
    print(f"File pointer is at {f.tell()} at the end of the file ")

if(o ==1):
store_data()
elif(o==2):
display_data()
else:
print("Invalid input")

