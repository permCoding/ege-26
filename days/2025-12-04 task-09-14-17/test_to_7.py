def to_7(v):
    if v == 0: return 0
    r = ''
    while v > 0:
        r = str(v % 7) + r
        v //= 7
    return r


print(to_7(0))
print(to_7(7))
print(to_7(8))
print(to_7(15))
