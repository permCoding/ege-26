def f(n):
    u1 = len(str(abs(n))) == 5
    u2 = str(n)[-2:] == '43'
    return u1 and u2
        

t = [int(e) for e in open('./17_19249.txt')]

m = max(e for e in t if f(e))

sms = []
for i in range(len(t)-2):
    w = t[i:i+3]
    if any(f(e) for e in w):
        sm = sum(e**2 for e in w)
        if sm <= m**2:
            sms.append(sm)
            
print(len(sms), min(sms))  # 92 838850571
