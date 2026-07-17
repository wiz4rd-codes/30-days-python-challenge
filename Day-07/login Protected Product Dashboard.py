from functools import reduce


def login_required(func):
    def login(*args, **kwargs):
        print("Checking Login Credentials...")
        func(*args, **kwargs)
        print("Thank you for visiting.")
    return login

@login_required
def dashboard(items):
    for item in items:
        print(f"{item[0]} = {item[1]}")
     
    expensive = list(filter(lambda x : x[1] >=1000 ,items))
    print(f"{expensive}")
    cost = list(map(lambda x : x[1], items))
    total_price = reduce(lambda x,y : x + y ,cost)
    print(f"{total_price}")

items = [("keyboard",1200),("Mouse",700),("Monitor",150000),("Headphone",2500),("USB cable",300)]
dashboard(items)
