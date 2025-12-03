from math import ceil

smb = 7  # bite - может: 65 .. 128
smb = 6  # bite - НЕ может: 33 .. 64 
ln = 1234  # smb
sn = ceil(ln * smb / 8)  # bites
# print(sn)

amount = 12_345_678

print(amount * sn)
print(12 * 1024**3)  # bytes
