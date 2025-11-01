from itertools import product

w = list(product('АКОРСТ', repeat=5))
mx = 0
for i in range(len(w)):
    if (i+1) % 2 == 0:
        s = w[i]
        if s[0] not in 'АСТ':
            if s.count('О') == 2:
                mx = i+1
print(mx)  # 5058
