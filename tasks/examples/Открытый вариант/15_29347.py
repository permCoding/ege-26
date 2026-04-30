def get(x, al, ar):
    A = al <= x <= ar
    B = 22 <= x <= 40
    C = 32 <= x <= 50
    return (not A) <= (B == C)

for lenA in range(1, 222):
    for left in range(200):
        if all(get(x, left, left+lenA) for x in range(200)):
            print(lenA)  # 28
            break