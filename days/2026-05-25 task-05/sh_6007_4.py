def ch(n):
    s = str(n)
    a,b = int(s[0])+int(s[1]), int(s[2])+int(s[3])
    return (a==17 and b==18) or (a==18 and b==17)

print(min(n for n in range(10**3, 10**4) if ch(n)))