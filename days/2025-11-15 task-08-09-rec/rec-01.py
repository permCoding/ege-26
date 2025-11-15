def add(last):
    if last == 1:
        return 1
    else:
        return last + add(last - 1)


# add(5) = 5 + add(4)
# add(4) = 4 + add(3)
# add(3) = 3 + add(2)
# add(2) = 2 + add(1)
# add(1) = 1 + add(0)
# add(0) = 0

print(add(2))  # 3
print(add(10))  # 55
print(add(100))  # 5050
print(add(4))  # 9
print(add(7))  # 25
# 0 1 2 3 4   5   6 7 8 9 10 => 5*10 + 5
# 0 1 2 3 4   50   96 97 98 99 100 => 50*100 + 50

