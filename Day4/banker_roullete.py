#import random modum
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
#save the splitted names in the names variable
names = names_string.split(", ")
#Save the length of the names in the length variable
length = len(names)
#choose the random name from 0 to the length of numbers provided -1 because lists count from index 0 and random counts from index1
random_name = random.randint(0, length -1)
name = names[random_name]
print(f"{name} is going to buy the meal today!")
