for n in range(1_000, 9_999+1):
    s = str(n)
    a = int(s[0]) + int(s[1])
    b = int(s[2]) + int(s[3])
    if (a==17 and b==18) or (a==18 and b==17):
        print(n)
        break