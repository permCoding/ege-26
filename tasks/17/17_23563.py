t = [int(e) for e in open('./17_23563.txt')]

mn = min(e for e in t if e > 0 and e%35==0)

cnt, sms = 0, []
for i in range(len(t)-1):
    if t[i] != t[i+1]:
        if abs(t[i] - t[i+1]) % mn == 0:
            cnt += 1
            sms.append(t[i]+t[i+1])
print(cnt, max(sms))  # 87 184328
