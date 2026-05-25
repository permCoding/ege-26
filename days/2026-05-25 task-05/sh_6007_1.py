for n in range(1_000, 9_999+1):
    s = str(n)
    a = int(s[0]) + int(s[1])
    b = int(s[2]) + int(s[3])
    t = [a,b]
    r = str(min(t)) + str(max(t))
    if r == '1718':
        print(n)
        break