def f(n): return n%2==0 and 99<abs(n)<1000

t = list(map(int, open('17_27299.txt')))
m = min(e for e in t if 999<e<10000)  # 1001
r = []
for i in range(len(t)-2):
    u1 = sum(f(e) for e in t[i:i+3]) >= 2
    u2 = sum(t[i:i+3]) >= m
    if u1 and u2:
        r += [sum(t[i:i+3])]
print(len(r), min(r))  # 16 1571

"""
количество троек элементов , в которых 
не менее двух трёхзначных чётных чисел, 
сумма элементов тройки не меньше 
минимального положительного четырёхзначного
"""
