def f(y, x, dels):
    return (4<=x<=82) or (x not in dels)

def get_dels(n):
    st = set()
    for d in range(2, int(n**.5)+1):
        if n % d == 0:
            st.add(d)
            st.add(n//d)
    return st

# max_kd = 0
# for y in range(1, 30_000):
#     dels = get_dels(y)
#     if len(dels) > max_kd:
#         if all(f(y, x, dels) for x in range(1, 30_000)):
#             max_kd = len(dels)
#             print(y, max_kd)

kds = []
for y in range(1, 30_000):
    dels = get_dels(y)  # if len(dels) > 0:
    if dels and all(f(y, x, dels) for x in range(1, 30_000)):
        kds += [ (len(dels), y) ]
print(max(kds))  # 6, 385 - ответ 385
