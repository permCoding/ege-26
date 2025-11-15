def add(first, last):
    if last == first:
        return last
    else:
        return last + add(first, last - 1)


print(add(1, 2))  # 3
print(add(1, 10))  # 55
print(add(0, 100))  # 5050
print(add(2, 4))  # 9
print(add(3, 7))  # 25
# 0 1 2 3 4   5   6 7 8 9 10 => 5*10 + 5
# 0 1 2 3 4   50   96 97 98 99 100 => 50*100 + 50

