#2D Lists

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8 , 9],
    [0]
]

print(number_grid[0][2])

for row in number_grid:
    print(row)

###

for row in number_grid:
    for col in row:
        print(col)


### Let's remember. Function FOR shows each element of your string, list, range etc one by one in different lines.

friends = ["Miguelito", "Federico", "Rosemberg", "Arthur", "Douglas"]
print(list(friends))

for seq in friends:
    print(seq)

###

friends1 = [
    ["Miguelito", "Federico"],
    ["Rosemberg", "Arthur"],
    ["Douglas", "Bia"]
]

for seq1 in friends1:
    for seq1 in friends1:
        print(seq1) # Printing only the first column multiplied by 3 (number of rows

