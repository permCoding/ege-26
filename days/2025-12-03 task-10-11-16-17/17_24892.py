t = [int(line) for line in open('./17_24892.txt')]

mx = max(e for e in t if (-10000 < e < -999) and (e%9 == 0))

cnt, sms = 0, []
for i in range(len(t)-1):
    u1 = (t[i] < 0) ^ (t[i+1] < 0)
    u2 = t[i] + t[i+1] > mx
    if u1 and u2:
        cnt += 1
        sms += [t[i]**2 + t[i+1]**2]
print(cnt, min(sms))  # 2627 504410
