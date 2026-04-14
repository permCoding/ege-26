s = open('./24_28765.txt').readline().strip()

cntBC = 180
cnt = 0
mx = 0

l = 0
for r in range(1, len(s)):
    if s[r-1]+s[r] == 'BC': cnt += 1
    
    while cnt > cntBC:
        if s[l:l+2] == 'BC': cnt -= 1
        l += 1
    
    mx = max(mx, r-l+1)
    if r%100_000 == 0: print('r =', r, 'mx =', mx)

print(mx)  # 38442 - за 15 секунд
