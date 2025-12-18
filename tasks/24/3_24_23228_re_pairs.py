import re

s = open('./23228.txt').readline().strip().replace('2025','*')

# ver 1
# lst_left = [-1]
# while s.find('*', lst_left[-1]+1) > -1:
#     lst_left.append(s.find('*', lst_left[-1]+1))
# lst_left = lst_left[1:]

# ver 2
# lst_left = []
# pos = -1
# while s.find('*', pos+1) > -1:
#     pos = s.find('*', pos+1)
#     lst_left += [pos]

# ver 3
lst_left = [m.start() for m in re.finditer(r'\*', s)]

pairs = [(lst_left[i],lst_left[i+59]) for i in range(len(lst_left)-59)]

for pair in pairs:
    substr = s[pair[0]:pair[1]+1]
    if substr.count('Y') >= 120:
        print(substr.count('*'), pair, len(substr) + 3*60)

""" 3190
состоит из десятичных цифр и заглавных букв латинского алфавита
Определите минимальное количество идущих подряд символов
- длину непрерывной подпоследовательности -
среди которых комбинация цифр 2025 встречается 60 раз, 
при этом искомая последовательность 
начинается на комбинацию цифр 2025 и 
содержит не менее 120 букв Y
"""