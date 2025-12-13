def f1(s):
    for e in '02468': s = s.replace(e, '8')
    mx = 1
    for left in range(0, len(s)):
        for right in range(left+mx, len(s)):
            subs = s[left:right+1]
            if subs[0] != '8' or subs.count('8')>1 or subs.count('S')>35:
                break
            if subs[0] == '8' and subs.count('S') == 35:
                mx = max(mx, len(subs))
    print(1, mx)  # 292


def f2(s):
    mx = 0
    left = 0
    for right in range(0, len(s)):
        if s[right] in '02468':
            left = right
        subs = s[left:right+1]
        if subs.count('S') == 35 and s[left] in '02468':
            mx = max(mx, right-left+1)
    print(2, mx)  # 292

def f1_plus(s):  # исправлено - эффективное решение
    mx = 0
    left = 0
    cnt_S = 0  # S
    for right in range(0, len(s)):
        if s[right] in '02468':
            left = right
            cnt_S = 0
        if s[right] == 'S': cnt_S += 1
        if cnt_S == 35 and s[left] in '02468':
            mx = max(mx, right-left+1)
    print(3, mx)  # 292


s = open('./24_23206.txt').readline()
f1(s)
f2(s)
f1_plus(s)

