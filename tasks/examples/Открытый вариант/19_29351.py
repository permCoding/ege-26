def f(a, b, st):
    if a+b >= 154: return st in [2]
    if st == 2: return False
    st += 1
    h = [
        f(a+4,b,st),
        f(a,b+4,st),
        f(a*3,b,st),
        f(a,b*3,st)
    ]
    return any(h)

for S in range(1, 143):
    if f(11, S, 0):
        print(S)  # 16
        break