import re

def f1(s):  # тут ответ 184 - это неверно - надо 185
    for i in '123456789': s = s.replace(i, '0')
    cnt_dec = 0
    while True:
        sub_str = '0' * cnt_dec
        pos = s.find(sub_str)
        if pos == -1: break
        if (s[pos-1] == s[pos+cnt_dec]) and (s[pos-1] in 'AEIOUY'):
            res_srt = s[pos-1] + sub_str + s[pos+cnt_dec]
            print(len(res_srt), res_srt)  # 185
        cnt_dec += 1


def f2(s):
    l = 0
    mx = 0
    for r in range(len(s)):
        if s[r].isalpha():
            if (s[l] == s[r]) and (s[r] in 'AEIOUY'):
                mx = max(mx, r-l+1)
            l = r
    print(mx)  # 185


def f3(s):
    al = 'AEIOUY'
    for cnt_digit in range(100, 200):
        ptn = rf'[{al}]\d{{{cnt_digit}}}[{al}]'  # {{ - так в регулярках экранируют спец символ
        for m in re.finditer(ptn, s):
            sub_str = m.group()
            if sub_str[0] == sub_str[-1]:
                print(len(sub_str), sub_str)  # 185
    
def f4(s):
    ln_mx = 0
    sub_str_mx = ''

    # ptn = rf'[AEIOUY]\d+[AEIOUY]'
    # ptn = rf'(?=({ptn}))'
    ptn = rf'(?=([AEIOUY]\d+[AEIOUY]))'

    for m in re.finditer(ptn, s):
        sub_str = m.group(1)
        if sub_str[0] == sub_str[-1]:
            if len(sub_str) > ln_mx:
                ln_mx = len(sub_str)
                sub_str_mx = sub_str

    print(ln_mx, sub_str_mx)  # 185


s = open('24_23424.txt').readline().strip()
# f1(s)
# f2(s)
# f3(s)
f4(s)

"""
E123432100E

файл состоит из десятичных цифр и заглавных букв латинского алфавита

Определите максимальную длину последовательности, 
которая начинается и заканчивается одинаковой гласной буквой 
и не содержит букв внутри

В ответе - количество символов в найденной посл-ти

гласными буквами считаются AEIOUY
"""