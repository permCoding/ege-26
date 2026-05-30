f = open('./26_17643.txt')
n = int(f.readline())
t = [list(map(int, e.split())) for e in f]  # art price status
avg = sum(e[1] for e in t) / len(t)  # 558.1
d = [e for e in t if e[1] > avg]  # len => 4831

dct = {e[0]: 0 for e in d}
for e in d:
    if e[2] == 0:
        dct[e[0]] += 1

lps = [art for art, v in dct.items() if v == 51]
for art in lps:
    for elm in d:
        if elm[0] == art:
            print(elm)
            break

for art in 51786, 46481:
    print(art, len([1 for elm in d if elm[0] == art and elm[2] == 1]))
print(dct[46481]*856, 36)

""" lp = 46481 36
[51786, 856, 0]
[46481, 856, 0]
[37134, 831, 0]
Если и таких товаров несколько, 
лидер продаж — тот из них, 
которого осталось меньше всего

art price status cnt_pr cnt_npr

"""