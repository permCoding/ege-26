s = open('./24_27634.txt').readline().strip()

mn_ln = 10**9
k, L = 0, 0
for R in range(0, len(s)):
    if s[R] == 'Z':
        k += 1
        while k == 270:
            mn_ln = min(mn_ln, R-L+1)
            if s[L] == 'Z': k -= 1  # 269
            L += 1
print(mn_ln)  # 1058

# s[L:R+1].count('Z')

# W ZUTZTZ WWW
# 0 123456 789