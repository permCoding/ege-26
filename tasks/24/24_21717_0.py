s = open('./24_21717.txt').read().replace('RSQ', '#')

ln_mn = 10**9
a, k = 0, 0
for b in range(len(s)):
    if s[b] == '#': k += 1
    while k == 130:
        ln_mn = min(ln_mn, b-a+1)
        if s[a] == '#': k -= 1
        a += 1
print(ln_mn+130*2+1)  # 497