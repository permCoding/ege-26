# import sys
# sys.set_int_max_str_digits(100_000_000)

dec = 5*1296**2021 - 4*216**2022 + 3*36**2023 - 2*6**2024 - 2025
cnt = 0
while dec:
    if (dec % 36)%2 == 0: cnt += 1
    dec //= 36
print(cnt)  # 1013