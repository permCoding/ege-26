amount = 0
for e in open('./9.csv'):
    t = sorted(map(int, e.split()))
    if t[2] > (t[0]+t[1]+t[3])/3:
        if len(set(t)) == 3:
            amount += 1
print(amount)  # 17