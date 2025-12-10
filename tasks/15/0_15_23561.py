def f(a, x):
    u1 = x % 128 == 0
    u2 = x % a == 0
    u3 = x % 80 == 0
    return (not u1) or (u2 or (not u3))

for a in range(1_000, 0, -1):
    if all(f(a, x) for x in range(1_000)):
        print(a)  # 640
        break
