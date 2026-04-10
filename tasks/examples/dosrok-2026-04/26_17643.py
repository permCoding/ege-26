f = open('./26_17643.txt')
n = int(f.readline())
t = [list(map(int, f.readline().split())) for _ in range(n)]

arg = sum(e[1] for e in t) / len(t)
print(arg)

tf = list(filter(lambda e: e[2]==1 and e[1]>arg, t))
nt = sorted(
    sorted(tf, key=lambda e: e[0]),
    key=lambda e: e[1],
    reverse=True
)
# for e in nt: print(e)
art = -1
mx_k, mx_art, mx_pr = 0, 0, 0
pr = 0
for e in nt:
    if e[0] != art:
        k = 1
        art = e[0]
    else:
        k += 1
        if k > mx_k:
            mx_k = k
            mx_pr = e[1]
            mx_art = e[0]
print(mx_k, mx_art, mx_pr, mx_k*mx_pr)
    