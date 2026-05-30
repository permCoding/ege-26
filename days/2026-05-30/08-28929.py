from itertools import product

n = 0
for comb in product("ВИЛМОС", repeat=5):
    n += 1
    if n%2:
        if comb[0] not in "ОС":
            if comb.count("В") == 1 and comb.count("С") <= 1:
                print(n, *comb)  # 5137
