
### FOR LOOP

for letter in "Wellington Migliari":
    print(letter)

# List of names, use = [] for strings

friends = ["Rosa", "Miguel", "Feder", "Arthur"]

for friend in friends:
    print(friend)

# OR loops for individual values

print("Names of my friends")

friends = ["Rosa", "Miguel", "Feder", "Arthur"]

for index2 in range(len(friends)):
    print(friends[index2])

print("Now, with numbers")


### List of Numbers, use RANGE for numbers

for index in range(20): # ATTENTION: not printing the number 20, but 0 included
    print(index)

# Compare the loops with LEN
numbers = range(5, 10)

for sequence in range(len(numbers)):
    print(numbers[sequence])

for sequence in numbers:
    print(sequence)

# LOOP with IF and ELSE

for sequence in range(20):
    if sequence == 0:
        print("zero")
    else:
        print("Other numbers")

# OR

for sequence in range(20):
    if sequence <= 10:
        print("zero")
    else:
        print("Other numbers")



