for n in range(10_000, 100_000):
    s = str(n)
    a, b = 0, 0
    for i in range(len(s)):
        if i%2 != 0:
            a += int(s[i])**2
        else:
            b += int(s[i])**2
    r = str(min(a,b)) + str(max(a,b))
    if r == '13':
        print(n)  # 11101