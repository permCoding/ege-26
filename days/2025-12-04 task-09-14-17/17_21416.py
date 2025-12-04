t = [int(e) for e in open('./17_21416.txt')]

s = sum([e for e in t if e < 0])

q = []
for i in range(len(t)-2):
    w = t[i:i+3]
    mx, mn = max(w), min(w)
    if mx*mn > s:
        q.append(sum(w))
print(len(q), abs(max(q)))  # 10007 7953
        