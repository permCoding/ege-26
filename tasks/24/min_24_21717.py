s = open('./24_21717.txt').readline()
mn = 10**9
cnt = 0
l = 0
for r in range(2,len(s)):
    if s[r-2:r+1] == 'RSQ': cnt += 1
    if s[r] == 'Q': continue
    while cnt == 130:
        mn = min(mn, r-l+1)
        if s[l:l+3] == 'RSQ': cnt -= 1
        l += 1
print(mn)  # 497

"""
способ с подменой НЕ подходит
так как нельзя чтобы заканчивалось на Q
а мы сами убираем RSQ - которое заканчивается на Q
"""
# s = open('./24_21717.txt').readline().replace('RSQ', '#')
# mn = 10**9
# cnt = 0
# l = 0
# for r in range(len(s)):
#     if s[r] == '#': cnt += 1
#     if s[r] == 'Q': continue
#     while cnt == 130:
#         mn = min(mn, r-l+1 + 130*2)
#         if s[l] == '#': cnt -= 1
#         l += 1
# print(mn)  # 496 ???

