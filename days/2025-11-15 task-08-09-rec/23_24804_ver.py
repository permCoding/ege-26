def f(a, b):
    if a == b: return 1
    if a > b: return 0
    return f(a*2, b) + f(a**2, b) + f(a**3, b)


all_ways = f(2, 131072)
_ways = f(2, 4) * f(4, 16) * f(16, 131072)
print(all_ways - _ways)  # 32
print(all_ways)  # 68
print(_ways)  # 36


"""
0) 
1) f(2, 131072) - 

3) 
lst = [2, 4, 16, 131072]
if not((4 in lst) and (16 in lst)):
    ++++++++++
"""