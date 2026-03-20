f = open('./26_27636.txt')
# f = open('./26_test.txt')
S, N = map(int, f.readline().split(' '))
t = sorted(int(e) for e in f)
sm, i_exit = 0, 0
for i in range(len(t)):
    if sm + t[i] > S:
        i_exit = i
        break
    sm += t[i]
print(i_exit, len(t)-i_exit, sum(t[i_exit:]))  
# 7347 472188
