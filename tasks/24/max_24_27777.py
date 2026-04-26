s = open('./24_27777.txt').readline()

al = '0123456789AB'
mx = 0
d = ''
for r in range(len(s)):
    if s[r] in al:
        d += s[r]
        while len(d)>0 and d[0] == '0':
            d = d[1:]
        mx = max(mx, len(d))
    else:
        d = ''
print(mx)  # 18
        