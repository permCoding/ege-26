import math
al = 10 + 26 + 8164
print(al, 2**13)
smb = 14  # bit

size_sn = math.ceil(110 * smb / 8)  # byte
print(size_sn)

all_sn = (835 * size_sn) / 1024  # Kbyte
print(all_sn)  # 110

print(156 * 1024 / 835)  # 192 byte on 1 sn
print(192*8/14)
