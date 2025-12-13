def f1(s):  # полный перебор
    mx = 0
    for left in range(0, len(s)):
        for right in range(left, len(s)):
            subs = s[left:right+1]
            if subs.count('A') == 5:
                mx = max(mx, right-left+1)
    print(mx)

def f2(s):  # два указателя
    mx = 0
    left = 0
    for right in range(0, len(s)):
        subs = s[left:right+1]
        cnt_A = subs.count('A')
        if cnt_A == 5:
            mx = max(mx, right-left+1)
        while cnt_A > 5:
            left += 1
            subs = s[left:right+1]
            cnt_A = subs.count('A')
    print(mx)


def f3(s):  # два указателя
    mx = 0
    left = 0
    cnt_A = 0
    for right in range(0, len(s)):
        if s[right] == 'A': cnt_A += 1
        if cnt_A == 5: mx = max(mx, right-left+1)
        while cnt_A > 5:
            if s[left] == 'A': cnt_A -= 1
            left += 1
    print(mx)


s = "123AA090AAA42AAA0A000A0A"
f1(s)
f2(s)
f3(s)
