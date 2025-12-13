s = "123AAA340000003AA3AAAAAAAA35475"
s = "ABCD"
ln = 10_000
s = "A" * ln
cnt = 0
for left in range(0, len(s)):
    for right in range(left, len(s)):
        cnt += 1
        # print(left, right, s[left:right+1])
print(cnt)