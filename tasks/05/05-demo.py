n = 0
while True:
    n += 1
    b = bin(n)[2:]
    if n%3 == 0:
        b += b[-3:]
    else:
        b += bin(n%3 * 3)[2:]
    r = int(b, 2)
    if r >= 200:
        print(n)  # 26
        break