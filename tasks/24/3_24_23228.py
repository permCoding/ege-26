s = open('./23228.txt').readline().strip().replace('2025','*') + '*'
lst_pos = [-1]
while s.find('*', lst_pos[-1]+1) > -1:
    lst_pos.append(s.find('*', lst_pos[-1]+1))
lst_pos = lst_pos[1:]
print(lst_pos)
for i in range(len(lst_pos)-60):
    substr = s[lst_pos[i]:lst_pos[i+60]]
    print(substr.count('Y'), len(substr) + 180)
    # print(substr, '\n')
    # break

# left = 0
# len_min = len(s)
# cnt_2025 = 0
# print(s.find('*'))
# print()
# # for right in range(len(s)):
# #     print(left, right, cnt_2025)
# #     if s[right] == '*':
# #         cnt_2025 += 1
# #         while cnt_2025 == 60:
# #             substr = s[left:right+1]
# #             if substr.count('Y') >= 120:
# #                 len_min = min(len_min, right-left+1 * 3*cnt_2025)
# #             if s[left] == '*': cnt_2025 -= 1
# #             left += 1

# print(len_min)

""" 3190
после [::-1] - разворота строки - новое условие задачи:

1) комбинация цифр 2025 встречается 60 раз
2) при этом ЗАКАНЧИВАЕТСЯ на комбинацию цифр 2025
3) содержит не менее 120 букв Y


состоит из десятичных цифр и заглавных букв латинского алфавита
Определите минимальное количество идущих подряд символов
- длину непрерывной подпоследовательности -
среди которых комбинация цифр 2025 встречается 60 раз, 
при этом искомая последовательность 
начинается на комбинацию цифр 2025 и 
содержит не менее 120 букв Y
"""