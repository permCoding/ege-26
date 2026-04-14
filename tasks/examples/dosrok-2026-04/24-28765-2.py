# s = 'BBCBABBAAABCBBCSSSBC'
s = open('./24_28765.txt').readline().strip()
print(len(s))

cntBC = 180  # 2
cnt = 0  # current cntBC
mx = 0

cur = ''  # current substring
for r in range(len(s)):
    cur += s[r]  # current substring
    if cur[-2:] == 'BC': cnt += 1
    
    while cnt > cntBC:
        if cur[:2] == 'BC': cnt -= 1  # удаляем лишний
        cur = cur[1:]
    
    mx = max(mx, len(cur))
    if r%100_000 == 0: print('r =', r, 'mx =', mx)

print(mx)  # 38442 - за 2 минуты
