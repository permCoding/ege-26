def get_prime_divs(n):
    divs, d = [], 2
    
    while n % 2 == 0:
        divs += [d]
        n //= d
    
    d = 3
    while d**2 <= n:
        while n % d == 0:
            divs += [d]
            n //= d
        d += 2

    if n > 1: divs += [n]
    return divs


cnt = 0
n = 8_996_452
while cnt < 5:
    n += 1
    t = get_prime_divs(n)
    if len(t) == 2:
        if str(t[0]).count('3')==2 and str(t[1]).count('3')==2:
            print(n, max(t))
            cnt += 1

# 9001609 24133
# 9002887 38639
# 9006149 38653
# 9012167 3853
# 9012373 23531

# print(get_prime_divs(128))  # 2 2 2
# print(get_prime_divs(6))    # 2 3
# print(get_prime_divs(625))    # 5 5 5 5
# print(get_prime_divs(125))    # 5 5 5
# print(get_prime_divs(9))  # 3 3 
# print(get_prime_divs(17)) # 17
# print(get_prime_divs(121)) # 11 11