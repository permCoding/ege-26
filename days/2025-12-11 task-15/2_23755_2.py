def f(pair_A, x):
    l_A, r_A = pair_A
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = l_A <= x <= r_A
    return (P) <= ((Q and (not A)) <= (not P))


lst_A = [
    (0, 25),
    (0, 40),
    (0, 200),
    (25, 40),
    (25, 64),
    (25, 115),
    (40, 64),
    (40, 115),
    (64, 115)
]

results = []
for A in lst_A:
    if all(f(A, x) for x in range(1, 333)):
        results.append(A[1]-A[0])
print(min(results))
