f = open('./26_23570.txt')
N, K = map(int, f.readline().split())
g = [int(f.readline()) for _ in range(N)]  # min мощности

d = dict()  # минимальные цены для каждой мощности
for i in range(K):
    sm, sp = list(map(int, f.readline().split()))
    if sm in d:
        d[sm] = min(d[sm], sp)
    else:
        d[sm] = sp
d = sorted(d.items(), key=lambda x: (x[1],-x[0]))  # отсортированные
# по возрастанию цены, для каждой цены по убыванию мощности

prices, powers = [], []
for u in g:  # все участки
    for e in d:  # все мощности
        if e[0] >= u:  # если мощность >= мощности участка
            prices.append(e[1])
            powers.append(e[0])
            break

print(sum(prices), max(powers))  # 1879667450 924
