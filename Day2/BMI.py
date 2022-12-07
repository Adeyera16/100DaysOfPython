#Calculate the body mass index of your user
#Ask the user to input their weight and height
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#convert the height to float and the weight to int
new_height = float(height)
new_weight = int(weight)
#calculate the BMI 
result = new_weight / (new_height * new_height)
#print the result as a whole number
print(int(result))
