def f(s, st):
    if s >= 124: return st == 2
    if st == 2: return False
    st += 1
    h = [
        f(s+1, st),
        f(s+5, st),
        f(s*3, st)
    ]
    if st == 1:
        return all(h)
    else:
        return any(h)
    
for s in range(1, 124):
    if f(s, 0) and (not f(s, 1)):
        print(s)  # 41
        break