import math
b = 8  # => 2**8 == 256
one_sn = 65 * b  # bit
one_sn = math.ceil(one_sn / 8)  # byte

print(131072 * one_sn)
print(9 * 1024 * 1024)