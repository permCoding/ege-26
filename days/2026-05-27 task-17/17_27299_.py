def check(sl):
    u1 = sum(n%2==0 and 99<abs(n)<1000 for n in sl) >= 2
    u2 = sum(sl) >= m
    return u1 and u2

t = list(map(int, open('17_27299.txt')))
m = min(e for e in t if 999<e<10000)  # 1001
r = [sum(t[i:i+3]) for i in range(len(t)-2) if check(t[i:i+3])]
print(len(r), min(r))  # 16 1571

"""
количество троек элементов , в которых 
не менее двух трёхзначных чётных чисел, 
сумма элементов тройки не меньше 
минимального положительного четырёхзначного
"""
