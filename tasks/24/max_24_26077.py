s = open('./24_26077.txt').readline()

cntOdd = 0
mx = 0
ss = ''
for r in range(len(s)):
    if s[r] == 'G':
        ss = 'G'
        cntOdd = 0
    else:
        if ss != '':
            ss += s[r]
            if s[r] in '13579': cntOdd += 1
            if cntOdd == 45: mx = max(mx, len(ss))
            if cntOdd > 45: ss = ''

print(mx)  # 76
