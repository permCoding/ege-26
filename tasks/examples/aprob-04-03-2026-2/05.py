t = []
for n in range(19, 219):
    b = bin(n)[2:]
    if n%2 == 0:
        b = '10' + b
    else:
        b = '1' + b + '01'
    r = int(b, 2)
    t += [r]
print(min(t))  # 84
