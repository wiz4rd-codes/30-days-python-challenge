class Animal : 
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
    def sound(self):
        print("Animal makes different sounds\n")
class Cat(Animal): 

    def __init__(self, name, age , breed , color):
        super().__init__(name, age)
        self.breed = breed 
        self.color = color 

    def display(self):
        super().display()
        print(f"Breed : {self.breed}")
        print(f"Color : {self.color}")

    def sound(self):
        print("sound : Meow Meow!\n")

num_cat = int(input("How many cats do you want to enter : "))
cats = []

for i in range (0,num_cat):

    name = input("cat Name : ")
    age = int(input("age : "))
    breed = (input("breed : "))
    color = (input("color : "))
    print()

    cat = Cat(name,age,breed,color)
    cats.append(cat)

for i,cat in enumerate(cats, start = 1):
    print(f"cat Number : {i}")
    cat.display()
    cat.sound()
