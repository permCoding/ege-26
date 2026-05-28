t = [int(s) for s in open('17.txt')]
k, m = 0, -10**5
for i in range(len(t)-1):
    if sum(t[i:i+2])%2 == 0:
        k += 1
        m = max(m, t[i], t[i+1])
print(k, m)