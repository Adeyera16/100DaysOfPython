#import random module
import random

#use the random number to choose a number from 0 to 1 
random_number = random.randint(0, 1)

#print heads if the number is 1. Print tails if the number is 0
if random_number == 1:
    print("Heads")
else:
    print("Tails")
