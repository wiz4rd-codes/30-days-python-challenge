import time 
accounts = [
    {"name": "Harry", "acc_no": 1001, "balance": 25000},
    {"name": "Rahul", "acc_no": 1002, "balance": 18000},
    {"name": "Aman", "acc_no": 1003, "balance": 32000},
    {"name": "Rohit", "acc_no": 1004, "balance": 15000},
    {"name": "Priya", "acc_no": 1005, "balance": 28000},
    {"name": "Neha", "acc_no": 1006, "balance": 12000},
    {"name": "Karan", "acc_no": 1007, "balance": 45000}
]
st_time = time.time()
acc_name = input("Enter name of the Account Holder : ")
acc_num = int(input("Enter Account Number : "))
no_acc = 0 

for index ,i in enumerate(accounts) : 
    if(i["name"] == acc_name.capitalize() and i["acc_no"] == acc_num):
        acc_index = index
        no_acc = 1
        break
    
if no_acc == 0 : 
    print("Invalid Account details ") 
    exit()

while True : 
    print("\nPress 1 for Check Balance\nPress 2 for Deposit Money\nPress 3 for Withdraw Money\nPress 4 for Exit")
    op = int(input("Enter : "))
    if(op == 1):
        print(f"\nCurrent Balance : {accounts[acc_index]["balance"]}")
    elif(op==2):
        depo_amount = int(input("\nEnter amount you want to deposit : "))
        if depo_amount > 0:
            accounts[acc_index]["balance"] = accounts[acc_index]["balance"] + depo_amount
            print(f"Money Deposited Successfully\nCurrent Balance : {accounts[acc_index]["balance"]}")
        else : 
            print("Invalid Amount")

    elif(op==3):
        withdraw_amount = int(input("\nEnter amount you want to withdraw : "))
        if withdraw_amount <= 0:
            print("Invalid Amount")
        elif(accounts[acc_index]["balance"] >= withdraw_amount):
            accounts[acc_index]["balance"] = accounts[acc_index]["balance"] - withdraw_amount
            print(f"Money Withdrawed Successfully\nCurrent Balance : {accounts[acc_index]["balance"]}")
        else : 
            print("Insufficient Balance")

    elif(op==4):
        print("Exited Successfully ")
        break
    else : 
        print("Invalid operation ")

end_time = time.time()
total_time = end_time - st_time
minutes = int(total_time/60)
seconds = int(total_time%60)
print(f"Session Duration : {minutes} min {seconds} sec")
        

