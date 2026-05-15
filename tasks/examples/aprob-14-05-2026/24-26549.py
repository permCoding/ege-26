s = open('./24_26549.txt').readline()

cnt50, l, mx = 0, 0, 0
for r in range(3,len(s)):
    if s[r-3:r+1] == '2025': cnt50 += 1
    while cnt50 > 50:
        if s[l:l+4] == '2025': cnt50 -= 1
        l += 1
    if cnt50 == 50 and s[r-3:r+1] == '2025':
        if s[l:r+1].count('Y') >= 140:
            mx = max(mx, r-l+1)
print(mx)  # 938


# s = open('./24_26549.txt').readline().replace('2025','#')

# cnt50, mx, ss = 0, 0, ''
# for r in range(len(s)):
#     ss += s[r]
#     if s[r] == '#': cnt50 += 1
    
#     while cnt50 > 50:
#         if ss[0] == '#': cnt50 -= 1
#         ss = ss[1:]
        
#     if cnt50 == 50 and s[r] == '#':
#         if ss.count('Y') >= 140:
#             mx = max(mx, len(ss) + 3*50)
# print(mx)  # 935 - а надо 938

# cnt50, l, mx = 0, 0, 0
# for r in range(len(s)):
#     if s[r] == '#': cnt50 += 1
#     while cnt50 > 50:
#         if s[l] == '#': cnt50 -= 1
#         l += 1
#     if cnt50 == 50 and s[r] == '#':
#         if s[l:r+1].count('Y') >= 140:
#             # print(l, r, s[l:r+1].count('Y'))
#             mx = max(mx, r-l+1 + 3*50)
# print(mx)  # 935 - а надо 938

# cnt50, cntY, l, mx = 0, 0, 0, 0
# for r in range(len(s)):
#     if s[r] == '#': cnt50 += 1
#     if s[r] == 'Y': cntY += 1
#     while cnt50 > 50:
#         if s[l] == '#': cnt50 -= 1
#         if s[l] == 'Y': cntY -= 1
#         l += 1
#     if cnt50 == 50 and s[r] == '#':
#         if cntY >= 140:
#             mx = max(mx, r-l+1 + 3*50)
# print(mx)  # 935 - а надо 938
