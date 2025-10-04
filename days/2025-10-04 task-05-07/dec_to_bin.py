d = 23

print(1,2,3,'qwerty')
print(1,2,3,'qwerty', sep=' ')
print(1,2,3,'qwerty', sep=' - ')

print(d, bin(d)[2:])  # 1

print(d, f'{d:b}')  # 2
##print(d, f'{d:08b}')  # 2

print(d, format(d, 'b'))  # 3
