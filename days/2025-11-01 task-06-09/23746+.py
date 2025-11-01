t = 'АКОРСТ'
w = [a+b+c+d+e for a in t for b in t for c in t for d in t for e in t]

mx = 0
for i in range(len(w)):
    if (i+1) % 2 == 0:
        s = w[i]
        if s[0] not in 'АСТ':
            if s.count('О') == 2:
                mx = i+1
print(mx)  # 5058
