t = [int(e.strip()) for e in open('./17_49381.txt')]
avg = sum(t) /len(t)

cnt, pairs = 0, []
for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    u1 = (a < avg) and (b < avg)
    pair = (a+b)
    u2 = pair % 100 == 19
    if u1 and u2:
        cnt += 1
        pairs += [pair]
        print(pair)

print(cnt, min(pairs))
