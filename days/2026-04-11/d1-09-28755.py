k = 0
for line in open('./09_28755.csv'):
    t = sorted(map(int, line.split()))
    u1 = t[3] < sum(t[:3])
    u2 = t[0]+t[3] != t[1]+t[2]
    if u1 and u2: k += 1
print(k)  # 2500

# 2 4 5 6