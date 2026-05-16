from itertools import product
i = 0
for e in product('АКОРСТ', repeat=5):
    i += 1
    if i%2 == 0:
        if e[0] not in 'АСТ' and e.count('О') == 2:
            print(i, ''.join(e))  # 5058
    