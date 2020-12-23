
### Calculator

num1 = float(input("Enter the first number: "))
op = input("Enter the operator (-/+/* or / for division): ")
num2 = float(input("Enter the second number: ")) ### the FUNCTION FLOAT means the assignment expects a NUMBER

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator. Would you like to try it again?")

