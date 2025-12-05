def is_prime(n):
    if n < 2: return False
    for d in range(2, int(n**0.5)+1): 
        if n%d == 0:
            return False
    return True


def f_old(n):
    divs = []
    for d in range(1, n+1):
        if n%d == 0 and is_prime(d):
            divs.append(d)
    if len(divs) == 0: return 0
    return min(divs)+max(divs)


def f(n):
    divs = set()
    for d in range(1, int(n**.5)+1):
        if n%d == 0:
            if is_prime(d): divs.add(d)
            if is_prime(n//d): divs.add(n//d)
    if len(divs) == 0: return 0
    return min(divs)+max(divs)


cnt, n = 0, 5_400_000
while cnt < 5:
    n += 1
    M = f(n)
    s = str(M)
    if M > 60_000 and s == s[::-1]:
        print(n, M)
        cnt += 1

"""
5400042 900009
5400420 90009
5400866 158851
5406116 1351531
5406420 90109
"""