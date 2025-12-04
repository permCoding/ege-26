t = [int(e) for e in open('./17_21903.txt')]

m = min([e for e in t if len(str(abs(e)))==3 and str(abs(e))[-2:]=='15'])
# print(m)
sms = []
for i in range(len(t)-2):
    w = t[i:i+3]
    a,b,c = w
    if (a>0 and b>0 and c>0) or (a<0 and b<0 and c<0):
        mn, mx = min(w), max(w)
        if mn*mx > m**2:
            sms += [mn*mx]
print(len(sms), min(sms))  # 3507 863808
