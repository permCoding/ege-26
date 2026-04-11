from itertools import product as p

n = 0
for tpl in p('АЕЛПРЬ', repeat=5):
    n += 1
    if n % 2 == 0:
        # if tpl[0] != 'Р' and tpl[0] != 'Ь':
        if tpl[0] not in 'РЬ':
            if tpl.count('Л') >= 2:
                print(n, ''.join(tpl))  # 5058
