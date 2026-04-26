s = open("24_28943.txt").readline()
mn = 10**9

cnt20, l = 0, 0
for r in range(1, len(s)):
    if s[r-1] + s[r] == "20": cnt20 += 1
    if s[r] in 'AEIOUY':
        while cnt20 >= 26:
            if cnt20 == 26: mn = min(mn, r-l+1)
            if s[l] + s[l+1] == "20": cnt20 -= 1
            l += 1
        l = r+1
        cnt20 = 0

# ss = ''
# for r in range(len(s)):
#     ss += s[r]
#     if ss[-1] in 'AEIOUY':
#         while ss.count('20') >= 26:
#             if ss.count('20') == 26: mn = min(mn, len(ss))
#             ss = ss[1:]
#         ss = ''

print(mn)  # 58