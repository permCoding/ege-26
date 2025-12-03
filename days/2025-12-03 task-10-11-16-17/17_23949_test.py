t = [int(e) for e in open('./17_23949.txt')]

cnt, sm = 0, 0
for i in range(len(t)-2):
    a,b,c = str(t[i]), str(t[i+1]), str(t[i+2])
    if (a[0] == a[-1]) + (b[0] == b[-1]) + (c[0] == c[-1]) == 1:
        
        if sum(len(str(t[i + j])) == 5 and str(t[i + j])[1] == '7' for j in range(3)) == 2:
        # f = [e for e in [a,b,c] if len(e)==5]
        # if len(f) == 2 and all(e[1]=='7' for e in f):
            
            cnt += 1
            sm += max(t[i], t[i+1], t[i+2])
            # print(f)
print(cnt, sm)  # 51 3584608
