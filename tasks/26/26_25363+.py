lines = open('./26_25363.txt').readlines()

t = [[i+1]+list(map(int, e.split())) for i, e in enumerate(lines[1:])]

b = [e for e in t if e[1] >= e[2]]
b.sort(key=lambda x: -x[2])

print(b[0], len(b)-1)  # 667 517
