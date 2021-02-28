import math

a = float(input("Type the value of a: "))
b = float(input("Type the value of b: "))
c = float(input("Type the value of c: "))

delta = b**2-4*a*c

print("{}". format(delta))

x1 = -b + (pow(delta, 2))/2*a
x2 = +b + (pow(delta, 2))/2*a

print("Delta =", delta)
print("R1 =", x1)
print("R2 =", x2)

rdelta = math.sqrt(delta)

x = ((0-b)+rdelta)/2*a

print("rdelta =", rdelta)








