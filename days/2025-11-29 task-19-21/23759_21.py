def f(s, step):
    if s <= 30: return step in [2,4]
    step += 1
    if step > 4: return False
    
    t = [f(s-3, step), f(s-5, step), f(s//4, step)]
    return all(t) if step in [1,3] else any(t)


for s in range(31, 666):
    if f(s, 0) and not(f(s,2)):
        print(s)  # 132

# 21 - Ваня - 1 минимальное
# Петя = [1,3]
# Ваня = [2,4] *
