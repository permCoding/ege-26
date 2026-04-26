al = '0123456789ABCD'
s = open('./24_21908.txt').read()
t = []

tmp = ''
for i in range(len(s)):
    if s[i] in al:
        tmp += s[i]
        tmp = tmp.lstrip('0')
        if tmp != '' and tmp[-1] in '02468AC': 
            t += [tmp]
    else:
        tmp = ''

print(len(max(t, key=len)))
