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
# start = input("""You have come to a fork in the road. Do you want to go 'left' or 'right'? """)
# water = ("""The winding road finally led to a large stream of water. Do you want to 'swim' across or 'wait' for possible help? """)
# door = ("""You spot a small boat floating down the stream. You decide to hop in and paddle across. Once across you notice a huge set of three colored doors. On the left side an almost translucent 'white' stood before you, in the middle an errie looking 'red' door, and finally on the right most side a 'blue' door that looked to be for a small creature. Destiny awaits, which door will you choose? """)
# if start.lower() == "left":
#   input(water)
#   if water.lower() == "wait":
#     input(door)
#     if door == "white":
#       print("""As you reach out to touch the white door a force repels you back. As your body flies back, your head slams into a medium size blouder and you permentently lose consciousness. GAME OVER.""")
#     elif door == "red":
#       print("""As you build up an limitless amount of confidence you begin to walk towards the red door. Sooner than your brain can react you realize that your whole body has been set ablaze. Nothing so far could prepare you for this torturous end. GAME OVER.""")
#     elif door == "blue":
#       print("""You walk towards the blue door with a belief that this must be the correct choice. As you try to fit inside the door you realize there is no possible way your whole body will fit. Running out of ideas you decide to stick your hand in. After briefly searching, you grab onto something that feels like a lever and pull down. A loud noise rings throughout the open field. As you begin to stand back up you realize that the translucent white door is slightly open. You quicky run inside and find a opened chest filled to the brim with gold. CONGRATULATIONS YOU WIN!! """)
#     else:
#       print("""Countless options lead to fates worse than death. GAME OVER.""")
    
#   else:
#     print("""While trying to swim across you notice something nibbling on your pinky toe. You look down and realize that your surronded by a group of piranhas. You start urgently swimming to the other side but your vision begins to get blurry due to lose of blood. You finally are able to touch the other side of the stream, but you aren't able to pull your body up to safety. GAME OVER.""")
# else:
#   print("""The right side of the path led to a traphole. You were unable to react quick enough. GAME OVER.""")
start = input("You have come to a fork in the road. Do you want to go 'left' or 'right'?\n").lower()
if start == "left":
  water = input("The winding road finally led to a large stream of water. Do you want to 'swim' across or 'wait'?\n").lower()
  if water == "wait":
    door = input("You spot a small boat floating down the stream. You decide to hop in and paddle across. Once across you notice a huge set of three colored doors. On the left side an almost translucent 'white' door stood before you, in the middle an errie looking 'red' door, and finally on the right most side a 'blue' door that looked to be for a small creature. Destiny awaits, which door will you choose?\n").lower()
    if door == "red":
      print("As you build up an limitless amount of confidence you begin to walk towards the red door. Sooner than your brain can react you realize that your whole body has been set ablaze. Nothing so far could prepare you for this torturous end. GAME OVER.")
    elif door == "white":
      print("As you reach out to touch the white door a force repels you back. As your body flies back, your head slams into a medium size blouder and you permentently lose consciousness. GAME OVER.")
    elif door == "blue":
      print("You walk towards the blue door with a belief that this must be the correct choice. As you try to fit inside the door you realize there is no possible way your whole body will fit. Running out of ideas you decide to stick your hand in. After briefly searching, you grab onto something that feels like a lever and pull down. A loud noise rings throughout the open field. As you begin to stand back up you realize that the translucent white door is slightly open. You quicky run inside and find a opened chest filled to the brim with gold. CONGRATULATIONS YOU WIN!!")
    else:
      print("Countless options lead to fates worse than death. GAME OVER.")
  else:
    print("While trying to swim across you notice something nibbling on your pinky toe. You look down and realize that your surronded by a group of piranhas. You start urgently swimming to the other side but your vision begins to get blurry due to lose of blood. You finally are able to touch the other side of the stream, but you aren't able to pull your body up to safety. GAME OVER.")
else:
  print("The right side of the path led to a traphole. You were unable to react quick enough. GAME OVER.")

