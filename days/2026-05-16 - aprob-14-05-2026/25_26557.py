def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
    

def get_divs(n):
    t = []
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            if is_prime(i): t.append(i)
            if is_prime(n//i): t.append(n//i)
    return t


cnt = 0
n = 7_800_000
while cnt < 5:
    n += 1
    t = get_divs(n)
    M = 0 if len(t) == 0 else (max(t) + min(t))
    if (M%100 == 63) and (M%len(t)==0):
        print(n, M)
        cnt += 1

# 7800610 780063
# 7801042 8463
# 7801312 1863
# 7801916 8163
# 7802032 69663