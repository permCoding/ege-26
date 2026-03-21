s = open('./24_27634.txt').readline().strip()

mn_ln = 10**9
L, cntZ = 0, 0  # метод двух указателей
for R in range(len(s)):
    if s[R] == 'Z':
        cntZ += 1
        if cntZ == 270:
            while s[L] != 'Z': L += 1
            # s[L] == 'Z'
            mn_ln = min(mn_ln, R-L+1)
            
print(mn_ln) # тут ответ неверный
# нужно перепроверить условия

# s[L:R+1].count('Z')

# W ZUTZTZ WWW
# 0 123456 789