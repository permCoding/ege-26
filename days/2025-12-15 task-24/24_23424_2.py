s = open("24_23424.txt").readline().strip()
for digit in '123456789': s = s.replace(digit, '0')

for cnt_dig in range(1, 666):
    pos = s.find('0' * cnt_dig)
    # if pos == -1: break
    substr = s[pos-1: pos+cnt_dig+1]
    if (s[pos-1] in "AEIOUY") and (s[pos+cnt_dig] == s[pos-1]):
        print(pos, len(substr), substr)  # 185
