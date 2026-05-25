def to_base(n, base=2):
    b = ''
    while n > 0:
        b += str(n%base)
        n //= base
    return b[::-1]  # b[0:len(b):-1]


def to_base_(n, base=2):
    b = ''
    while n > 0:
        b = str(n%base) + b
        n //= base
    return b


n = 13  # 1101
print(to_base(n, 2))
print(to_base(n))
print(to_base_(n))

print(bin(n)[2:len(bin(n))])
print(bin(n)[2:])
print(f"{n:b}")


print(f"{n:08b}")
print("01234567"[2:-1])
