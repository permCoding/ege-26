b = "01'2345'6789ABCDEF"

i = 0
while i < len(b):
    print(b[i], end='')
    i += 1

print()
s = ''
i = 0
while i < len(b):
    s += b[i]
    i += 1

print(s)
for i in range(len(b)):
    print(b[i], end='')

print()
for ch in b:
    print(ch, end='')

print()
for ch in b[::-3]:
    print(ch, end='')
