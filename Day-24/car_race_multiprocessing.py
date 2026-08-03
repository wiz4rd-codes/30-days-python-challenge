import multiprocessing
import random
def race(car,q):
    i = 1 
    distance = 0 
    while True:
        print(f"Roound {i} starts !!")
        print(f"Roound {i} finished !!")
        if(random.randint(1,100)>=85):                   
            special = random.choice(["crash","nitro"])
            if(special == "crash"):
                print(f"{car} crashesd , skipped 1 turn ")
                print(f"Total distance coverd : {distance}")
                i +=1 
                continue
            elif(special == "nitro"):
                print(f"{car} got an nitro !")
                distance = distance + 200 
        distance = distance + random.randint(97,220)
        if(distance >= 1000):
            print(f"{car} finished the race")
            break
        else :
            print(f"Total distance coverd : {distance}")
        i +=1 
    q.put(car,i)

num_players = int(input("Enter number of players : "))
players = []
for i in range(0,num_players):
    player = input(f"Enter name of player {i+1} : ")
    players.append(player)

record = []
results = []
for player in players : 
    q = multiprocessing.quene()
    p = multiprocessing.Process(target = race, args = (f"{player}'s car",q))
    record.append(p)
    p.start()
for r in record:
    r.join()
