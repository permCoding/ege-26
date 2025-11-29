def f(s, step):
    if s <= 30: return step == 2
    step += 1
    if step > 2: return False
    
    t = [f(s-3, step), f(s-5, step), f(s//4, step)]
    
    if step == 1:
        return all(t)
    else:
        return any(t)

for s in range(31, 666):
    if f(s, 0):
        print(s)

# 19
# Петя = [1]
# Ваня = [2]
