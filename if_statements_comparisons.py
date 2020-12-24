print("Hello World!")

### Creating a function COMPARING parameters num1, num2 and num3,
# in fact, Boolean game (TRUE or FALSE through comparison < or > with =)

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 <= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 40, 100))

### Comparing with names (strings)

def cats(blue, black, white):
    if blue == black and blue == white: # == meaning is EQUAL TO
        print("blue")
    elif black != black and black == blue: ## != meaning NOT EQUAL TO
        return black
    else:
        return white

###

print(cats("black", "white", "blue"))

def cats(blue, black, white):
    if blue == black and blue == white: # == meaning is EQUAL TO
        print("blue")
    elif black != black and black == blue: ## != meaning NOT EQUAL TO
        print("white")
    else:
        print("black")

print(cats("black", "blue", "black"))