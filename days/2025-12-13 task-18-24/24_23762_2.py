s = open('./24_23762.txt').readline()

mx = 0
left = 0
for right in range(0, len(s)):
    subs = s[left:right+1]
    cnt_A = subs.count('Y')
    if cnt_A == 80:
        if subs.count('2025') >= 90:
            mx = max(mx, right-left+1)
    while cnt_A > 80:
        left += 1
        subs = s[left:right+1]
        cnt_A = subs.count('Y')

print(mx)