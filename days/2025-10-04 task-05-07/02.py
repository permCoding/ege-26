# b = input("Введите двузначное число: ")
# d = 0
# p = 0
# for i in 5,4,3,2:
#     d = d + int(b[i]) * 2**p
#     p = p + 1
# print(d)

s = 'QWER219031902376190'  # индексация с нуля
for i in range(len(s)-1, -1, -1):  # 3 2 1 0
    print(i, s[i])
