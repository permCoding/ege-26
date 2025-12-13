def f1(s):
    mx = 0
    left = 0
    cnt_S, cnt_E = 0, 0  # S even
    ss = ''
    for right in range(0, len(s)):
        if s[right] == 'S': cnt_S += 1
        if s[right] in '02468': cnt_E += 1
        if cnt_S == 35 and cnt_E == 1 and s[left] in '02468':
            if right-left+1 > mx:
                mx = right-left+1
                ss = s[left:right+1]
        while cnt_S > 35:
            if s[left] == 'S': cnt_S -= 1
            if s[left] in '02468': cnt_E -= 1
            left += 1
    print(mx, ss, ss.count('S'), ss.count('0'), ss.count('2'), ss.count('4'), ss.count('6'), ss.count('8'))


def f2(s):
    mx = 0
    left = 0
    lst = []
    for right in range(0, len(s)):
        subs = s[left:right+1]
        cnt_S = subs.count('S')
        if cnt_S == 35:
            if subs[0] in '02468':
                mx = max(mx, right-left+1)
            lst.append(subs)
        while cnt_S > 35:
            left += 1
            subs = s[left:right+1]
            cnt_S = subs.count('S')
    print(mx, len(lst))
    for e in lst:
        print(e, '\n')


s = open('./24_23206.txt').readline()
f1(s)
# f2(s)