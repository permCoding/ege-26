al = 'АКОРСТ'
w = []
for a in al:
    for b in al:
        for c in al:
            for d in al:
                for e in al:
                    w.append(a+b+c+d+e)

for i in range(len(w)):
    if (i+1) % 2 == 0:
        s = w[i]
        if s[0] not in 'АСТ':
            if s.count('О') == 2:
                print(i+1, w[i])  # 5058
