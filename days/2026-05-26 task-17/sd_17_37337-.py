t = [int(s) for s in open('./17.txt')]

cnt, sms = 0, []
for i in range(len(t)-1):
    a, b = t[i], t[i+1]
    if a%160 != b%160:
        if a%7 == 0 or b%7 == 0:
            cnt += 1
            sms.append( a+b )
print(cnt, max(sms))
