def ceil(a, b):
    return a//b if a%b == 0 else a//b + 1


smb = 9  # 257 .. 512
ln = 2783
sn = ceil(ln * smb, 8)
amount = 3_845_627
print(amount * sn)
print(11 * 1024**3)