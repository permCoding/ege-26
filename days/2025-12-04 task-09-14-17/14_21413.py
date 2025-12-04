al = '0123456789ABCDEFGHIJK'

for x in al:
    v = int(f'82934{x}2', 21) + \
        int(f'2924{x}{x}7', 21) + \
        int(f'67564{x}8', 21)
    if v % 20 == 0:
        print(v // 20)  # 72450445
        break


# from string import *
# al = digits + ascii_uppercase[:11]
# print(len(al), al)

# al = '0123456789' + ''.join(chr(i) for i in range(65, 65+11))
# print(len(al), al)
