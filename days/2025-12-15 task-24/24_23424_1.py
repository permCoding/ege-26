s = open("24_23424.txt").readline().strip()

left, ln_mx = 0, 0

for right in range(len(s)):
    if s[right].isalpha():
        if (s[right] in 'AEIOUY') and (s[left] == s[right]):
            ln_mx = max(ln_mx, right - left + 1)
        left = right

print(ln_mx)  # 185
