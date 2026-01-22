f = open('./26_23283.txt')
K, N = int(f.readline()), int(f.readline())  # окна гражд

g = sorted(list(map(int, f.readline().split())) for _ in range(N))
# g.sort(key=lambda x: (x[0], x[1]))

w = [0] + [0] * K  # время окончания для каждого окна
k, last = 0, -1  # количество граждан принятых
for e in g:  # каждый гражданин
    for i in range(1, K+1):  # в каждое окно
        if e[0] > w[i]:  # гражданин пришёл после окончания приёма
            w[i] = e[1]
            k += 1
            last = i
            break

print(k, last)  # 4 1

"""
2
5
30 60
40 100
59 60
61 100
101 144
время начала и время окончания 
приёма специалистом (в минутах от начала суток)
"""