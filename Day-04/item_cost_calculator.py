item_num = int(input("How many items you want to enter :"))
record = []
for i in range ( 0, item_num):
    product_name = input("Enter name of the product : ")
    price = int(input("Enter price of the item : "))
    quantity = int(input(f"Enter total number of {product_name} : ")) 
    record.append((product_name,price,quantity))


# List containing only total cost of each product (used for reduce())
cost = list(map(lambda x :(x[1]*x[2]),record))

# List containing product name and total cost (used for filter() and display)
costwithname = list(map(lambda x :(x[0],x[1]*x[2]),record))
print("Total price of keyboards : ",costwithname,"\n")

greater_thousand = list(filter(lambda x : (x[1]>1000) ,costwithname))
print(f"list of item costlier than 1000 rupees : \n{greater_thousand}\n")

from functools import reduce 
grand_total = (reduce(lambda x,y : x+y, cost ))
print(f"grand total of all the items are : {grand_total}\n")

for i,item in enumerate(record, start = 1) : 
    print(f"{i}.Name of the product : {item[0]}\nPrice of the item : {item[1]}\nTotal number of {item[0]} : {item[2]}")

