s = open('./24_21908.txt').read()

t, tmp, mx = [], '', 0
for ch in s:
    if ch not in '0123456789ABCD':
        tmp = ''
        continue

    tmp += ch
    tmp = tmp.lstrip('0')
    if tmp != '' and tmp[-1] in '02468AC':
        mx = max(mx, len(tmp))

print(mx)  # 2598
