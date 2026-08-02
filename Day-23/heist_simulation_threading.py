import random 
import threading
crew = [("Hacker", 85,"Security"),("Lockpicker", 75,"Vault"),("Explosives Expert", 90,"Breach"),("Driver", 80, "Escape")]
heist_status ={
    "Security": False,
    "Vault": False,
    "Breach": False,
    "Escape": False,
}
def heist(crew_member):
    print(f"{crew_member[0]} startes work......\n")
    if(crew_member[1]>= random.randint(1,100)):
        print(f"{crew_member[0]} succeeded!\n")
        heist_status[crew_member[2]] = True
        return True 
    else : 
        print(f"{crew_member[0]} fails !\n")
        return False 
threads = []
for crew_member in crew : 
    t = threading.Thread(target = heist, args = (crew_member,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
if all(heist_status.values()):
    print("Mission Successful")
else:
    print("Mission Failed")
