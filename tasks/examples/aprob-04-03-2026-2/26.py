f = open('./26_27779.txt')

N = int(f.readline())
t = sorted([int(e) for e in f], reverse=True)

v = [(0, t[0])]
for i in range(1, len(t)):
    if v[-1][1] - t[i] >= 8:
        v.append((i, t[i]))
    
print(len(v), v[-1][1])  # 1159 57
