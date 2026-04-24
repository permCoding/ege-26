s = open('./24_26078.txt').readline().replace('2025','#')

mn = 10**9
l = 0
cntW = 0
for r in range(len(s)):
    if s[r] == 'W': cntW += 1
    while cntW == 90:
        cnt_ = s[l:r+1].count('#')
        if cnt_ >= 110:
            mn = min(mn, r-l+1 + cnt_*3)
        if s[l] == 'W': cntW -= 1
        l += 1
print(mn)  # 780
    