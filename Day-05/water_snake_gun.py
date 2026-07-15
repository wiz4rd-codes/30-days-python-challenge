import random 
def game(computer,user):
    if((computer== 0 and user ==1) or (computer== 1 and user ==2) or(computer== 2 and user ==0)):
        print("Computer Wins!")
        return
    elif(computer== user):
        print("It's a draw")
    else: 
        print("You Win!")
    
computer = random.randint(0,2)
user = int(input("Enter 0 for Snake\nEnter 1 for Water \nEnter 2 for Gun\nWhat do you want to choose : "))
if user not in [0,1,2]:
    raise ValueError("Invalid choice !")
print("Computer chose : ",computer)
game(computer, user)
