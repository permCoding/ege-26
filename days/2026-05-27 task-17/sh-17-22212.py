nums = [int(e) for e in open('./17-22212.txt')]

for i in range(len(nums)-2):
    t = nums[i:i+3]
    if 99 < sum(t) < 1000:
       print(*t, sum(t))  # 2 418

"""
количество троек, 
сумма элементов в которых трёхзначна
"""
