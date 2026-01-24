t = sorted(map(int, open('./26_21910.txt').readlines()[1:]), reverse=True)

k, n = 1, 0  # кол-во взятых, номер последнего взятого
for i in range(1, len(t)):
    if t[n] - t[i] >= 9:
        n = i
        k += 1

print(k, t[n])  # 1040 57
