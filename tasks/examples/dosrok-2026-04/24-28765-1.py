s = 'BBCBABBAAABCBBCSSSBC'
# s = open('./24_28765.txt').readline().strip()
print(len(s))

cntBC = 2  # 180  # 2
mx = 1
for l in range(len(s)-1):
    for r in range(l+mx, len(s)):
        if s[l:r+1].count('BC') > cntBC:
            print(s[l:r])
            break  # остальные не подходят
        else:
            mx = r-l+1  # взяли один лишний символ
            
    if l%100_000 == 0: print('l =', l, 'mx =', mx)
print(mx)  # 38442 - за 10 минут
