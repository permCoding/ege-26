f = open('./26_23208.txt')
n = int(f.readline())

t = [[i+1]+list(map(int, f.readline().split())) for i, _ in enumerate(range(n))]

a = [e for e in t if e[1] < e[2]]
b = [e for e in t if e[1] >= e[2]]

a.sort(key=lambda x: +x[1])
b.sort(key=lambda x: -x[2])

print(b[0], len(a))  # 503 478
# тут в примере была ошибка
