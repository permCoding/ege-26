s = open("24_28765.txt").readline()

cntBC = 0
mx = 0
l = 0
for r in range(1, len(s)):
    if s[r-1] + s[r] == "BC": cntBC += 1
    if cntBC <= 180: mx = max(mx, r-l+1)
    while cntBC > 180:
        if s[l] + s[l+1] == "BC": cntBC -= 1
        l += 1
print(mx)  #38442
