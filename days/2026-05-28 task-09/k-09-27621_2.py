p = []
for i, e in enumerate(open('9_27621.csv')):
    t = sorted(map(int, e.split()))
    if len(set(t)) == 5 and t[-1]-t[0] == sum(t[1:-1]):
        p += [i+1]  # 1321
print(p)