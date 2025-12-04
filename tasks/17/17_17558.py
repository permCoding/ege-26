t = [int(e) for e in open('./17_17558.txt')]

k = len([e for e in t if e%32==0])

amount, mx = 0, -9999999
for i in range(len(t)-1):
    if t[i] < 0 or t[i+1] < 0:
        if t[i]+t[i+1] < k:
            amount += 1
            mx = max(mx, t[i]+t[i+1])
print(amount, mx)  # 4969 299
