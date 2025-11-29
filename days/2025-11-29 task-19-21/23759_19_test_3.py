def f(s, step):
    if s <= 30: return step == 2
    step += 1
    if step > 2: return False
    
    a = f(s-3, step)
    b = f(s-5, step)
    c = f(s//4, step)
    
    if step == 1:
        return a and b and c
    else:
        return a or b or c

for s in range(31, 666):
    if f(s, 0):
        print(s)
        break

# 19
# Петя = [1]
# Ваня = [2]
