s = open('./24_23568.txt').readline().strip()

for ch in '123456789': s = s.replace(ch, '0')

for cnt_digits in range(1_000, 3_000):
    pos = s.find(cnt_digits * '0')
    if pos == -1: break
    if s[pos-1] == s[pos+cnt_digits]:
        print(cnt_digits+2, pos-1)  # 310030

# print(s[pos:pos+cnt_digits])

"A000A"