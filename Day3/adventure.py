print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad = input("You are at a crossroad, where do you want to go? type 'left' or 'right'.  ")

if crossroad == 'left':
  swim_or_wait = input ("You came to a lake. There is an Island in the middle of the lake. Type 'wait' to wait, type 'swim', to swim across.   ")
  if swim_or_wait == 'wait':
    which_door = input("You arrived at the Island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?. ")
    if which_door == 'yellow':
      print("YOU WIN!")
    elif which_door == 'red':
      print("Burned by fire. GAME OVER!")
    elif which_door == 'blue':
      print("Eaten by beasts, GAME OVER!")
    else:
        print("GAME OVER!")

  else:
    print("Attacked by trout, GAME OVER!")
else:
  print("Fall into a hole. GAME OVER!")


