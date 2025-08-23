def get(s, x):
    res = 0
    s = s[::-1]
    for p in range(len(s)):
        if s[p] == 'x':
            res += x * 29**p
        else:
            res += int(s[p]) * 29**p
    return res

# print(get('1x', 28))
for x in range(28, -1, -1):
    n1 = get('923x874', x)
    n2 = get('524x6152', x)
    print(x, n1, n2)
    if (n1 + n2) % 28 == 0:
        print((n1 + n2) // 28)  # 3319197720
        break
