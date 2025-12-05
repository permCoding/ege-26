import timeit
from fnmatch import fnmatch
import re


def f_while():
    num = 1917
    while num < 10**10+1:
        s = str(num)
        if  s[0] == '3' and \
            s[2:4] == '12' and \
            s[5:7] == '14' and \
            s[-1] == '5': 
                pass
                # print(num, num // 1917)
        num += 1917


def f_for():
    for num in range(1917, 10**10+1, 1917):
        s = str(num)
        if  s[0] == '3' and \
            s[2:4] == '12' and \
            s[5:7] == '14' and \
            s[-1] == '5': 
                pass
                # print(num, num // 1917)


def f_re_compile():
    ptn = re.compile('3.12.14.*5$')
    for num in range(1917, 10**10+1, 1917):
        s = str(num)
        if ptn.match(s):
            pass
            # print(num, num // 1917)


def f_re():
    for num in range(1917, 10**10+1, 1917):
        s = str(num)
        if re.match('3.12.14.*5$', s):
            pass
            # print(num, num // 1917)


def f_fnmatch():
    for num in range(1917, 10**10+1, 1917):
        s = str(num)
        if fnmatch(s, '3?12?14*5'):
            pass
            # print(num, num // 1917)


t = timeit.timeit(f_for, number=1)
print(f'time = {t:.3f} sec')  # 01.10

t = timeit.timeit(f_while, number=1)
print(f'time = {t:.3f} sec')  # 01.30

t = timeit.timeit(f_re_compile, number=1)
print(f'time = {t:.3f} sec')  # 02.30

t = timeit.timeit(f_re, number=1)
print(f'time = {t:.3f} sec')  # 04.50

t = timeit.timeit(f_fnmatch, number=1)
print(f'time = {t:.3f} sec')  # 10.50

