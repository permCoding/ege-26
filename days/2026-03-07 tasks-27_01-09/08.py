from itertools import product

n = 0
for w in product('ИРСТУЦ', repeat=5):
    n += 1
    s = ''.join(w)
    if (s.count('И') == 2) and ('ЦЦ' not in s):
        print(n, s)  # 7525
