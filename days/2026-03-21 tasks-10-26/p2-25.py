d = 271
for n in range(d, 10**8+1, d):
    s = str(n)
    if s[:2]=='12' and s[4:6]=='15' and s[-1]=='6':
        print(n, n//d)

# 12??15*6