class Course : 

    def __init__(self,course_name,instructor):
        self.course_name = course_name
        self.instructor = instructor

    def display_course(self):
        print(f"Course Name : {self.course_name}")
        print(f"Instructor : {self.instructor}\n")

class Programming (Course):

    def __init__(self, course_name, instructor,programming_language,duration):
        Course.__init__(self,course_name,instructor)
        self.programming_language = programming_language
        self.duration = duration

    def display_programming(self):
        print(f"Programming Language : {self.programming_language}")
        print(f"Duration : {self.duration}\n")

class Design (Course):

    def __init__(self, course_name, instructor,design_tool,projects):
        Course.__init__(self,course_name, instructor)
        self.design_tool = design_tool
        self.projects = projects

    def display_design(self):
        print(f"Design Tool : {self.design_tool}")
        print(f"Projects : {self.projects}\n")

class Fullstack(Programming,Design):

    def __init__(self, course_name, instructor, programming_language, duration,design_tool,projects,certificate,price):
      
        Programming.__init__(self,course_name, instructor,programming_language, duration)
        Design.__init__(self,course_name, instructor,design_tool,projects)
        self.certificate = certificate
        self.price = price

    def display(self):
        Course.display_course(self)
        Programming.display_programming(self)
        Design.display_design(self)
        print(f"Certificate : {self.certificate}")
        print(f"Price : {self.price}\n")

num_full_stack = int(input("How many Full Stack courses do you want to enter : "))
full_stacks = []

for i in range (0,num_full_stack):

    course_name = input("Full Stack Course Name : ")
    instructor = (input("Instructor : "))
    programming_language = (input("Programming Language : "))
    duration = (input("Duratione : "))
    design_tool = (input("Design Tool : "))
    projects = (input("Projects : "))
    certificate = (input("Certificate : "))
    price = int(input("Price : "))
    print()

    full_stack = Fullstack(course_name,instructor,programming_language,duration,design_tool,projects,certificate,price)
    full_stacks.append(full_stack)

for i,full_stack in enumerate(full_stacks, start = 1):
    print(f"Full Stack course Number : {i}")
    full_stack.display()
   


        


