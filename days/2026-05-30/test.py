lst = [
    [12, 98, 0],
    [7, 99, 1],
    [32, 99, 1],
    [7, 55, 0]
]

print(lst)

new_lst = sorted(lst, key=lambda x: (-x[2], x[0], -x[1]))

print(lst)
print(new_lst)

