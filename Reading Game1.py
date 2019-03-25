#print("") for future andrew ctr + c
import random

def bandit_attack(player_health, bandit_health, player_strength, bandit_strength, weapon,):
     
    print("A bandit attacks you!")
    input("Press Enter to continue")
    print("1 : fight back or 2 : Let them take your gold")
    a = player_input(2)
    if a == 1:
        print("You have " + str(player_health) +" health")
        input("Press Enter to continue")
        print("The bandit has " + str(bandit_health) + " health")
        input("Press Enter to continue") 
        while bandit_health >= 1 and player_health >= 1: 
            bandit_current_strength = random.randrange(1,bandit_strength)  
            current_strength = random.randrange(1,player_strength)  
            bandit_health = attack(weapon, current_strength, bandit_health)
            print("Your attack deals " + str(current_strength) + " damage the bandit has now " + str(bandit_health) + " Health")
            input("Press Enter to continue")
            if not bandit_health <= 0:
                player_health = attack("dagger", bandit_current_strength, player_health)
                print("The bandit attack you for " + str(bandit_current_strength) + " you now have " + str(player_health) + " health")
                input("Press Enter to continue")
        return player_health
    else:
        Money = 0


def wolf_attack(player_health, wolf_health, player_strength, wolf_strength, weapon):
     
    print("A wolf attacks you!")
    input("Press Enter to continue")
    print("1 : attack or 2 : flee")
    a = player_input(2)
    if a == 1:
        print("You have " + str(player_health) +" health")
        input("Press Enter to continue")
        print("The wolf has " + str(wolf_health) + " health")
        input("Press Enter to continue") 
        while wolf_health >= 1 and player_health >= 1: 
            wolf_current_strength = random.randrange(1,wolf_strength)  
            current_strength = random.randrange(1,player_strength + weapon_damage(weapon))  
            wolf_health = attack(weapon, current_strength, wolf_health)
            print("Your attack deals " + str(current_strength) + " damage the wolf has now " + str(wolf_health) + " Health")
            input("Press Enter to continue")
            if not wolf_health <= 0:
                player_health = attack("claw", wolf_current_strength, player_health)
                print("The wolf attack you for " + str(wolf_current_strength) + " you now have " + str(player_health) + " health")
                input("Press Enter to continue")
        return player_health
          
    else:
        print("you died while trying to run away")
        return 0
def weapon_damage(weapon):
    if weapon == "sword":
        return 4
    elif weapon == "none":
        return 1
    elif weapon == "holy":
        return 6
    elif weapon == "demon":
        return 8
    elif weapon == "claw":
        return 2 
    elif weapon == "dagger":
        return 2  
    else:
        raise RuntimeError("You cheated you shouldn't have that weapon")
def player_input(number):
    while True:
        a = input()                                                                        
        if a.isdigit():
            if int(a) > 0 and int(a) <= number:
                return int(a)
            else:
                print("Not a choice")    
        else:
            print("Not a number try again.")





def attack(weapon, strength, enemy_health):
    return enemy_health-weapon_damage(weapon)-strength
          
weapon = "none"
bandit_weapon = "dagger"
wolf_weapon = "claw"
Food = 1
Money = 0
Health1 = 30
Strength1 = 9
bandit = 23
bandit_strength = 8
wolf = 15
wolf_strength = 5
Strength = Strength1 + random.choice([1,2,3,4,5])
Money = Money + random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
Health = Health1 + random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print("Your strength is " + str(Strength1) +" Plus a random number between 1-5. Your Strength equals to " + str(Strength))
print("Your Health is " + str(Health1) +" Plus a random number between 10-20. Your Health equals to " + str(Health))
input("Press Enter to continue")
print("The story beings With you being attacked by bandits and losing most of your belongings")
input("Press Enter to continue")
print("You had a secret pouch of gold that the bandit didn't find. Your gold is a number from 1-15 you have " + str(Money) + " Gold in your pouch. You also have one meal left to eat")
input("Press Enter to continue")
print("When you wake up you see two paths in front of you do you go to the left path or the right path")
print("1 : go right or 2 : go left ")
a = player_input(2)
if a == (1):    
    print("After heading down the right path you get a feeling that something is whatching you")
    input("Press Enter to continue")
    print("1 : continute down the path or 2 : hide in a bush")
    a = player_input(2)
    if a == 1:
        Health = wolf_attack(Health, wolf, Strength, wolf_strength, weapon)   
        if Health <= 0:
            print("You dead the end")
        else:
            print("After surviving the attack you continue along the road.") 
            input("Press Enter to continue")
            print("While walking you see smoke coming across the horizon do you continue down the road or investigate the smoke")
            print("1 : continue down the road or 2 : investigate the smoke")
            a = player_input(2)
            if a == 1:
                print("You ignored the smoke and went along the road")
            else:
                print("You went to investigate the smoke")
                input("Press Enter to continue")
                print("After coming closer you see a hut on fire")
                input("Press Enter to continue")
                print("You run towards the hut to see if anyone is stuck inside")
                input("Press Enter to continue")
                print("You see no one inside and the house looks empty")
                input("Press Enter to continue")
                print("A bandit come's out of hiding and begins to rob you")
                input("Press Enter to continue")   
                Health = bandit_attack(Health, bandit, Strength, bandit_strength, weapon)
    else:
        print("You hid in the bush    (to be continued)  ")   
else:
    print("After walking down the left path an arrow flies out of the bushes and hits you")
    input("Press Enter to continue")
    print("The end you died")