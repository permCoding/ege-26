lines = open('./26_21910.txt').readlines()
t = sorted(map(int, lines[1:]), reverse=True)

u = [t[0]]
for i in range(1, len(t)):
    if u[-1] - t[i] >= 9:
        u += [t[i]]
print(len(u), u[-1])  # 1040 57
