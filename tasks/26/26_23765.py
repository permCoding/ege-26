lines = open('./26_23765.txt').readlines()
t = [[i+1] + [int(s) for s in e.split()] for i, e in enumerate(lines[1:])]

b = [e for e in t if e[1] >= e[2]]
b.sort(key=lambda x: -x[2])
print(b[0], len(b)-1)  # 564 444
