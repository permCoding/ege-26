def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_sum(n):
    sm = 0
    for i in range(2, n):
        if n % i == 0:
            if is_prime(i):
                sm += i
    return sm

cnt = 0
for n in range(1_475_000-1, 0, -1):
    sm = get_sum(n)
    if 0 < sm <= 42_000:
        if sm % 6 == 0:
            print(n, sm)
            cnt += 1
    if cnt == 5:
        break

"""
1474997 16662
1474992 10248
1474973 4386
1474968 204
1474954 150
"""