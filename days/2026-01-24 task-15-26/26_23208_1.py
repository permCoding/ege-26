lines = open('./26_23208.txt').readlines()[1:]
t = [tuple(map(int, line.split())) for line in lines]

a = sorted([e for e in t if e[0]<e[1]], key=lambda x: x[0])
b = sorted([e for e in t if e[0]>=e[1]], key=lambda x: -x[1])
# t = a + b

print(b[0], len(a))  # (96995, 96881) 478

n = -1
for i in range(0, len(t)):
    if b[0] == t[i]:
        print(i+1)  # 503
        break

"""
время шлифовки | время окрашивания детали

"""
