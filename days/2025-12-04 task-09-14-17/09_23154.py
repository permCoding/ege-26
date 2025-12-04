numbers = []
for line in open('./09_23154.csv'):
    t = [int(e) for e in line.split()]
    p = [e for e in t if t.count(e) > 1]
    n = [e for e in t if t.count(e) < 2]
    d = {e:t.count(e) for e in t}
    if sorted(d.values()) == [1,1,1,3]:
        if p[0] < 2*min(n):
            # numbers += t  # 1
            # numbers.extend(t)  # 2
            for e in t: numbers.append(e)  # 3

print(sum(numbers)/len(numbers))  # 53
