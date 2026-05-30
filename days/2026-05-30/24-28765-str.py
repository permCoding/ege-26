s = open('24_28765.txt').readline()

subs, cntBC, mx = '', 0, 0

for r in range(len(s)):
    subs += s[r]
    if subs[-2:] == 'BC': cntBC += 1

    while cntBC > 180:
        if subs[:2] == 'BC': cntBC -= 1
        subs = subs[1:]

    mx = max(mx, len(subs))

print(mx)  # 38442
