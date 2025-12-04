t, k = [], 0
for e in open('./17_17558.txt'):
    t += [int(e)]
    if int(e)%32 == 0:
        k += 1

sms = [t[i]+t[i+1] for i in range(len(t)-1) if (t[i]<0 or t[i+1]<0) and (t[i]+t[i+1] < k)]

print(len(sms), max(sms))  # 4969 299
