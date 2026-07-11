st = int(input("Enter total number of students : "))
marks = []
for i in range (0, st): 
    m = int(input(f"Enter marks of student number {i+1} : "))
    marks.append(m)


def chk_result(l):
    for i, marks in enumerate(l, start=0):
        print("Student number ",i+1," : ", "Pass" if marks>40 else "Fail")
        

chk_result(marks)
