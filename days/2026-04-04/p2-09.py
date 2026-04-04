# cnt = 0
# for s in open('./09_27764.txt'):
#     t = sorted(map(int, s.strip().split()))
#     a = len(set(t)) == len(t)
#     b = 2*(t[0]+t[-1]) == sum(t[1:-1])
#     if a and b:
#         cnt += 1
# print(cnt)  # 5019

cnt = 0
for s in open('./09_27764.txt'):
    t = [int(e) for e in s.strip().split()]
    a = all(t.count(e)==1 for e in t)
    mm = min(t)+max(t)
    b = 2*mm == sum(t)-mm
    if a and b:
        cnt += 1
print(cnt)  # 5019
