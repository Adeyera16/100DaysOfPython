#Write a program that writes how many days, month and weeks is left, if the user is to live till 90 years old
#take the input of the user
age = input("What is your current age? ")
#change the age to an integer
new_age = int(age)
#minus the age from 90
years_left = 90 - new_age
#calculate the days, weeks and months left
days_left = years_left * 365
weeks_left= years_left * 52
months_left = years_left * 12
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
