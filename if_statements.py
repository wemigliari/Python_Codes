print("Hello World!")

### IF

is_urbanist = True
is_urban_planer = True

if is_urbanist:
    print ("Interesting!")

if is_urban_planer:
    print("It must be difficult dealing with politicians.")

## IF, OR and  ELSE

if is_urbanist or is_urban_planer:
    print("You are an expert at cities and urban transformation.")
else:
    print("You must be curious about cities.")


not_urbanist = False
not_urban_planer = False

if not_urbanist or not_urban_planer:
    print("You are an expert at cities and urban transformation.")
else:
    print("You must be curious about cities.")

## IF, AND and ELSE

not_urbanist = True  # I can play with the Boolean CHANGING the conditions (TRUE or FALSE) to get different answers.
not_urban_planer = True

if not_urbanist and not_urban_planer:
    print("Study both urbanism and urban planning. Be careful with politicians.")
elif not_urbanist and not(not_urban_planer): # elif = else if
    print("You just have to add urbanism in your life.")
elif not(not_urbanist) and (not_urban_planer):
    print("You can start with urban planning, but be careful with politicians.")
else:
    print("So, you have experience with both urbanism and urban planning. Cool!")

#### Test

## IF, AND, ELIF and AND NOT

question1 = input("Do you see yourself as an urbanist? Write True or False. ")

if question1 == "True":
    print("Interesting!")
elif question1 != "True":
    print("We have something for you.")
else:
    print(question1)


question2 = input("Do you know what is urban planning? Write Yes or No. ")

if question2 == "No":
    print("Good! Let's talk about it.")
elif question2 == "Yes":
    print(asnwer2 = input('Do you know how Nordic cities are commonly planned? Yes or No? '))

question3 = input("Do you know something about Nordic cities and transport? Write Yes or No. ")
if question3 == "Yes":
    print(input("Have you ever heard about green corridors? There is a route of transport called STRING linking Hamburg to Oslo."))
elif question3 == "No":
    print("It involves 4 countries, 7 regions, 5 cities, 3 metropolitan areas, 109.000 sq/km and 12.8 million people.")

question3a = input("Do you know its main idea?")
if question3 == "No":
    print("Green corridors are train lines, ferries and highways for cargo linking different long-distant places.")

print("There is a route of transport called STRING linking Hamburg to Oslo.")

question3b = input("Do you know the purpose?")
if question3b == "Yes":
    print("Please, define it using just two words.")
elif question3b == "No":
    print("Carbon reduction")
else:
    print("Well, it has been more related to carbon reduction, but anyway good point. ")

print("So, the idea is to reduce the use of CO2 and other greenhouse effect gases lining up different geographical points.")
print("It involves 4 countries, 7 regions, 5 cities, 3 metropolitan areas, 109.000 sq/km and 12.8 million people.")
print("All of that was planned. So, it involves urban planning its subsection called means of transportation. ")

question4 = input("Interesting?")
if question4 == "Yes" or "yes":
    print("I have more for you.")
elif question4 == "NO" or "no":
    print("Do not worry! Urban topics vary so much that you'll be impressed!")