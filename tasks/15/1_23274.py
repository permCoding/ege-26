def f(x, y, a):
    return (x < a) and (y < 3*a) or (2*x + y > 128)

for a in range(1, 200):
    if all(f(x,y,a) for x in range(1, 200) for y in range(1, 200)):
        print(a)
        break


"""
Для какого наименьшего натурального А выражение
          (x<A) ∧ (y<3A) V (2x+y>128)
истинно при любых целых положительных х и у ?
"""