def f(a, b, count=0):
    if a in [4, 16]: count += 1
    if count == 2: return 0
    if a == b: return 1
    if a > b: return 0
    return f(a*2, b, count) + f(a**2, b, count) + f(a**3, b, count)


print(f(2, 131072))  # ____



"""
0) 
1) f(2, 131072) - 

3) 
lst = [2, 4, 16, 131072]
if not((4 in lst) and (16 in lst)):
    ++++++++++
"""