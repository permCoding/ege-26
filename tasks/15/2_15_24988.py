def get_dels(n):
    st = set()
    for d in range(2, int(y**.5)+1):
        if y % d == 0:
            st.add(d)
            st.add(y//d)
    return st

def f(y, x, C):
    # A = 100 <= x <= 200
    # return (x in C) <= (A and (x != 11))
    return (x in C) <= (100 <= x <= 200)


for y in range(1, 59_999):
    dels = get_dels(y)
    if len(dels) != 0:
        if all(f(y,x, dels) for x in range(1, 59_999)):
            print(y)
            break