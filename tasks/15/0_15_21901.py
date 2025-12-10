def f(x, a):
    v1 = (x&52 != 0) and (x&48 == 0)
    v2 = x&a != 0
    return v1 <= v2

for a in range(1, 999):
    if all(f(x, a) for x in range(1, 999)):
        print(a)  # 4
        break
