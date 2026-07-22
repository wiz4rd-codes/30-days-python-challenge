class Employee :
    def __init__(self,name,id,department,salary):
        self.name = name
        self.id = id
        self.department = department
        self.salary = salary
    def display(self):
        print(f"Name : {self.name}")
        print(f"Employee ID : {self.id}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")
    def annual_salary(self):
        print(f"Annual Salary : {self.salary*12}")
num_ep = int(input("How many employees they want to enter : "))

employees = []
for i in range(0,num_ep): 
    name = input("Enter name of the Employee : ")
    id = int(input("Enter ID of the Employee : "))
    department = input("Enter department of the Employee : ")
    salary = int(input("Enter salary of the Employee : "))
   
    employee =Employee(name,id,department,salary)
    employees.append(employee)
for i , employee in enumerate(employees , start = 1 ):
    print(f"Employee NUmber : {i}")
    employee.display()
    employee.annual_salary()
inspect = input("Do you want to inspect any employee? (Yes/No)\n Enter : ")
if(inspect.capitalize() == "Yes"):
    emp = int(input("Enter employee number you want to inspect : "))
    print(f"All Atrributes and Method : {dir(employees[emp-1])}\n")
    print(f"All instances and variable: {employees[emp-1].__dict__}\n")
    help(Employee)
