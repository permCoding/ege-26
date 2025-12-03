from math import ceil


ln = 172
smb = 8  # bite => alph: 129 .. 256
sn = ceil(ln * smb / 8)  # bytes

amount = 356_984

print(amount * sn)
print(54 * 1024**2)