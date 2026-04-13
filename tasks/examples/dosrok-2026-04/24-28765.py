# s = 'BBCBABBAAABCBBCSSS'
s = open('./24_28765.txt').readline().strip()

cnt = 180  # 2
print(len(s))
mx = 1
for l in range(0, len(s)-1):
    for r in range(l+mx, len(s)):
        if s[l:r+1].count('BC') <= cnt:
            mx = r-l+1
        else:
            break  # все остальные r не подходят
    if l%100_000 == 0: print('l = ', l, 'mx = ', mx)
print(mx)  # 38442 - за 10 минут


# s = 'BBCBABBAAABCBBCSSS'  # тут 3 BC
# print(len(s))
# l, r = 0, 18
# print(s[l:r+1].count('BC'))