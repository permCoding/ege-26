lines = open('./26_23208.txt').readlines()[1:]
t = [list(map(int, line.split()))+[i+1] for i, line in enumerate(lines)]

a = sorted([e for e in t if e[0]<e[1]], key=lambda x: x[0])
b = sorted([e for e in t if e[0]>=e[1]], key=lambda x: -x[1])

print(b[0][-1], len(a))  # 503 478

"""
время шлифовки | время окрашивания детали
[
    [1, 62333, 51058], 
    [2, 88889, 72360], 
    [3, 24078, 31450], 
    [4, 28297, 6979], 
    [5, 75001, 50706]
] 
"""
