def f(l, r):
    A = True
    res = []
    for x in range(l, r):
        P = 25 <= x <= 64
        Q = 40 <= x <= 115
        func = P <= ((Q and (not(A))) <= (not(P)))
        res.append( func )
    return all( res )
        

for l in range(22, 120):
    for r in range(23, 121):
        if f(l, r) == False:
            print(l, r, r-l+1)

# (x∈P)→(((x∈Q)∧¬(x∈A))→¬(x∈P))

# P -> ((Q & ~A) -> ~P)

# ((Q & ~A) -> ~P) => (~(Q & ~A) V P)

# ~(Q & ~A) => ~Q V A
# (~Q V A V P)

# P -> (~Q V A V P) => ~P V ~Q V A V P

# ~P V ~Q V A V P => ~Q V A

# P = [25; 64] и Q = [40; 115]

# Укажите наименьшую возможную длину такого отрезка A, что логическое выражение истинно при любом значении переменной х.