def to3(n):
    t = ''
    while n>0:
        t = str(n%3) + t
        n //= 3
    return t

lst = []
for n in range(1, 5800):
    t = to3(n)
    if n%3==0:
        t += t[-2:]
    else:
        t += to3(sum(int(e) for e in list(t))*2)
    r = int(t, 3)
    if r%2!=0 and r > 520: lst += [r]
print(min(lst))  # 567
