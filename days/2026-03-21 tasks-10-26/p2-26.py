f = open('./26_27779.txt')
n = int(f.readline())
t = sorted([int(line) for line in f], reverse=True)

pir = [t[0]]
for elm in t[1:]:
    if pir[-1] - elm >= 8:
        pir.append(elm)
print(len(pir), pir[-1])  # 1159 57
