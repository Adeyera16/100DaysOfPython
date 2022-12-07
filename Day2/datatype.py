#A program that calculates two digits number, for example 23 should print out 5
two_digit_number = input("Type a two digit number: ")
#convert both digit to an integer and use subcripting to get each numbers
digit1 = int(two_digit_number[0])
digit2 = int(two_digit_number[1])
#add the 2 digits together
two_digit_number = digit1 + digit2
print(two_digit_number)
