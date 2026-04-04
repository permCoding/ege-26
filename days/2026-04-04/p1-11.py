ln_al = 10 + 26 + 8164
# print(ln_al, 2**13)
ln_smb = 14  # bit per smb

ln_sn_byte = 192
print(835 * ln_sn_byte)
print(156 * 1_024)

ln_sn_smb = ln_sn_byte * 8 / ln_smb
print(ln_sn_smb)  # 110
