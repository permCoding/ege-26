s = open('./24_23281.txt').readline().replace('2025', '*')

left = 0
mx = 0
cnt_Y = 0
# cnt_W = 0
for right in range(len(s)):
    if s[right] == 'Y': cnt_Y += 1
    # if s[right] == '*': cnt_W += 1

    if cnt_Y == 80:
        cnt_W = s[left:right+1].count('*')
        if cnt_W >= 90:
            mx = max(mx, right-left+1 + 3*cnt_W)
            # print(mx, left, right)

    while cnt_Y > 80:
        if s[left] == 'Y': cnt_Y -= 1
        # if s[left] == '*': cnt_W -= 1
        left += 1


print(mx)  # 2981
