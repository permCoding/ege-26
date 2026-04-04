from itertools import product as p

cnt = 0
for tpl in p('0123456', repeat=5):
    if tpl[0] != '0': # 00023   10000
        if tpl.count('0') == 1:
            if tpl.count('1') <= 2:
                cnt += 1
print(cnt)  # 5100        


def get(n):
    s = ''
    while n > 0:
        s = str(n%7) + s
        n //= 7
    return s

# print(get(6))  # '6'
# print(get(7))  # '10'
# print(get(9))  # '12'

cnt = 0
n = 0  # это десятичное
while True:
    n += 1
    v = get(n)  # oct()
    if len(v) < 5: continue
    if len(v) > 5: break
    if v.count('0') == 1 and v.count('1') <= 2:
        cnt += 1
print(cnt)  # 5100
