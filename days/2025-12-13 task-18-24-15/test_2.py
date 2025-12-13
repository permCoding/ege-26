s = "123AAA340003AA3A2343AAAAAAA3547500005A5A"

for left in range(0, len(s)):
    for right in range(left, len(s)):
        subs = s[left:right+1]
        if subs.count('A') == 8:
            print(left, right, right-left+1, subs)