class Cricketer : 

    def __init__(self,name ,runs,wickets,matches):
        self.name = name
        self.runs = runs 
        self.wickets = wickets 
        self.matches = matches 

    def __str__(self):
        return f"\nPlayer Name : {self.name}\nRuns : {self.runs}\nWickets : {self.wickets}\nMatches : {self.matches}\n "
    
    def __gt__(self,other):
        return self.runs>other.runs
   
    def __eq__(self, other):
        return self.name == other.name and self.matches == other.matches
    
    def __len__(self):
        return self.matches
    
    def __add__(self,other):
        return Cricketer((self.name +" & " + other.name),(self.runs  + other.runs),(self.wickets + other.wickets),(self.matches  + other.matches))
num_player = int(input("How many players do you want to enter : "))
players = []

for i in range (0,num_player):

    name = input("Player Name : ")
    runs = int(input("Runs : "))
    wickets = int(input("Wickets : "))
    matches = int(input("Matches : "))
    print()

    player = Cricketer(name,runs,wickets,matches)
    players.append(player)

for i,player in enumerate(players, start = 1):
    print(f"Player Number : {i}")
    print(player)
compare = input("Do you want to compare two player \"yes or no\"?\nEnter : ")
if(compare.capitalize()== "Yes"):
    p1 = int(input("Enter number of first player : "))
    p2 = int(input("Enter number of second player : "))
    print(f"{players[p1-1].name} have more runs ") if (players[p1-1]>players[p2-1]) else print(f"{players[p2-1].name} have more runs ")
    print(f"Both player are same") if (players[p1-1]==players[p2-1]) else print("Both are different players ")
    print((players[p1-1]+players[p2-1]))
    print(f"Matches played by {players[p1-1].name} : {len(players[p1-1])}\nMatches played by {players[p2-1].name} : {len(players[p2-1])}")
