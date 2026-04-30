def f(a, b, st):
    if a+b >= 154: return st in [2,4]
    if st == 4: return False
    st += 1
    h = [
        f(a+4,b,st),
        f(a,b+4,st),
        f(a*3,b,st),
        f(a,b*3,st)
    ]
    if st in [2,4]:
        return any(h)  # Ваня
    else:
        return all(h)  # Петя

for S in range(1, 143):
    if f(11, S, 0) and (not f(11, S, 2)):
        print(S)  # 41
        break