print("Hello World!")

#Return statement. Creating a function with numbers. Function DEF

def cube(num):
    num*num*num

print(cube(3)) ### Nothing happens "non". Why? I need a return statement.

def cube(num):
    return num*num*num

print(cube(5))

result = cube(4)
print(result)

number1 = input("Type a number and I will multiply it to the power of 4!")

print(result)