# Power functions

# print(2**3)
# print(2*3)

def raise_to_power(base_num, pow_num):
    result = 3 #How many times do you to multiply by your raise_to_power. E.g., (2*2) x 3, result = 3
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 2))