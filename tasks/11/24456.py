from math import ceil
# макс возможн который не может использ
smb = 6  # bite => 64
# smb = 7  # 7 бит уже может исп-ся
ln = 1234  # symbols

sn = ln * smb  # bite
sn = ceil(sn / 8)  # byte

amount = 12_345_678  # count sn

v = 12 * 1024 * 1024 * 1024  # byte

print(amount * sn)  # byte
print(v)  # byte
