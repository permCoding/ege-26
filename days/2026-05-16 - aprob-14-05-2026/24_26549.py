s = open('./24_26549.txt').readline()

cnt, l, max_len = 0, 0, 0
for r in range(3, len(s)):
    
    if s[r-3:r+1] == '2025': cnt += 1

    while cnt > 50:
        if s[l:l+4] == '2025': cnt -= 1
        l += 1
    
    if cnt == 50 and s[r-3:r+1] == '2025':
        if s[l:r+1].count('Y') >= 140:
            max_len = max(max_len, r-l+1)

print(max_len)  # 938


# cnt2025 = s[l:r+1].count('2025')
