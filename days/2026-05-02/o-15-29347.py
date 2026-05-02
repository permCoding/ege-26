def f(x, l, r):
    A = l <= x <= r
    B = 22 <= x <= 40 
    C = 32 <= x <= 50
    return (not A) <= (B == C)

for ln in range(1, 222):
    check = False
    for left in range(1, 222):
        if all(f(x, left, left+ln) for x in range(1, 222)):
           check = True
           break
    if check: print(ln); break
       
# l = 0
# ln = 3
# 0123