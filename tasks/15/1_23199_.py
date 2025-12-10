def f(x, y, a):
    return 

for a in range(200, 0, -1):
    check = True
    for x in range(1, 200):
        for y in range(1, 200):
            f = (x*y > a) or (x > y) or (11 > x)
            if f == False: 
                check = False
                break
        if check == False: break
    if check:
        print(a)  # 120
        break

"""
Для какого наименьшего натурального А выражение
          (x<A) ∧ (y<3A) V (2x+y>128)
истинно при любых целых положительных х и у ?
"""