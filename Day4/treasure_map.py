#create lists of blank tiles
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
#save the lists in a variable called map
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
#use the index method to get the first and second number to determine the rows and columns
column = int(position[0])
row = int(position[1])
#save the row selected in a variable , the -1 is because the person is choosing rom row 1-3 but it is counted as 0-2
selected_row = map[row -1]
#replace the column with x
selected_row[column -1] = 'X'

print(f"{row1}\n{row2}\n{row3}")


