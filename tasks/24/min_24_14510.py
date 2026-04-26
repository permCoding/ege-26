s = open("24_14510.txt").readline()
# НЕ использовать replace
def g(smb): return smb in 'AEIOUY'

l = 0
cnt = 0
mn = 10**9
for r in range(2, len(s)):
    if (not g(s[r-2])) and (not g(s[r-1])) and g(s[r]): cnt += 1
    while cnt >= 500:
        mn = min(mn, r-l+1)
        if (not g(s[l])) and (not g(s[l+1])) and g(s[l+2]): cnt -= 1
        l += 1
print(mn)  # 3493
