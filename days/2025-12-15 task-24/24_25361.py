s = open("24_25361.txt").readline().strip()

l = 0
cnt_F = 0
ln_mx = 0

for r in range(len(s)):
    
    if s[r] == 'F': cnt_F += 1
    
    if (cnt_F > 76) or (s[r] in '02468'): 
        l = r
        cnt_F = 0
    
    if cnt_F == 76: ln_mx = max(ln_mx, r-l+1)
    
print(ln_mx)  # 163

    # substr = s[l:r+1]
    # substr.count('F') == 76

    
"""
2SKDVEKLRBVERKLFFFIHWEQUDGJWQGVFFFIQEJHBDFFQWHJKGDFFWJEJFW
файл состоит из десятичных цифр и заглавных букв латинского алфавита. Определите максимальное количество идущих подряд символов, среди которых 

буква F встречается ровно 76 раз, 
чётная цифра встречается ровно один раз, 
искомая последовательность начинается с этой единственной чётной цифры.


В ответе запишите число - количество символов в найденной последовательности.


s ='2SKDVEKLRBVERKLFFFIHWEQUDGJWQGVFFFIQEJHBDFFQWHJKGDFFWJEJFW'
print(s[0] in '02468')
print(s.count('F'))

"""