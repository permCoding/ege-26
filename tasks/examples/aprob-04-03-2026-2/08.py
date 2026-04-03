from itertools import product as p

k = 0
for e in p('0123456', repeat=5):
    if e[0] != '0':
        if e.count('0') == 1:
            if e.count('1') <= 2:
                k += 1
print(k)  # 5100
