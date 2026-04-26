s = open('24_14505.txt').readline()

gl = 'AEIOUY'
mx = 0
l = 0
for r in range(len(s)):
    if s[r] not in gl:
        if s[r-1] in gl:
            mx = max(mx, r-l)
            l = r
print(mx)  # 9052
   