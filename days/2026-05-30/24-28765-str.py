s = open('24_28765.txt').readline()

l, cntBC, mx = 0, 0, 0

for r in range(len(s)-1):
    if s[r:r+2] == 'BC': cntBC += 1

    while cntBC > 180:
        if s[l:l+2] == 'BC': cntBC -= 1
        l += 1

    mx = max(mx, r-l+1 + 1)

print(mx)  # 38442
