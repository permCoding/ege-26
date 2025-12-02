from math import ceil
# найти min мощн алфавита
# 8 => 129 .. 256
# 9 => 257 .. 512
# ответ = 257
smb = 9  # bite
ln = 2_783  # symbols
sn = ceil(ln * smb / 8)  # byte
print(sn)
amount = 3_845_627
v = 11 * 1024**3
print(amount * sn)
print(v)
