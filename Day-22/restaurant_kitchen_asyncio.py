import asyncio

print("Restaurant Menu :\nBurger\nPizza\nPasta\nSandwich\nFries")
orders = []
while True:
    item = input("Order name (stop to finish): ")
    if item.capitalize() == "Stop":
        break
    orders.append(item)
async def preparing(order):
    
    if order.capitalize() == "Burger":
        print(f"preparing {order.capitalize()}.......")
        await asyncio.sleep(6) 
        return f"{order.capitalize()} -> Ready"
    elif order.capitalize() == "Pizza":    
        print(f"preparing {order.capitalize()}.......")
        await asyncio.sleep(7)    
        return f"{order.capitalize()} -> Ready"
         
    elif order.capitalize() == "Sandwich":    
        print(f"preparing {order.capitalize()}.......")
        await asyncio.sleep(4)    
        return f"{order.capitalize()} -> Ready"
         
    elif order.capitalize() == "Pasta":
        print(f"preparing {order.capitalize()}.......")
        await asyncio.sleep(5)    
        return f"{order.capitalize()} -> Ready"
   
    elif order.capitalize() == "Fries":
        print(f"preparing {order.capitalize()}.......")
        await asyncio.sleep(3)    
        return f"{order.capitalize()} -> Ready"
         
    else : 
        return (f"Ivalid order : {order}")
tasks = []
for order in orders:
    tasks.append(preparing(order))
async def main():
    results = await asyncio.gather(*tasks)
    print("\n===================KITCHEN REPORT===================")
    for item in results:
     print(item)
    print(f"Total Orders : {len(results)}")
asyncio.run(main())
