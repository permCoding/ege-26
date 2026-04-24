def solve_1(s, amount=26):
    ss = ''
    min_len = 10**9
    for r in range(len(s)):
        ss += s[r]
        if ss[-1] == 'A':
            while ss.count('20') >= amount:
                if ss.count('20') == amount:
                    min_len = min(min_len, len(ss))
                ss = ss[1:]
            ss = ''
    print(min_len)

def solve_2(s, amount=26):
    s = s.replace('20','#')
    
    r, min_len = len(s), 10**9
    while r > amount*2:
        r -= 1
        if s[r] == 'A':
            
            cnt20, cntA, l = 0, 0, r
            while cnt20 < amount and l > 0:
                l -= 1
                if s[l] == '#': cnt20 += 1
                if s[l] == 'A': cntA += 1
                
            if cnt20 == amount and cntA == 0:
                min_len = min(min_len, r-l+1)

    print(min_len+amount)

def solve_3(s, amount=26):
    s = s.replace('20','#')
    
    min_len = 10**9
    r = len(s) - 1
    while r > amount * 2:
        while s[r] != 'A': r -= 1
        cnt20 = 0
        l = r
        while cnt20 < amount and l > 0:
            l -= 1
            if s[l] == '#': cnt20 += 1
            
        if cnt20 == amount and s[l:r+1].count('A') == 1:
            if r-l+1 < min_len:
                min_len = r-l+1
                # print(l, r, s[l:r+1])
            
        r -= 1

    print(min_len+amount)

s = open('./24_28943.txt').readline()
# s = 'PA20KZ8T220IS20D'  # 20
for c in 'EIOUY': s = s.replace(c, 'A')
solve_2(s)

'''
Текстовый файл состоит из десятичных цифр и заглавных букв латинского алфавита. 

Определите минимальное количество идущих подряд символов, среди которых 
1) пара символов «20» (в указанном порядке) встречается ровно 26 раз, 
2) гласная буква (A, E, I, O, U, Y) встречается ровно один раз, 
3) искомая последовательность заканчивается этой единственной гласной буквой. 

В ответе запишите число - количество символов в найденной последовательности.
'''