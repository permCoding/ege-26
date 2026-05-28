t = [sorted(map(int, e.split())) for e in open('./09_29962.csv')]

for j, e in enumerate(t):
    k, p = 0, 0
    for i in range(5):
        if e[i] == e[i+1] and e[i+1] == e[i+2]:
            k += 1
            p = e[i]
    if k == 1 and (sum(e)-3*p)/4 > p:
            print(e, j+1)  # 13609