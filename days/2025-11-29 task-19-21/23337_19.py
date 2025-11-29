from math import *

def f(k, s, step):
    if k+s <= 200: return step in [2]
    step += 1
    if step > 2: return False
    
    t = [f(k-3, s-4, step), f(k-8, s//2, step), f(ceil(k/2), s-10, step)]
    return all(t) if step in [1] else any(t)


for s in range(100, 999):
    if f(110, s, 0):
        print(s)  # 198

# 19 - Ваня
# Петя = [1]
# Ваня = [2] *
