def f(n):
    return (len(str(abs(n))) == 4) and (str(n)[-1] == '6')

t = [int(e) for e in open('./17_21712.txt')]

m = min([e for e in t if e > 0 and f(e)])

sms = []
for i in range(len(t)-2):
    w = t[i:i+3]
    if len([e for e in w if f(e)]) == 1:
        if sum(w) <= m:
            sms.append(sum(w))
print(len(sms), max(sms))  # 507 1042
