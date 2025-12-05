from fnmatch import fnmatch as fn

for n in range(8993, 10**10+1, 8993):
    if fn(str(n), '89*4?5?7?'):
        print(n, n//8993)
