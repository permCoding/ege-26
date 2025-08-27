from itertools import product as p

for i, e in enumerate(p('АКОРСТ', repeat=5), start=1):
    if i%2 ==0:
        if e.count('О') == 2:
            if e[0] != 'А' and e[0] != 'С' and e[0] != 'Т':
                print(i, e)  # 5058
