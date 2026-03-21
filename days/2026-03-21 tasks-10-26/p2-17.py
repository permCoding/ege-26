def check(n):
    return 999<abs(n)<10_000


t = [int(e) for e in open('./17_27629.txt')]
m = max(e for e in t if check(e) and abs(e)%100==43)
# print(m)  # 9943

cnt, lst = 0, []
for i in range(1, len(t)):
    u1 = check(t[i-1]) or check(t[i])
    kv = (t[i-1]+t[i])**2
    u2 = kv < m**2
    if u1 and u2: 
        cnt +=1
        lst += [kv]
print(cnt, max(lst))

"""
максим из 
четырёхзначных элементов
оканчивающихся на 43

1) хотя бы один из элементов является четырёхзначным числом, 
2) квадрат суммы элементов пары меньше квадрата m
"""