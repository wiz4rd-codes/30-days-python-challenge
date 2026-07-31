import time
import os
print("=================WATER REMINDER=================")
glass = 0 
while (True):
    print("It's Time to Drink Water !!!!")
    os.system(f'say "It\'s Time to Drink Water"')
    drink = input("Do you drink water yes or no ?\nEnter : ")
    if(drink.capitalize()=="Yes"):
        num_glass = int(input("How many glasses of water you drink : "))
        glass += num_glass
        print(f"Total Glasses Drank : {glass}")
    
    choice = input("Press 1 to Exit, Enter to Continue : ")

    if choice == "1":
        break
    else : 
        time.sleep(7200)
