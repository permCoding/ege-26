s = open('24_28943.txt').readline()

subs = ''
mn = 10**12

for e in s:
    subs += e
    if subs[-1] in 'AEIOUY':
        while subs.count('20') > 26:
            subs = subs[1:]
        if subs.count('20') == 26:
            mn = min(mn, len(subs))

print(mn)