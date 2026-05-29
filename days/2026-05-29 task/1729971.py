t = [int(e) for e in open('./17_29971.txt')]
#  макс эл оканчивающегося на 33
m = max(e for e in t if abs(e)%100==33)  # 99033

k, mx = 0, -10**9
for i in range(len(t)-2):
    a,b,c = t[i],t[i+1],t[i+2]
    u1 = len([1 for e in [a,b,c] if 9<abs(e)<100]) == 2
    u2 = (a+b+c)**2 < m
    if u1 and u2:
        k += 1
        mx = max(mx, (a+b+c))
print(k, mx)  # 68 306