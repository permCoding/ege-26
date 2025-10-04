b = '0123456789'

print(b[0:len(b)])
print(b[:])
print(b[::-1])
print(b[len(b)-1:0:-2])


print(b[::2])
for i in range(0, len(b), 2):
    print(i, b[i])
