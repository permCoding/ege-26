import re

# pattern = re.compile(r'^3\d12\d14\d{0,}5$')

pattern = re.compile(r'^3.12.14.*5$')

for n in range(1917, 10**10+1, 1917):
    if pattern.match(str(n)):
        print(n, n // 1917)
"""
351261495 183235
3212614035 1675855
3412614645 1780185
3712414275 1936575
3912414885 2040905
"""