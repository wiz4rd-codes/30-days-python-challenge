import os 
num = int(input("How many people do you want to give a shoutout to : "))
l = []
for i in range(0,num):
    name = input(f"Enter name of person number {i+1} : ")
    l.append(name)
for name in l : 
    os.system(f'say "Shoutout to {name}"')

