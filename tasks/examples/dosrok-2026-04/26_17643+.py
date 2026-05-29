f = open('./26_17643.txt')
n = int(f.readline())
t = [list(map(int, f.readline().split())) for _ in range(n)]
arg = sum(e[1] for e in t) / len(t)  # средняя цена
tf = list(filter(lambda e: e[2]==0 and e[1]>arg, t))  # 0 - это продан

d = {e[0]: 0 for e in tf}  # словарь - артикул: кол-во продаж
for e in tf: d[e[0]] += 1

cnt_mx = max(d.items(), key=lambda e: e[1])[1]  # максимальное кол-во продаж
t_mx = [e[0] for e in d.items() if e[1] == cnt_mx]  # артикулы лучших по кол-во продаж
print(cnt_mx, t_mx)  # 51 [51786, 46481, 37134] - их продали по 51 больше всех

# std = sorted(d.items(), key=lambda e: e[1], reverse=True)
# cnt_mx = std[0][1]
# t_mx = [e[0] for e in std if e[1] == cnt_mx]  # артикулы лучших по кол-во продаж
# print(cnt_mx, t_mx)  # 51 [51786, 46481, 37134] - их продали по 51 больше всех

for art in t_mx:
    print(*next((e for e in t if e[0] == art), -1))  # первый найденный - артикул, цена, остался

# for art in t_mx:
#     for e in t:
#         if e[0] == art:
#             print(*e)
#             break
# 51786 856 0
# 46481 856 0
# 37134 831 0

for art in t_mx[:2]:  # 2 лучших по 856
    k = len([e for e in t if e[0] == art and e[2] == 1])
    print(art, k)
# 51786 37
# 46481 36  # этого осталось меньше

print(856*cnt_mx, 36)

# print(ost_51786, ost_46481)  # 37 36
# print(856 * cnt_mx)  # 43656

# (51786, 51) 856  # этого осталось больше 37
# (46481, 51) 856  # этого осталось меньше 36
# (37134, 51) 831  # у этого цена ниже
