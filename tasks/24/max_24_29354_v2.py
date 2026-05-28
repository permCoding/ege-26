s = open("24-29354.txt").readline().strip()

t = [-2]+[i for i in range(len(s)-1) if s[i:i+2] == 'BC']+[len(s)]

d = 190
max_len = 0
for j in range(len(t) - d - 1):
    ln = t[j+d+1] - t[j] - 2
    max_len = max(max_len, ln)
print(max_len)  # 2285 | но 2287 - правильный ответ

# t = [-2]+[i for i in range(len(s)-1) if s[i:i+2] == 'BC']+[len(s)]
#
# d = 190
# r = [t[j+d+1]-(t[j]+2) for j in range(len(t)-d-1)]
# print(max(r)) # 2285 | но 2287 - правильный ответ
#
# s = 'BC**BC***BC*BC'  # len=4
# s = '12BC345BC6BCBC'  # len=4

# mx, cntBC, l = 0, 0, 0
# for r in range(1, len(s)):
#     if s[r-1:r+1] == 'BC': cntBC += 1
#     while cntBC > 190:
#         if s[l:l+2] == 'BC':
#             cntBC -= 1
#         l += 1
#     if cntBC == 190: mx = max(mx, r-l+1)
# print(mx)  # 2287
