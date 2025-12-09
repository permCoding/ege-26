num = 52
print(bin(num)[2:])
lst = []
for x in range(0, 99):
    if x & num == 0:
        lst.append(x)
print(lst)