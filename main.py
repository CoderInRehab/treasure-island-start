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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("Wait! There is a truck blocking the road ahead! Take a different route")
direction = input("Which direction would you like to take? left or right? \t").lower()
# print(direction)
if direction == "left":
  print("Whew!!! You survived the pit! Good Work there! \n Keep moving forward!")
  print("After moving fwd for many miles in the hot sun, you come across a river. You see an abondoned house across the river!\n")
  print("There are two options now!")
  choice = input("Would you like to 'swim' across the river or you want to 'wait' for a boat/ship? \t").lower()
  if choice == "wait":
    print("So you waited for the boat!\n A ship arrives and takes you to the other side of the river. So you survived a river full of crocodiles\n")
    print("You check the house! you sense the Golds somewhere near! wait, there are three doors ahead in three different colors ('Red','Black','Blue')!\n One of them leads to treasure! Choose wisely! ")
    door = input("Which door you want to enter? Red/Black/Blue\t").lower()
    if door == "red":
      print("You open the door! It\'s the Fire room! Fire Everywhere!!! I\'m sorry, you couldn\'t survive that!\n****************************GAME OVER****************************** ")
    elif door == "blue":
      print("You open the door! It\'s a freezing room! You froze to death! I\'m sorry, you couldn\'t survive that!\n****************************GAME OVER****************************** ")
    elif door == "black":
      print("Everything seems dark here but you see some lights coming from a place ahead, you run to that place, see a box. You open the box carefully!\nWhoaaaaaaaaa!!!!! You hit a jackpot! It\'s a box full of golds and jewels. It\'s your treasure\n************** congratulations for winning the treasure*****************************")
    else:
      print("You tried something different.... you keep trying different things. Oops!! There is a large storm approaching and you swept away with the storms !!!\n****************************GAME OVER****************************** ")
  else:
    print("Oh my God! the river was full of crocodiles! They ate every bit of you!\n**************************GAME OVER*********************************\n")
else:
  print("Oops! there was a huge pit on the road. You fell in the pit and died instantly!\n************************* GAME OVER************************\n ")