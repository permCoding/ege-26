t = [sorted(map(int, e.split(';'))) for e in open('./9_27621.csv')]
n = 0
for e in t:
    n += 1
    if len(set(e)) == 5:
        if e[-1]-e[0] == sum(e[1:-1]):
            print(n, e)  # 1321 [4, 7, 15, 38, 64]