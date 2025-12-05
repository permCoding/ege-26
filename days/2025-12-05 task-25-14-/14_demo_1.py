import sys
sys.set_int_max_str_digits(7_000)

v = 2*2187**2020 \
+ 729**2021 \
- 2*243**2022 \
+ 81**2023 \
- 2*27**2024 \
- 6561

cnt = 0  # > 9
while v > 0:
    if v % 27 > 9:
        cnt += 1
    v //= 27
print(cnt)  # 3367
