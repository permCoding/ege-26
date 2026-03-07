for n in range(999, 0, -1):
    b = bin(n)[2:]
    b += bin((n%3)*3)[2:] if n%3 else b[-3:]
    r = int(b, 2)
    if 120 <= r <= 140:
        print(n, r)  # 31
