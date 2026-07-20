class Gym_member:
    membership_fee = 1500
    def __init__(self,name,age,id):
        self.name = name 
        self.age = age
        self.id = id
    def display(self):
        print(f"Member Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Membership ID : {self.id}")
        print(f"Membership Fee : {self.membership_fee}")
    @classmethod
    def update_fee(cls,new_fee):
        cls.membership_fee = new_fee
no_mem = int(input("How many members do you want to enter : "))
members = []
for i in range(0,no_mem):
    name = input("Enter name of the member : ")
    age = int(input("Enter age of the member : "))
    id = int(input("Enter Membership ID : "))
    member = Gym_member(name,age,id)
    members.append(member)
for i,member in enumerate(members, start = 1):
    print(f"Member number : {i}")
    member.display()
ch = input("Do you want to change Membership fees \nEnter yes or no :")
if(ch.capitalize() == "Yes"):
    new_fee = int(input("Enter new Membership fee : "))
    Gym_member.update_fee(new_fee)
    for i,member in enumerate(members, start = 1):
        print(f"Updated Data\nMember number : {i}")
        member.display()
