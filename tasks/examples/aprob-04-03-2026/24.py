s = open('./24_27634.txt').readline().strip()
print(len(s))  # 10_000_000

mn_ln = 10**10
cnt = 0
i_start = 0
for i in range(0, len(s)):
    if s[i] == 'Z':
        cnt += 1
        while cnt == 270:
            mn_ln = min(mn_ln, i-i_start+1)
            if s[i_start] == 'Z': cnt -= 1
            i_start += 1
            
print(mn_ln)  # 1058

"""
из символов TUVWXYZ
Определите минимальное количество идущих подряд символов
среди которых символ Z встречается не менее 270 раз
"""