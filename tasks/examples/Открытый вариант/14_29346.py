import sys
sys.set_int_max_str_digits(0)
n = 5*1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 - 2025
k = 0
while n > 0:
    if (n%36) % 2 == 0: k += 1
    n //= 36
print(k)  # 1013
