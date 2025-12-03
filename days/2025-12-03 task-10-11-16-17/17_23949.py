def u2(a,b,c):
    f = [e for e in [a,b,c] if len(e)==5]
    if len(f) == 2:
        if (f[0][1]=='7') and (f[1][1]=='7'):
            return True
        else:
            return False
    else:
        return False


t = [int(e) for e in open('./17_23949.txt')]

cnt, sm = 0, 0
for i in range(len(t)-2):
    a,b,c = str(t[i]), str(t[i+1]), str(t[i+2])
    u1 = (a[0] == a[-1]) + (b[0] == b[-1]) + (c[0] == c[-1]) == 1
    if u1 and u2(a,b,c):
        cnt += 1
        sm += max( t[i],t[i+1],t[i+2] )
print(cnt, sm)  # 51 3584608
