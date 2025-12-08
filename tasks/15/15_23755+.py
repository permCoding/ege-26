def check(x, l, r):
    p = 25 <= x <= 64
    q = 40 <= x <= 115
    a = l <= x <= r
    result = (p) <= ((q and (not a)) <= (not p))
    return result

A = (40, 64)  # предполагаем отрезок A
# проверка по всем целым x от 0 до 130
for x in range(0, 131):
    if not check(x, *A):
        print("Ошибка при x =", x)
        break
else:
    print("Для A = [40,64] все x от 0 до 130 дают истину")

# можем проверить граничные вещественные числа
points = [0 + i*(130/1000) for i in range(1001)]
for x in points:
    if not check(x, *A):
        print("Ошибка при вещ. x =", x)
        break
else:
    print("Все проверенные вещественные дают истину")
print("Длина A =", A[1] - A[0])


# формула: p → ((q ∧ ¬a) → ¬p)
# импликация: X → Y   это  not X or Y
# part2 = (q and (not a))  # q ∧ ¬a
# part2_imp = (not part2) or (not p)  # (q ∧ ¬a) → ¬p
# result = (not p) or part2_imp
