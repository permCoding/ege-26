t = [int(e.strip()) for e in open('./17_49381.txt')]
avg = sum(t) /len(t)

for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    u1 = (a < avg) and (b < avg)
    u2 = (a+b) % 100 == 19
    if u1 and u2:
        print(a+b)  # 6 4919
