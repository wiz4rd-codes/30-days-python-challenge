class Product : 

    def __init__(self,name,price,quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity 
  
    def display(self):
        print(f"Product Name : {self.name}")
        print(f"Price : {self.price}")
        print(f"Quantity : {self.quantity}")
        print(f"Total Price : {self.total_price()}")

    def total_price(self):
        return self.price*self.quantity
    
class DiscountProduct(Product):

    def __init__(self,name,price,quantity,discount_percentage,category):
        super().__init__(name,price,quantity)
        self.discount_percentage = discount_percentage
        self.category = category

    def total_price(self):
        original_price = super().total_price()
        dis_price = original_price*(self.discount_percentage/100)
        return (original_price - dis_price)
    
    def display(self):
        super().display()
        print(f"Category : {self.category}")
        print(f"Discount Percentage : {self.discount_percentage}\n")
        print(f"Final Price : {self.total_price()}")

no_product = int(input("How many products do you want to enter : "))

products = []
for i in range (0,no_product):
    cate = input(f"Product {i+1} is Normal Product or Discount Product \nEnter : ")
    name = input(f"Product Name : ")
    price = int(input(f"Price : "))
    quantity = int(input(f"Quantity : "))

    if(cate.capitalize() == "Discount product" or cate.capitalize() =="Discount"):
        category = input("Category : ")
        discount_percentage = int(input("Discount Percentage : "))
        product = DiscountProduct(name,price,quantity,discount_percentage,category)
        products.append(product)
    else : 
        product = Product(name,price,quantity)
        products.append(product)

for i,product in enumerate(products,start = 1): 
    print(f"Product Number { i }")
    product.display()
