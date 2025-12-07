def f1(s):  # O(n^2)
    ln_mx = 0
    for a in range(0, len(s)):
        for b in range(a, len(s)):
            tmp = s[a:b+1]
            if tmp == 'A' * (b-a+1):
                if ln_mx < b-a+1:
                    ln_mx = b-a+1
                    print(a, tmp)
    print(ln_mx)


def f2(s):  # O(n)
    str_find = 'A' * 10
    for a in range(0, len(s)-10):
        tmp = s[a:a+10]
        if tmp == str_find:
            print(a, tmp)


def f3(s):  # O(n*m)
    ln, ln_mx = 1, 0
    while True:
        substr = 'A' * ln
        if s.find(substr) == -1: break
        ln_mx = ln
        ln += 1
    print(f'ln_mx = {ln_mx}')


def f4(s):  # O(n^2)
    ln_mx = 0
    for a in range(0, len(s)):
        for b in range(a, len(s)):  # полный перебор
            tmp = s[a:b+1]
            if tmp.count('A') == 10:
                if b-a+1 > ln_mx:  # первую
                    ln_mx = b-a+1
                    print(a, tmp)
    print(ln_mx)

def f5(s):  # O(n) - два указателя
    ln_mx, cnt_A = 0, 0
    a = 0
    for b in range(0, len(s)):  # O(n)
        if s[b] == 'A': cnt_A += 1
        if cnt_A == 10:
            if b-a+1 > ln_mx:
                ln_mx = b-a+1
        while cnt_A > 10:
            if s[a] == 'A': cnt_A -= 1
            a += 1
    print(ln_mx)


s = 'SASAAAASAAAAAAAAAASAASSSSSSS'
# f1(s)  # O(n^2)
# f2(s)
# f3(s)

"""
найти длину максимальной подстроки из строки s
такой чтобы в подстроке было ровно 10 символов A
найти позицию начала подстроки
если таких несколько то вывести первую/последнюю

+++>>SSSSAAAAAAAAAASSSSSSS<<+++ 10
+++>>SSSSAAAASOSOSOSASSSAAAAASSSSSSS<<+++ 10
+++>>ASSSAAAAAAAAAAOOOOOOOAAAASOSOSOSASSSAAAAAAASSSSSSS<<+++ 10
"""
s = 'SASAAAASAAAFAFAASOSAAAASAASSSSSSS'
s = 'SSSSAAAAAAAAAASSSSSSS'
s = 'SSSSAAAASOSOSOSASSSAAAAASSSSSSS'
s = 'ASSSAAAAAAAAAAOOOOOOOAAAASOSOSOSASSSFAAAAAAASSSSSSS'
f4(s)  # O(n^2)
f5(s)  # два указателя