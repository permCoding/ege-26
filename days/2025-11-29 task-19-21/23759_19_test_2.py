def f(s, step):
    print(step, s)
    if s <= 30: return step == 2
    step += 1
    if step > 2: return False
    
    f(s-3, step)
    f(s-5, step)
    f(s//4, step)
    


s = 124
print(f(s, 0))

# 19
# Петя = [1]
# Ваня = [2]
