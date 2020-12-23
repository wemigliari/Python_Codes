print("Hellow World!")

#Tuples: a type of data structure. Use () NOT []

coordinates = (4, 5)
print(coordinates)

### Tuples are immutable. It means you CANNOT reassign them. Ex:

# Printing to check the values (0 for the first element, 1 for the second element).

print(coordinates[1])

# Trying to reassign the tuple, positions 0 and 1

#print(coordinates [1]) = 10 (Typed on purpose to check the program yelling at you9

# Different between lists and tuples [] versus ()

### Attention: a list of coordinates [()]

#list of coordinates

coordinates = [(4, 5), (5, 6), (99, 100)]
print(coordinates)

print(coordinates[1])
