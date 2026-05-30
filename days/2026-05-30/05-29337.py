def get_cnt(num):
    cnt1 = 0
    while num > 0:
        cnt1 += num & 1
        num >>= 1
    return cnt1

def get_r(n):
    b = f"{n:b}"
    p = get_cnt(n) & 1
    return int(f'1{p}' + b[2:] + f'{p}', 2)

print(max(n for n in range(5555) if get_r(n) <= 19))  # 12
