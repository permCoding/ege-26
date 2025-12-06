s = open('./24_21717.txt').read().replace('RSQ', '#')
for ch in 'FGQRSW': s = s.replace(ch, '*')

k = 0
ln, ln_mn = 0, 10**9
a, b = 0, 0
for b in range(len(s)):
    if s[b] == '#': k += 1
    if k == 130:
        st = s[a:b+1].strip('*')
        ln_mn = min(ln_mn, len(st))
    while k > 130:
        if s[a] == '#': k -= 1
        a += 1
print(ln_mn+130*2+1)  # 497