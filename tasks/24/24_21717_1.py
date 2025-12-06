s = open('./24_21717.txt').read()

ln_mn = 10**9
a, k = 0, 0
for b in range(2, len(s)):
    if s[b-2:b+1] == 'RSQ': k += 1
    while k == 130 and s[b] != 'Q':
        ln_mn = min(ln_mn, b-a+1)
        if s[a:a+3] == 'RSQ': k -= 1
        a += 1
print(ln_mn)  # 497