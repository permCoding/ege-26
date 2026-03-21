import re  # import fnmatch

s = open('./24_27777.txt').readline().strip()

# способ просто циклом
al = '0123456789AB'
mx_ln, cur = 0, ''
for i in range(len(s)):
    if s[i] in al:
        if s[i] == '0' and cur != '':
            cur += s[i]
        else:
            cur += s[i]
        mx_ln = max(mx_ln, len(cur))
    else:
        cur = ''
print(mx_ln)  # 18


# способ с регуляркой
# t = []
# for elm in re.findall(r'[1-9AB][0-9AB]*', s):
#     t.append(elm)
#     if len(elm) > 16:
#         print(len(elm), elm)
    
# способ с регуляркой
# t = []
# for elm in re.findall(r'[1-9AB][0-9AB]*', s):
#     t.append(elm)
# print(len(max(t, key=len)))

# способ с регуляркой
print(len(max([elm for elm in re.findall(r'[1-9AB][0-9AB]*', s)], key=len)))

# ответ : 18