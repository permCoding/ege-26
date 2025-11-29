from math import ceil, floor


def ceil_(a, b):
    if a % b == 0:
        return a // b
    else:
        return a // b + 1

def ceil_mini(a, b):
    return a//b if a % b == 0 else a // b + 1


a, b = 17, 3
print(a / b)
print(a // b)
print(floor(a / b))
print(ceil(a / b))
print(ceil_(a, b))
print(ceil_mini(a, b))

# a // b === floor(a / b)
# ceil(a / b)