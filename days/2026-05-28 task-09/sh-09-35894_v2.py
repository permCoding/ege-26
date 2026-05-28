w = [list(map(int, e.split())) for e in open('09.csv')]
r = [1 for t in w if sum(t)-max(t)-2*min(t) >= 30 and max(t) <= 700]
print(len(r))  # 26