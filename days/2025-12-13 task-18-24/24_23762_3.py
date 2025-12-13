s = open('./24_23762.txt').readline()

mx = 0
left = 0
cnt_A = 0
for right in range(0, len(s)):
    if s[right] == 'Y': cnt_A += 1
    if cnt_A == 80: 
        if s[left:right+1].count('2025') >= 90:
            mx = max(mx, right-left+1)
    while cnt_A > 80:
        if s[left] == 'Y': cnt_A -= 1
        left += 1
print(mx)