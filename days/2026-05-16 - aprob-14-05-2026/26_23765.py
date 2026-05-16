lines = open('./26_23765.txt').readlines()

b = []
for line in lines[1:]:
    h, g = map(int, line.split())
    if h > g:
        b += [ (h, g) ]

b.sort(key=lambda elm: -elm[1])
print(b[0], len(b)-1)  # 565 444
