def f(s, step):
    if s <= 30: return step in [2]
    step += 1
    if step > 2: return False
    
    t = [f(s-3, step), f(s-5, step), f(s//4, step)]
    return all(t) if step in [1] else any(t)


for s in range(31, 666):
    if f(s, 0):
        print(s)  # 124

# 19 - Ваня
# Петя = [1]
# Ваня = [2] *
