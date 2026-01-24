f = open('./26_23283.txt')
K, N = int(f.readline()), int(f.readline())  # ОКОН | ГРАЖДАН
g = sorted(list(map(int, f.readline().split())) for _ in range(N))

w = [-1] * K
amount, last = 0, -1

for i in range(N):  # по людям
    for j in range(K):  # по окнам слева направо
        if g[i][0] > w[j]:
            amount += 1
            last = j+1
            w[j] = g[i][1]
            break

print(amount, last)  # 793 2

# 685 812
