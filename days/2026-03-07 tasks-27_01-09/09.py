n = 0
for s in open('./09_27621.csv'):
    n += 1
    t = sorted(map(int, s.split()))
    st = set(t)
    if len(st) == 5:
        if t[-1]-t[0] == sum(t[1:-1]):
            print(n, t)  # 1321
            break