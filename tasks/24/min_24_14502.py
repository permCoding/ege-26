s = open("24_14502.txt").readline()

al = ''.join(chr(i) for i in range(ord('A'),ord('Z')+1))
dct = {smb:0 for smb in al}

l = 0
mn = 10**9
for r in range(len(s)):
    dct[s[r]] += 1
    
    while 0 not in dct.values():
        mn = min(mn, r-l+1)
        dct[s[l]] -= 1
        l += 1

print(mn)  # 440
