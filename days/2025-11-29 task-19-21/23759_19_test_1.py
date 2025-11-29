def f(s, step):
    # 2 точки останова - по s и по st
    if s <= 30:
        return step == 2  # 1

        # return True if step == 2 else False  # 2
                
        # if step == 2:  # 3
        #     return True
        # else:
        #     return False
    
    step += 1
    if step > 2: return False
    
    
    # s-3
    # s-5
    # s//4
    
    # f(s, st)   - шаг рекурсии
    


s = 80
print(f(s, 0))

# 19
# Петя = [1]
# Ваня = [2]
