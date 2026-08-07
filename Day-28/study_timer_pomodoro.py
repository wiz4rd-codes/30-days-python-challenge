import time 
study = int(input("Enter study time in minutes : "))
rest =int(input("Enter break time in minutes : "))
i = 1
while True:
    print(f"session {i} started......")
    time.sleep(study*60)
    print(f"Session {i} completed take a {rest} minutes break")
    time.sleep(rest*60)
    print("Break Over!")
    if((e := input("Enter stop to quit the program or Press \"enter\" to continue : ")).lower() == "stop"):
        print(f"Session completed today : {i}")
        print(f"Studied for {i*study} minutes")
        break
    i +=1 
