from collections import Counter

s = 'abbadeeeefadd'
lst = list(s)
ctr = Counter(lst)
dct = dict(ctr)

print(ctr)
print(dct)  # словарь сортируется по ключам

print(ctr['a'], dct['a'])
print(ctr.most_common(1))
print(ctr.most_common(2))
print(ctr.most_common(3))

pairs = [(key, dct[key]) for key in dct.keys()]
tpl = sorted(pairs, key=lambda x: x[1], reverse=True)  # сортировка по второму элементу кортежа
print(tpl)
