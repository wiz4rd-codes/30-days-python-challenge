balance = 100000
o = int(input("Enter 1 for depost money\nEnter 2 for withdraw money\nenter 3 for checking balance\nEnter number : "))
def deposit():
    amount = int(input("Enter amount you want to deposit : "))
    global balance 
    balance = amount + balance
def withdraw():
    amount = int(input("Enter amount you want to withdraw : "))
    global balance
    if(balance >= amount):
        print("Withdraw successful")
        balance = balance - amount
    else:
        print("Insufficient balance")
def show_balance():
    global balance 
    print(f"Your current balance is : {balance}")
if(o==1):
    deposit()
    show_balance()
elif(o==2):
    withdraw()
    show_balance()
elif(o==3):
    show_balance()
else:
    print("invalid number")
