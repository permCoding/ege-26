lines = open('./26_23765.txt').readlines()

i, b = 0, []
for line in lines[1:]:
    i += 1
    h, g = map(int, line.split())
    if h > g:
        b += [ (h, g, i) ]

b.sort(key=lambda elm: -elm[1])
print(b[0], len(b)-1)  # 564 444
