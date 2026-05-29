from itertools import product


i = 0
for comb in product('АКОРСТ', repeat=5):
    i += 1
    if i%2 == 0:
        if comb[0] not in 'АСТ':
            if comb.count('О') == 2:
                print(i, *comb)  # 5058