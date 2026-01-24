t = [list(map(int, s.split())) for s in open('./26_21719.txt').readlines()[1:]]
# можно удалить дубликаты сразу
t.sort(key=lambda e: (e[0], e[1]))
# for e in t: print(e)

k, md, mi = 1, 1, -1
for i in range(1, len(t)):
    a, b = t[i-1], t[i]
    if a[0] == b[0]:
        if b[1] == a[1]: continue
        if b[1] - a[1] == 2:
            k += 1
            if k > md:
                md = k
                mi = b[0]
        else:
            k = 1
    else:
        k = 1

print(mi, md)  # 10135 42

"""
[50, 124] [50, 126] 2
[50, 126] [50, 128] 2

идентификатор студента | номер правильно решённой задачи
студента, который решил наибольшее количество задач через одну

$ C:/Users/algop/AppData/Local/Programs/Python/Python314/python.exe "c:/Users/algop/Documents/GitHub/ege-26/days/2026-01-24 task-15-26/26_21719.py"
[40, 3]
[40, 4]
[50, 72]
[50, 124]
[50, 126]
[50, 126]
[50, 128]
[60, 31]
[60, 33]
[60, 33]
[60, 35]
"""
