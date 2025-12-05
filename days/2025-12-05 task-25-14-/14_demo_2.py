for x in '0123456789ABCDEFGHIJKLMNOPRSQ':
    v = int(f'923{x}874', 29) + int(f'524{x}6152', 29)
    if v % 28 == 0:
        print(x, v // 28)  # 3319197720
