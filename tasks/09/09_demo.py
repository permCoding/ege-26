i = 0
for s in open('./DEMO_9.csv'):
    i += 1
    if i%1000 == 0: print(i)
    a = list(map(int, s.split()))
    dct = {e: a.count(e) for e in a}
    if sorted(dct.values()) == [1,1,1,1,3]:
        x = [e for e in a if a.count(e) == 3][0]
##        p = [e for e in a if a.count(e) > 1]
        n = [e for e in a if a.count(e) < 2]
        avg = sum(n) / len(n)
        if avg <= x:
            print(i, sum(a))  # 41990 901
"""
Определите сумму чисел в строке с наибольшим
номером, для которой выполнены оба условия:
– в строке есть одно число, которое повторяется трижды,
  остальные четыре числа различны;
– среднее арифметическое неповторяющихся чисел строки
  не больше повторяющегося числа
"""
