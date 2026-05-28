cnt = 0
for e in open('./09_28930.csv'):
    t = [int(x) for x in e.split()]
    if (sorted(t) == t) and len(set(t))==5:
        if max(t)+min(t) <= sum(t)-(max(t)+min(t)):
            cnt += 1
print(cnt)