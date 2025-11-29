def f(s, step):
    if s <= 30: return step in [1,3]
    step += 1
    if step > 3: return False
    
    t = [f(s-3, step), f(s-5, step), f(s//4, step)]
    return all(t) if step in [2] else any(t)


for s in range(31, 666):
    if f(s, 0) and not(f(s,2)):
        print(s)  # 127 128

# 20 - Петя - 2 минимальных
# Петя = [1,3] *
# Ваня = [2]
