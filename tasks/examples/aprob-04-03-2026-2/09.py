k = 0
for e in open('./09_27764.csv'):
    t = sorted(map(int, e.split()))
    if len(set(t)) == len(t):
        if 2 * (t[0]+t[-1]) == sum(t[1:-1]):
            k += 1
print(k)  # 5019
