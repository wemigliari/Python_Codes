print("Hello Again!")

#Functions. Function DEF

def sayhi (): # What comes after the colon : is going to be inside the () or inside my function.
    print("Hello User!")

    #or

def say_hi ():
    print("Hello User!")

sayhi()
say_hi()

print("Here")
sayhi()
print("There")


#Function with parameters - characters

def say_hi_1(name, age):
    print("Hello " +name+ " ! You are " +age+ ".")

say_hi_1("Wellington", "60")
say_hi_1("Caro", "70")

#Function with parameters - characters and integers

def say_hi_1(name, age):
    print("Hello " +name+ " ! You are " +str(age)+ ".")

say_hi_1("Wellington", 60)
say_hi_1("Caro", 70)

#Create the structure of your tuples (structure of your "table" of values, for example,
# 3 lines and 3 columns, 4 lines and 4 columns etc) with squared brackets [ ]


coordinates1 = []

#Now the formula

for x in range(3):
 for y in range(3):
  coordinates1.append((x, y))
print(coordinates1)
print(coordinates1[1])

coordinates2 = []

for x in range(2^2):
    for y in range(2^2):
        coordinates2.append((x, y))
print(coordinates2)

coordinates3 = [(0, i) for i in range(20)]
print(coordinates3)


