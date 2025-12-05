def func_M(n):
    divs = [d for d in range(2, n) if n % d == 0]
    if len(divs) == 0: return 0
    return divs[0] + divs[-1]


cnt = 0
num = 800_000
while cnt < 5:
    num += 1
    M = func_M(num)
    if M % 10 == 4:
        print(num, M)
        cnt += 1

"""
800004 400004
800009 114294
800013 266674
800024 400014
800033 61554
"""