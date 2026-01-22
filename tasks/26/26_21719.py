lines = open('./26_21719.txt').readlines()
lines = list(set(lines))
t = sorted(list(map(int, e.split())) for e in lines[1:])

m, k, idn = 1, 1, -1
for i in range(1, len(t)):
    a, b = t[i], t[i-1]
    if a[0] == b[0]:
        if a[1] - b[1] == 2:
            k += 1
            if k > m:
                m = k
                idn = a[0]
        else:
            k = -1000
    else:
        k = 1
print(idn, m)

"""
идентификатор студента и номер правильно решённой задачи

"""