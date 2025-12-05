def f(n):
    st = set()
    for i in range(1, int(n**.5)+1):
        if n%i == 0:
            st.add(i)
            st.add(n//i)
    return sum(list(st))


cnt, n = 0, 500_000
while cnt < 5:
    n += 1
    R = f(n)
    if R%10 == 6:
        print(n, R)
        cnt += 1

"""
500032 1070356
500035 606816
500039 501456
500050 949716
500052 1333696
"""