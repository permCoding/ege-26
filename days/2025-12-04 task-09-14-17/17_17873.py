t = [int(e) for e in open('./17_17873.txt')]

mn = min(t)

sms = []
for i in range(len(t)-1):
    if t[i]%16==mn or t[i+1]%16==mn:
        sms.append(t[i]+t[i+1])
print(len(sms), max(sms))  # 1214 176024
