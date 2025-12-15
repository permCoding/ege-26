s = open('./24_23568.txt').read()
for e in '0123456789':
    s = s.replace(e, '*')

for k in range(1000, 5240):
    p = k * '*'
    i = s.find(p)
    if s[i-1] == s[i+k]:
        print(k+2, i-1)  # длина=1952; позиция=310030
    if i == -1: break  # не нашли
