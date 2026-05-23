def f(A, x, y):
    return (x*y < A) or (5*x < y) or (486 <= x)

k = 10_000
for A in range(k):
    if all(f(A, x, y) for x in range(5) for y in range(5)):
        print(A)
        break

print(f(1176126, 485, 2425))

"""
x > 485
y > 2425

x = 485  y = 2425
2425 * 485 = 1176125 => A = 1176125+1
"""