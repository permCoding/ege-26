from itertools import product as p

n = 0
for s in p('АЕЛПРЬ', repeat=6):
    n += 1
    if n%2 == 1:
        if (s[0] not in 'АЛ') and (s.count('П')>=2):
            print(n, ''.join(s))  # 7903 ЕААППА
            break
