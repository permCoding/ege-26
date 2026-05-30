amount = 0

for line in open('09-28930.csv'):
    t = list(map(int, line.split()))
    # u1 = (t[0]<t[1]<t[2]) and (t[2]<t[3]<t[4])
    u1 = all(t[i]<t[i+1] for i in range(4))
    u2 = 2*(min(t)+max(t)) <= sum(t)
    if u1 and u2: amount += 1

print(amount)

"""
1) возрастание - 1 3 4 5 7 99 122
2) неубывание  - 1 3 3 5 5 5 99
"""