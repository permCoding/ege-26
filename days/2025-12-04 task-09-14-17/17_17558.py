t = [int(e) for e in open('./17_17558.txt')]

k = len([e for e in t if e%32 == 0])

sms = []
for i in range(len(t)-1):
    if t[i]<0 or t[i+1]<0:
        if t[i]+t[i+1] < k:
            sms.append(t[i]+t[i+1])           
print(len(sms), max(sms))  # 4969 299
