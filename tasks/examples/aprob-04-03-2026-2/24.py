s = open('./24_27777.txt').readline().strip()
print(len(s))  # 10_000_000

mx_ln, cur = 0, ''
for i in range(len(s)):
    if s[i] in '0123456789AB':
        if cur == 0:
            if s[i] != '0': cur += s[i]
        else:
            cur += s[i]
            mx_ln = max(mx_ln, len(cur))
    else:
        cur = ''

print(mx_ln)  # 18

import re
print(len(max(list(re.findall(r'[1-9AB][0-9AB]*', s)), key=len)))
