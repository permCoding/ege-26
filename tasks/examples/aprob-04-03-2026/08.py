from itertools import product

i = 0
for e in product("ИРСТУЦ", repeat=5):
    i += 1
    s = "".join(e)
    if s.count("И") == 2 and s.count("ЦЦ") == 0:
        print(i, s)  # 7525