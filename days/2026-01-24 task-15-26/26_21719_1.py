# t = [[int(e) for e in s.split()] for s in open('./26_21719_.txt').readlines()[1:]]

t = [list(map(int, s.split())) for s in open('./26_21719_.txt').readlines()[1:]]
t.sort(key=lambda e: (e[0], e[1]))  # t.sort()

for p in t: print(p)

"""
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
[60, 33]
[60, 33]
"""
