s = open('./24_29354.txt').readline().strip()

l, cntBC, ln_mx = 0, 0, 0
for r in range(1, len(s)):
    if s[r-1]+s[r] == 'BC': cntBC += 1
    while cntBC > 190:
        if s[l]+s[l+1] == 'BC': cntBC -= 1
        l += 1
    if cntBC == 190: ln_mx = max(ln_mx, r-l+1)

print(ln_mx)  # 2287

# l  r    
# 012345
# ABCDEF
    
    