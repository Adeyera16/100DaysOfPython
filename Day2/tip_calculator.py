#Write a program that calculates the amount of tip + split the bill among people
#print a welcome message
print("Welcome to tip calculator!")
#Ask the user to input their total bill
bill = float(input("What was the total bill?  $"))
#Ask the user how much they would like to give
amount = int(input("How much tip would you like to give? 10, 12, or 15? "))
#Ask the user how many people would be splitting the bill
bill_split = int(input("How many people to split the bill? "))
#Calculate the percentage by dividing the tip amount by 100
percentage = amount / 100
#multiply the percentage by the bill amount to get the exact percentage
total_percentage_amount = bill * percentage
#add the bill plus the percentage amount to get the bill and tip amount all together
total_bill_amount = bill + total_percentage_amount
#divide the total amount by the number of people that wants to split the bill
total_bill = total_bill_amount / bill_split
#round the amount to 2 decimal places
rounded_amount = round(total_bill, 2)
#print the output
print(f"Each person should pay: {rounded_amount}")

