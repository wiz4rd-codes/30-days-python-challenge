students = [
    ("s1", 78),
    ("s2", 35),
    ("s3", 92),
    ("s4", 48),
    ("s5", 67)
]
def student_report(students): 
    for i , (name, marks) in enumerate(list, start = 1 ):
            print(f"Student number : {i}\nName of the student : {name}\nMarks of the student : {marks}\n","Result : Pass" if marks>= 40 else "Result : Fail")

if __name__ == "__main__": 
      student_report(students)
