w = [int(s) for s in open('./17_23757.txt')]

amount = 0
for i in range(len(w)-1):
    a = w[i]
    b = w[i+1]
    a = len(str(a)) == 2
    b = len(str(b)) == 2
    if a ^ b:
        pass


# a = True
# b = False
# print(a ^ b)

# X Y XOR
# 0 0  0
# 0 1  1
# 1 0  1
# 1 1  0
