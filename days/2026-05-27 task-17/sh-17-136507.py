t = [int(e) for e in open('17.txt')]
m = max(e for e in t if abs(e)%10==3)

k, mx = 0, 0
for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    u1 = (abs(a)%10==3) ^ (abs(b)%10==3)
    u2 = a**2 + b**2 >= m**2
    if u1 and u2:
        k += 1
        mx = max(mx, a**2 + b**2)
print(k, mx)
