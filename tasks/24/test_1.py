def f1(s):  # O(n^2)
    k = 0
    for a in range(0, len(s)):
        for b in range(a, len(s)):
            tmp = s[a:b+1]
            k += 1
            # print(k, tmp)
    n = len(s)
    print(n, k, n*(n+1)//2)


lst = open('./test.txt').readlines()
for s in lst:
    f1(s.strip())