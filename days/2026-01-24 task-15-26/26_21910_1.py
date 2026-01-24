# t = map(lambda x: int(x), open('./26_21910.txt').readlines()[1:])

# t = list(map(int, open('./26_21910_.txt').readlines()[1:]))
# t.sort()

t = sorted(map(int, open('./26_21910_.txt').readlines()[1:]), reverse=True)
# t = t[::-1]
print(t)

u = [t[0]]  # список взятых
for i in range(1, len(t)):
    if u[-1] - t[i] >= 3:
        u.append(t[i])

print(u)  # 3
