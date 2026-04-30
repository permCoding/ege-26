s = open("24-29354.txt").readline()
mx, cntBC, l = 0, 0, 0
for r in range(1, len(s)):
    if s[r-1:r+1] == 'BC': cntBC += 1
    while cntBC > 190:
        if s[l:l+2] == 'BC':
            cntBC -= 1
        l += 1
    if cntBC == 190: mx = max(mx, r-l+1)
print(mx)  # 2287
