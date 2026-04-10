
def f(x, left, right):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = left <= x <= right
    return P <= ((Q and (not A)) <= (not P))

def check(ln):
    for left in range(1, 200):
        if all(f(x, left, left+ln) for x in range(1, 200)):
            return True
    return False

for ln in range(1, 100):
    if check(ln):
        print(ln)
        break
