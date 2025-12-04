from fnmatch import fnmatch
import timeit
import re

def solve_1():
    for n in range(1917, 10**10+1, 1917):
        s = str(n)
        if s[0]=='3' and s[2:4]=='12' and s[5:7]=='14' and s[-1]=='5':
            pass
            # print(n, n//1917)

def solve_2():
    for n in range(1917, 10**10+1, 1917):
        s = str(n)
        if fnmatch(s, '3?12?14*5'):
            pass
            # print(n, n//1917)

def solve_3():
    for n in range(1917, 10**10+1, 1917):
        if re.match('^3.12.14.*5$', str(n)):
            pass
            # print(n, n // 1917)

def solve_4():
    pattern = re.compile(r'^3.12.14.*5$')
    for n in range(1917, 10**10+1, 1917):
        if pattern.match(str(n)):
            pass
            # print(n, n // 1917)

exe_timer = timeit.timeit(solve_1, number=1)
print(f"{1} = {exe_timer:.6f} sec")

exe_timer = timeit.timeit(solve_2, number=1)
print(f"{2} = {exe_timer:.6f} sec")

exe_timer = timeit.timeit(solve_3, number=1)
print(f"{3} = {exe_timer:.6f} sec")

exe_timer = timeit.timeit(solve_4, number=1)
print(f"{4} = {exe_timer:.6f} sec")
    
"""
1 = 1.860069 sec
2 = 14.673363 sec
3 = 7.211398 sec
4 = 3.078864 sec

351261495 183235
3212614035 1675855
3412614645 1780185
3712414275 1936575
3912414885 2040905
"""