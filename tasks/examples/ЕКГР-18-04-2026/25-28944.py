# def prime_divs(n):
    # t, d = [], 2
    # while n > 1:
#         while n%d == 0:
#             t.append(d)
#             n //= d
#             if len(t) > 2:
#                 return []
#         d += 1
#     return t
# # print(f_mn(24))

def prime_divs(n):
    t, d = [], 2
    while n % d == 0:  # Делим на 2 пока возможно
        t.append(d)
        n //= d
        
    d = 3  # Проверяем нечетные делители от 3 до sqrt(n)
    while d * d <= n:
        while n % d == 0:
            t.append(d)
            n //= d
        d += 2
    
    if n > 1:  # Если осталось простое число больше 1
        t.append(n)
    return t
# print(prime_divs(175))

n = 8_996_452
cnt = 0
while cnt < 5:
    n += 1
    t = prime_divs(n)
    if len(t) == 2:
        if str(t[0]).count('3')==2 and str(t[1]).count('3')==2:
            print(n, max(t))
            cnt += 1
