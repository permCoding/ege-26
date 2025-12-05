from fnmatch import fnmatch


for n in range(7993, 10**10+1, 7993):
    if fnmatch(str(n), '4*4736*1'):
        print(n, n//7993)
