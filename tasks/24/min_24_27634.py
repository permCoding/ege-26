s = open('./24_27634.txt', 'r').readline()

cnt = 0
mn = 10**9
l = 0
for r in range(len(s)):
    if s[r] == 'Z': 
        cnt += 1
        while cnt == 270:
            mn = min(mn, r-l+1)
            if s[l] == 'Z': cnt -= 1
            l += 1

print(mn)  # 1058
        