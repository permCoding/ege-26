from itertools import product as p

for i, e in enumerate(p('ЕИОРТЯ', repeat=6), start=1):
    if i%2 == 1:
        if e.count('И') >= 2:
            # if e[0] != 'Р' and e[0] != 'Т' and e[0] != 'Я':
            if not(e[0] in 'РТЯ'):
                print(i, e)  # 23159
