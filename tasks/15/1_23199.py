def f(x, y, a):
    return (x*y > a) or (x > y) or (11 > x)

for a in range(200, 0, -1):
    if all(f(x,y,a) for x in range(1, 200) for y in range(1, 200)):
        print(a)  # 120
        break


"""
Для какого наименьшего натурального А выражение
          (x<A) ∧ (y<3A) V (2x+y>128)
истинно при любых целых положительных х и у ?
"""