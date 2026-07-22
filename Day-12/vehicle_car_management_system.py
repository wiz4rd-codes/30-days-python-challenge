class Vehicle : 
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model 
        self.price = price 
    def display(self):
        print(f"Brand Name : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Price : {self.price}")
class Car(Vehicle):
    def __init__(self,brand,model,price,fuel_type,seating_capacity):
        super().__init__(brand,model,price)
        self.fuel_type = fuel_type
        self.seating_capacity = seating_capacity
    def display(self):
        super().display()
        print(f"Fuel Type : {self.fuel_type}")
        print(f"Seating Capacity : {self.seating_capacity}\n")
no_car = int(input("Hoe many cars do you want to enter : "))
cars = []
for i in range (0,no_car):
    brand = input(f"Brand Name : ")
    model = input(f"Model : ")
    price = int(input(f"Price : "))
    fuel_type = input(f"Fuel Type : ")
    seating_capacity = int(input(f"Seating Capacity : "))

    car = Car(brand,model,price,fuel_type,seating_capacity)
    cars.append(car)

for i,car in enumerate(cars,start = 1):
    print("\nCar NUmber : ",i)
    car.display()
