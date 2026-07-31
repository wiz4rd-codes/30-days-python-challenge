import random

class Player : 
    def __init__(self,name):
        self.name = name 
    hp = 120
    MaxHP = 120
    rage = 0 
    max_rage = 100
    potions = 2 

class Monsters : 
    rage = 0
    def __init__(self,name):
        self.name = name.capitalize()
        if((name).capitalize()=="Goblin"):
            self.hp = 80
            self.special = "Rage Drain"
            
        elif((name).capitalize()=="Skeleton"):
            self.hp = 90
            self.special = "Bone Throw"
            
        elif((name).capitalize()=="Zombie"):
            self.hp = 100
            self.special = "Regenerate"
            
        elif((name).capitalize()=="Orc"):
            self.hp = 120
            self.special = "Heavy Smash"
            
        elif((name).capitalize()=="Dragon"):
            self.hp = 200
            self.special = "Fire Breath"
    def choose_monster():
        print("\n========== CHOOSE MONSTER ==========")
        print("1. Goblin   👺 | HP : 80  | Special : Rage Drain")
        print("2. Skeleton 💀 | HP : 90  | Special : Bone Throw")
        print("3. Zombie   🧟 | HP : 100 | Special : Regenerate")
        print("4. Orc      👹 | HP : 120 | Special : Heavy Smash")
        print("5. Dragon   🐉 | HP : 200 | Special : Fire Breath")

            
name = input("Enter name of the Player : ")
hero = Player(name)

Monsters.choose_monster()
monster_name = input("\nEnter name of the Monster : ")
monster = Monsters(monster_name)

def fight_generator(hero,monster):
   
    while True: 
        if hero.hp >0 and monster.hp>0:
            print("\nChoose a move : ")
            print("Press 1 for Slash ⚔          \nDamage: 10-20 \nRage: +15 \nAccuracy: 100%\n")
            print("Press 2 for Heavy Strike 🪓    \nDamage: 10-20 \nRage: +15 \nAccuracy: 100%\n")
            print("Press 3 for Heal ❤️           \nHeal: +35 HP  \nPotions: -1 \nRage: +10\n")
            print("Press 4 for Blood Rage 😈     \nLose: 15 HP \nGain: +35 Rage")
            if(hero.rage >= 100): print("SPECIAL MOVE UNLOCKED :\nPress 5 for Thunder Break ⚡   Damage: 80 | Requires: 100 Rage | Ultimate")
            move = int(input("\nEnter move : "))
            if(move in [1,2]):
                monster.hp = monster.hp - random.randint(10,20)
                print("\nHero used Slash ⚔ Attack") if (move ==1) else print("Hero used Heavy Strike 🪓 Attack")
                if(hero.rage <= 65) :
                    hero.rage += 15
                else : 
                    hero.rage = hero.max_rage
               
            elif(move == 3 and hero.potions >0):
                print("\nHero used Healing Potion ❤️")
                if(hero.hp<=85):
                    hero.hp = hero.hp + 35  
                else :
                    hero.hp = hero.MaxHP
                if(hero.rage <= 65) :
                    hero.rage += 10
                else : 
                    hero.rage = hero.max_rage
                if(hero.potions>0):
                    hero.potions -=1  
                
               
            elif(move == 4):
                print("\nHero use Blood Rage 😈")
                hero.hp -= 15 
                if(hero.rage <= 65) :
                    hero.rage += 35
                else : 
                    hero.rage = hero.max_rage
                
            elif(hero.rage >= 100 and move == 5):
                print("\n========ULTIMATE MOVE========\n")
                monster.hp -= 80
                hero.rage = 0
                
            print()
            print("Hero HP : ",hero.hp)if(hero.hp >= 0 and hero.hp <= hero.MaxHP) else print("Monster HP : 0 ")
            print(f"Potion : {hero.potions}")
            print(f"Monster HP : {monster.hp}")if(monster.hp >= 0) else print("Monster HP : 0 ")
            print(f"Rage : {hero.rage}\n")
        elif(monster.hp <= 0 or hero.hp <= 0):
            if(monster.hp <= 0):
                print("🏆 VICTORY!")
            else:
                print("You Lose !!")
            return
        
            
        yield "Monster's Turn"
            
        if hero.hp >0 and monster.hp>0:
            if(monster.rage >= 100):
                print("==========SPECIAL MOVE==========")
                print(f"Move : {monster.special}")
                if(monster.name == "Goblin"):
                    if(hero.rage > 25):
                        hero.rage -= 25 
                    else :
                        hero.rage = 0
                elif(monster.name == "Skeleton"):
                    hero.hp -= random.randint(25,32)
                elif(monster.name == "Zombie"):
                    monster.hp += random.randint(12,20)
                elif(monster.name == "Orc"):
                    hero.hp -= random.randint(30,40)
                elif(monster.name == "Dragon"):
                    hero.hp -= random.randint(37,50)
                monster.rage = 0
            else : 
                move = random.randint(1,3)
                if (move in [2,3]):
                    print("Monster use Basic Attack 👊") if(move == 2) else print("Monster use Claw Attack 🩸")
                    monster.rage += 10
                    hero.hp -= random.randint(10,20)
                else:
                    print("Monster use Power Strike 🔥")
                    monster.rage += 15
                    hero.hp -= random.randint(15,25)
            print()
            print("Hero HP : ",hero.hp)if(hero.hp >= 0 and hero.hp <= hero.MaxHP) else print("Monster HP : 0 ")
            print(f"Potion : {hero.potions}")
            print(f"Monster HP : {monster.hp}")if(monster.hp >= 0) else print("Monster HP : 0 ")
            print(f"Rage : {hero.rage}\n")
        elif(monster.hp <= 0 or hero.hp <= 0):
            if(monster.hp <= 0):
                print("🏆 VICTORY!")
            else:
                print("You Lose !!")
            return
        
        yield f"\n{hero.name}'s Turn\n"
            
                
g = fight_generator(hero,monster)
for i in g:
     print(i)
