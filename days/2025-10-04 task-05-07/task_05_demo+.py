def get_r(n):
    # b = bin(n)[2:]  # 1
    b = format(n, 'b')  # 2
    # b = f'{n:b}'
    if n % 3 == 0:
        b += b[-3:]
    else:
        b += bin((n % 3) * 3)[2:]
    return int(b, 2)


for n in range(1, 100):
    if get_r(n) >= 200:
        print(n)
        break
