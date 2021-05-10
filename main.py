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
choice_one = input ('You are in a cross road. Where do you want to go? Type "left" or "right"\n')

#Select go to the left
if choice_one.lower() == "left":

  choice_two = input ('You arrive to a lake. Type "boat" to take a boat. Type "swim" to swim across\n')
  #Select take the boat
  if choice_two.lower() == "boat":

    door = input('You arrive at the island. There is a house with three doors. One red, one yellow and one blue. Which color do you choose?\n')

    if door.lower() == "yellow":
      print("You found the treasure. You Win!!")
    elif door.lower() == "red":
      print("You were catched by pirates. Game over.")
    elif door.lower() == "blue":
      print("You were eaten by crocodiles. Game over.")
    else:
      print("Wrong choice. Game over.")
  else:
    print("You were eaten by sharks. Game over.)
else:
  print("You fell down in a hole. Game over.")
  


