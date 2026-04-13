s = open('./24_28765.txt').readline().strip()

mx = 0
cntBC = 0
l = 0

for r in range(1, len(s)):
    if s[r-1]+s[r] == 'BC': cntBC += 1
    
    while cntBC > 180:
        if l+1 < len(s):
            if s[l:l+2] == 'BC': cntBC -= 1
        l += 1
    
    mx = max(mx, r-l+1)

print(mx)
