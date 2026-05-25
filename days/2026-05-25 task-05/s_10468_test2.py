n = 13

b = f"{n:b}"

print(sum(int(e) for e in list(b)))
print(sum(int(e) for e in b))
print(sum(map(int, list(b))))

from functools import reduce

r = reduce(lambda acc,cur: acc+int(cur), list(b), 0)
print(r)

print(b.count('1'))