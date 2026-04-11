al = '0123456789' + ''.join(chr(i) for i in range(65, 65+12))

for x in al[::-1]:
    val = int('12313' + x + '57', 22) + int('1' + x + '34561', 22)
    if val % 21 == 0:
        print(val // 21)  # 140914722
