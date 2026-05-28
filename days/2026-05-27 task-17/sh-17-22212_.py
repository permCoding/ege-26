w = [int(e) for e in open('./17-22212.txt')]

r = [w[i:i+3] for i in range(len(w)-2) if 99<sum(w[i:i+3])<1000]

r = [sum(e) for e in r if any(x%2!=0 for x in e)]

print(len(r), max(r))  # 2 418

"""
количество троек, 
сумма элементов в которых трёхзначна
"""
