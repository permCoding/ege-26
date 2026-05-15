def is_prime(d):
    return all(d % i != 0 for i in range(2, int(d**0.5)+1))


def f(n):
    st = set()
    for d in range(2, int(n**0.5)+1):
        if n%d==0: 
            if is_prime(d): st.add(d)
            if is_prime(n//d): st.add(n//d)
    return sorted(st)


n = 7_800_000
cnt = 0
while cnt < 5:
    n += 1
    primes_div = f(n)
    M = 0
    if len(primes_div) > 0:
        M = min(primes_div)+max(primes_div)
    if (M%100 == 63) and (M%len(primes_div)==0):
        print(n, M)
        cnt += 1

# 7800610 780063
# 7801042 8463
# 7801312 1863
# 7801916 8163
# 7802032 69663