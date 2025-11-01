k = 0
for line in open('./9_21895.csv'):
    t = sorted([int(elm) for elm in line.split(' ')])
    if len(set(t)) == 5:
        if t[3]+t[4] <= t[0]+t[1]+t[2]:
            k += 1
print(k)

# lst = sorted([97, 59, 96, 28, 39], reverse=True)
# lst = sorted([97, 59, 96, 28, 39])
# print(lst)

