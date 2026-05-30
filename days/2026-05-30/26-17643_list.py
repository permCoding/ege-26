f = open('./26_17643.txt')
n = int(f.readline())
t = [list(map(int, e.split())) for e in f]  # art price status
avg = sum(e[1] for e in t) / len(t)  # 558.1
d = [e for e in t if e[1] > avg]  # len => 4831

dct = {e[0]: [e[1], 0, 0] for e in d}
for e in d:
    pr, cnt_pr, cnt_npr = dct[e[0]]
    if e[2] == 0:
        dct[e[0]] = [pr, cnt_pr+1, cnt_npr]
    else:
        dct[e[0]] = [pr, cnt_pr, cnt_npr+1]
lst = [[art]+val for art, val in dct.items()]

r = sorted(lst, key=lambda x: (-x[2], -x[1], x[3]))[0]
print(r[1]*r[2], r[3])  # 43656 36

""" lp = 46481 36
Если и таких товаров несколько, лидер продаж — 
тот из них, которого осталось меньше всего

art: price cnt_pr cnt_npr

[51786, 856, 0]
[46481, 856, 0] +
[37134, 831, 0]
"""