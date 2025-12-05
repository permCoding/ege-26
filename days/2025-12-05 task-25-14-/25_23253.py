def is_prime(n):
    if n < 2: return False
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            return False
    return True


def get_M(n):
    divs = set()
    for d in range(2, int(n**.5)+1):
        if n % d == 0:
            if is_prime(d): divs.add(d)
            if is_prime(n//d): divs.add(n//d)
    if len(divs) == 0: return 0
    return min(divs) + max(divs)


cnt, n = 0, 4_500_000
while cnt < 5:
    n += 1
    M = get_M(n)
    S = str(M)
    if M > 30_000 and S == S[::-1]:
        print(n, M)
        cnt += 1
"""
4500350 90009
4500836 1125211
4501040 56265
4501698 32623
4505172 53635
"""