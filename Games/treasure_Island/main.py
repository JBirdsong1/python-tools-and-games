print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
        
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            choice4 = input("You see the treasure chest, but it is locked! Next to it are two keys: a 'gold' key and a 'silver' key. Which do you pick? \n").lower()
            if choice4 == "silver":
                print("The key fits perfectly! You open the chest and find the treasure! You Win!")
            else:
                print("The key snaps inside the lock, triggering a trap door. You fall into darkness. Game Over.")
                
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
            
    elif choice2 == "swim":
        choice_swim = input("You decide to swim. A shadow passes beneath you! Type 'dive' to submerge or 'sprint' to swim faster to the shore. \n").lower()
        if choice_swim == "dive":
            print("You dive down and find an underwater tunnel that leads straight into the hidden treasure vault! You Win!")
        else:
            print("You try to sprint, but you get attacked by a group of piranhas. Game Over.")
    else:
        print("You stood still for too long and vanished. Game Over.")

elif choice1 == "right":
    choice_right = input("You walk down the right path and find a dark cave. Type 'enter' to explore it or 'climb' to scale the mountain above it. \n").lower()
    
    if choice_right == "enter":
        choice_cave = input("Inside the cave, a sleeping dragon blocks the path. Type 'sneak' to crawl past or 'wake' to confront it. \n").lower()
        if choice_cave == "sneak":
            print("Success! You sneak past the dragon and find a secret back entrance to the house of doors! You Win!")
        else:
            print("The dragon wakes up and turns you to ash. Game Over.")
            
    elif choice_right == "climb":
        print("The rocks crumble beneath your feet. You fall into a deep hole. Game Over.")
    else:
        print("You got lost in the woods. Game Over.")

else:
    print("You fell into a hole. Game Over.")