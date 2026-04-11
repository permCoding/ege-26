t = [int(e) for e in open('./17_27629.txt')]
mx43 = max(e for e in t if 999<abs(e)<10_000 and abs(e)%100==43)

k, mx = 0, 0
for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    u1 = 999<abs(a)<10_000 or 999<abs(b)<10_000
    u2 = (a+b)**2 < mx43**2
    if u1 and u2:
        k += 1
        mx = max(mx, (a+b)**2)
print(k, mx)  # 1218 98843364


# квадрата максимального 
# из четырёхзначных элементов последовательности
# оканчивающихся на 43