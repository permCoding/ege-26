t = [int(s) for s in open('17.txt')]
r = []
for i in range(len(t)-1):
    if sum(t[i:i+2])%2 == 0:
        r.extend(t[i:i+2])
print(len(r)//2, max(r))