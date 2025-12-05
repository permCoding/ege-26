def is_prime(n):
    if n < 2: return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def check(n):
    for d in range(1, n+1):
        if n%d == 0:
            if is_prime(d) and is_prime(n//d):
                return sorted([d, n//d])
    return []


num = 2_750_000
cnt = 0
while cnt < 5:
    num += 1
    divs = check(num)
    if divs:
        print(num, divs[1])
        cnt += 1

"""
2750003 144737
2750009 4591
2750014 1375007
2750017 58511
2750023 3923
"""