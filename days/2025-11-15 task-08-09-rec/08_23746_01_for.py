def to_base(dec, base=6):
    res = ''
    while dec > 0:
        ost = dec % base
        res = str(ost) + res
        dec //= base
    return res


lst = []
i = 0
for dec in range(6**5):  # 7776
    i += 1
    if i%2 == 0:
        s = to_base(dec)
        if not(s[0] in '045'):
            if s.count('2') == 2:
                lst += [i]  # 5058
                
print(lst[-1])

# А 0
# К 1
# О 2
# Р 3
# С 4
# Т 5


# print(to_base(5))  # 5
# print(to_base(6))  # 10
# print(to_base(7))  # 11
# print(to_base(8))  # 12

# print(to_base(0))  #  10000

# print(to_base(7776))  # 100000