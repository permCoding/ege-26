def f19(s, step):
    # <= 30
    return True


for s in range(31, 666):
    if f19(s, 0):
        print(s)  # min s = ?
        break
