s = open('./24_23762.txt').readline().replace('2025','*')

mx = 0
left = 0
cnt_Y, cnt_W = 0, 0  # Y 2025
for right in range(0, len(s)):
    if s[right] == 'Y': cnt_Y += 1
    if s[right] == '*': cnt_W += 1
    if cnt_Y == 80 and cnt_W >= 90:
        mx = max(mx, right-left+1 + 3*cnt_W)
    while cnt_Y > 80:
        if s[left] == 'Y': cnt_Y -= 1
        if s[left] == '*': cnt_W -= 1
        left += 1
print(mx)