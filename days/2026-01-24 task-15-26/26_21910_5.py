t = [int(line) for line in open('./26_21910.txt').readlines()[1:]]
t.sort(reverse=True)

u = [t[0]]
for elm in t[1:]:
    if u[-1] >= elm + 9:
        u += [elm]

print(len(u), u[-1])  # 1040 57
