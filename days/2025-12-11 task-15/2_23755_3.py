def f(pair_A, x):
    l_A, r_A = pair_A
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = l_A <= x <= r_A
    return (P) <= ((Q and (not A)) <= (not P))


lst_A = [ ]
for l in range(1, 199):
    for r in range(l+1, 200):
        lst_A.append((l, r))

results = []
for A in lst_A:
    if all(f(A, x) for x in range(1, 333)):
        results.append(A[1]-A[0])
print(min(results))  # 24
