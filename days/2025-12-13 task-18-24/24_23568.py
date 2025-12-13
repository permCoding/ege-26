s = open("24_23568.txt").readline()
for e in '0123456789': s = s.replace(e, '*')

for cnt in range(1_000, 5_000):
    pos = s.find(cnt * '*')
    if pos >= 0:
        if s[pos-1] == s[pos+cnt+1]:
            print(cnt+2, pos-1)  # 310_030
    else:
        break
# 01234
# A***A
