it = int(input("Enter total number of items : "))
items = []
for i in range (0,it): 
    item = input(f"Enter item number {i+1} : ")
    items.append(item)

def show_item(items): 
    for it_n , item in enumerate (items, start = 1 ):
        print(f"{it_n}. {item}","Long Name" if len(item) >5 else "Short Name")

if __name__ == "__main__":
    show_item(items)
