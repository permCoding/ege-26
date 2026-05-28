t = [int(e) for e in open('17.txt')]

k,m = 0,0
for i in range(len(t)-1):
    for j in range(i+1, len(t)):
        if (t[i]*t[j])%26==0:
            k += 1
            m = max(m, t[i]+t[j])

print(k, m)  # 5678937 19886
