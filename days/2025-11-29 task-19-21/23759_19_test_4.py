def f(s, step):
    if s <= 30: return step == 2
    step += 1
    if step > 2: return False
    
    a = f(s-3, step)
    b = f(s-5, step)
    c = f(s//4, step)
    
    if step == 1:
        return all( [a, b, c] )
    else:
        return any( [a, b, c] )

for s in range(31, 666):
    if f(s, 0):
        print(s)

# 19
# Петя = [1]
# Ваня = [2]
