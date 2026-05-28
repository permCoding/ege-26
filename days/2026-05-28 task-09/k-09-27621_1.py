i = 0
for e in open('./9_27621.csv'):
    i += 1
    t = list(map(int, e.split()))
    if len(set(t)) == len(t):
        if max(t)-min(t) == sum(t)-max(t)-min(t):
            print(i, t)  # 1321
            break