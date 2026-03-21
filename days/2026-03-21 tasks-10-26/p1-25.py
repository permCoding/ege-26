for n in range(171, 10**8+1, 171):
    s = str(n)
    if s[0]=='1' and s[-6:-4]=='23' and s[-2:]=='56':
        print(n, n//171)

# 1*23??56