from math import ceil

size_alph = 10 + 52 + 500  # 10 bite
smb = 10  # bite
ln = 896  # ?
sn = ceil((ln * smb) / 8)  # bytes
# print(sn)

amount = 45_877
print(amount * sn > 49 * 1024**2)  # bytes

