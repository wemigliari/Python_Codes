# Comments after a wrong value being introduced

try:
    number = int(input("Enter a number for the base : "))
    number1 = int(input("Enter a number for the power : "))
    print(number ** number1)
except ZeroDivisionError as err: #Without the two dots
    print(err)
except ValueError:
    print("Invalid Input")


### Notice the differences between the outputs (for example, 1 (INT) and 1.0 (FLOAT)

try:
    number = float(input("Enter a number for the base : "))
    number1 = float(input("Enter a number for the power : "))
    print(number ** number1)
except: # (WITH TWO DOTS, please! One more thing: ATTENTION if not specified, the exception will catch any sort of error including code error and not necessarily an INPUT ERROR.
    print("Invalid entry. Please, enter a the correct value!")

### Let's look at divisions by zero

try:
    answer = 10/0 # So, the problem is with the code not with the input
    number = int(input("Enter a number for the base : "))
    number1 = int(input("Enter a number for the power : "))
    print(number ** number1)
except ZeroDivisionError as err:  # Without the two dots
    print(err)
except ValueError:
    print("Invalid Input")

