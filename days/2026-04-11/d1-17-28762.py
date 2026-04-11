t = [int(e) for e in open('./17_28762.txt')]
mn23 = min(e for e in t if e%23==0)

k, mx = 0, 0
for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    if a%mn23==0 or b%mn23==0:
        k += 1
        mx = max(mx, a+b)
print(k, mx)  # 113 168437
