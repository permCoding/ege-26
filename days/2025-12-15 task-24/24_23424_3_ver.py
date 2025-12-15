import re

s = open("24_23424.txt").readline().strip()

ln_mx = 0
for cnt_digits in range(1, 190):
    al = "AEIOUY"
    ptn = f"[{al}][0-9]{{{cnt_digits}}}[{al}]"

    for m in re.finditer(ptn, s):
        substr = m.group()
        if substr[0] == substr[-1]:
            ln_mx = max(ln_mx, len(substr))
            break
print(ln_mx)  # 185


# cnt_digits = 1
# check = True
# while check:
#     ptn = f"[0-9]{{{cnt_digits}}}"

#     check = False
#     for m in re.finditer(ptn, s):
#         print(cnt_digits)
#         check = True
#         break
    
#     cnt_digits += 1


# print(s[m.start()], s[m.end()-1])
