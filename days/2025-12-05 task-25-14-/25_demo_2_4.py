from fnmatch import fnmatch

for num in range(1917, 10**10+1, 1917):
    s = str(num)
    if fnmatch(s, '3?12?14*5'):
        print(num, num // 1917)

"""
m = '3?12?14*5'
351261495 183235
3212614035 1675855
3412614645 1780185
3712414275 1936575
3912414885 2040905
"""