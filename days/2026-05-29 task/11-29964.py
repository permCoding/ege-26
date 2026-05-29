al = 72
sm = 7  # bit per smb
for ln in range(100):
    sn = ln * sm

    cnt = 5_895_222
    val = 23 * 1024 * 1024 * 8
    if cnt * sn > val:
        print(ln)  # 5
        break