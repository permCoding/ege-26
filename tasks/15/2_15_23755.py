def f(lA, rA):
    for x in range(left, right):
        P = 25 <= x <= 64
        Q = 40 <= x <= 115
        A = lA <= x <= rA
        func = P <= ((Q and (not(A))) <= (not(P)))
        if func == False: return False
    return True


left, right = 1, 200
mn, mn_lr = 999, ()
for l in range(left, right):
    for r in range(l+1, right+1):
        if r-l < mn:
            if f(l, r):
                mn = r-l
                mn_lr = (l, r)
print(mn, mn_lr)

# (x∈P)→(((x∈Q)∧¬(x∈A))→¬(x∈P))

# P -> ((Q & ~A) -> ~P)

# ((Q & ~A) -> ~P) => (~(Q & ~A) V P)

# ~(Q & ~A) => ~Q V A
# (~Q V A V P)

# P -> (~Q V A V P) => ~P V ~Q V A V P

# ~P V ~Q V A V P => ~Q V A

# P = [25; 64] и Q = [40; 115]

# Укажите наименьшую возможную длину такого отрезка A, что 
# логическое выражение истинно при любом значении переменной х.