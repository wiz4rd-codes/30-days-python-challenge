class Mobile : 
    def __init__(self,b,m,p):
        self.brandname = b
        self.modelname = m
        self.price = p
    def display(self):
        print(f"Brand name : {self.brandname}")
        print(f"Model name : {self.modelname}")
        print(f"Price : {self.price}\n")
n = int(input("How many mobiles do you want to enter : "))
m = []
for i in range (0, n):
    brandname= input("Enter Brand name : ")
    modelname = input("Enter Model name : ")
    price = int(input("Enter Price : "))
    mobile = Mobile(brandname,modelname,price)
    m.append(mobile)
for i,mobile in enumerate(m, start = 1):
    print(f"\nMobile Number : {i}")
    mobile.display()

