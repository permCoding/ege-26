s = open('./24_21717.txt').read().replace('RSQ', '#')

ln_mn = 10**4
for a in range(len(s)):
    for b in range(a+ln_mn, a, -1):
        subs = s[a:b+1]
        if subs.count('#') < 130: break
        if subs.count('#') == 130:
            ln_mn = min(ln_mn, len(subs))
print(ln_mn+130*2+1)  # 497