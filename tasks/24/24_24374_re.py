from re import *


def f1(s):
    ptn = r'[A-Z]+(\d+[A-Z]+){79}'
    for m in finditer(ptn, s):
        print(m.group())


def f2(s):
    ptn = r'[A-Z]+(\d+[A-Z]+){79}'
    ptn = rf'(?=({ptn}))'
    k = 0
    # for m in finditer(ptn, s): k += 1
    # print(k)  # 2433022
    subs_max = ''
    for m in finditer(ptn, s):
        subs = m.group(1)
        if len(subs) > len(subs_max):
            subs_max = subs
    print(subs_max)  # DXGRCQQ6YHAGLR8PTONADXIKKJMRKRRJGGXUO202WGGNOCTEYCWWEGKWJ0BKWKYNSDGQUODPRPA85G3HN84VFLDMJ3WAJMBMZM5GD4BI8LC9M9OLVPNDICIKO9CX47LKW64E6PNTKF6LPU6DAYPKGCQWR8J7SFPQ60DVOT8FJYR06B7NNCTNYC9GJ3TJDFK5ROAFEMYJDXKHUXG537CQ6OFDA3WYJ2S9Q6PZCR42OWDJQVLVETCSFZDNX3L3ZXCOJM0VNXDCM2HNY4F2TUHPBGKDRGNI5QYZO2Y5ZT1MCNQ2C49LAKBHDVN0BOKLSQISDMSPFFEFPZFZNH3CY3PB0MJW54CUV4L2HIVQJBP1WR6OKCLWUGRDEWLS8PLI9ACO32CG10BAAGQKSAY82CLFX1PBKBM887CUQXVA089MDMPY9ZHTAGJRIN6CWQKD8BLRIZURE8YEZR6YFQSE9SSIUKHCRD07HHJ1FF4CCCYR1JUH5FSG52LUMNIFI07I08LXLMRT5FYLYZLQVIIXULHKZV


def f3(s):
    subs = "DXGRCQQ6YHAGLR8PTONADXIKKJMRKRRJGGXUO202WGGNOCTEYCWWEGKWJ0BKWKYNSDGQUODPRPA85G3HN84VFLDMJ3WAJMBMZM5GD4BI8LC9M9OLVPNDICIKO9CX47LKW64E6PNTKF6LPU6DAYPKGCQWR8J7SFPQ60DVOT8FJYR06B7NNCTNYC9GJ3TJDFK5ROAFEMYJDXKHUXG537CQ6OFDA3WYJ2S9Q6PZCR42OWDJQVLVETCSFZDNX3L3ZXCOJM0VNXDCM2HNY4F2TUHPBGKDRGNI5QYZO2Y5ZT1MCNQ2C49LAKBHDVN0BOKLSQISDMSPFFEFPZFZNH3CY3PB0MJW54CUV4L2HIVQJBP1WR6OKCLWUGRDEWLS8PLI9ACO32CG10BAAGQKSAY82CLFX1PBKBM887CUQXVA089MDMPY9ZHTAGJRIN6CWQKD8BLRIZURE8YEZR6YFQSE9SSIUKHCRD07HHJ1FF4CCCYR1JUH5FSG52LUMNIFI07I08LXLMRT5FYLYZLQVIIXULHKZV" 
    cnt_d = 0
    for e in subs: 
        if e.isdigit(): 
            cnt_d += 1
            print(e)
    print(cnt_d)
    pos_l = s.find(subs)
    print(pos_l)  # 2576274 - это НЕ верный ответ, верный ответ = 2576273


s = open('./24_24374.txt').readline()
# s = "DF3UYC4I3TS8UZ93H1XNF"
# f1(s)
# f2(s)  # 2433022 - это неверный ответ
f3(s)

"""
файл состоит из десятичных цифр и заглавных букв латинского алфавита. 
Определите последовательность из максимального количества идущих подряд символов, 
удовлетворяющую условию: в ней ровно 80 отдельных слов 
слова - это последовательности подряд идущих букв, отделенные друг от друга хотя бы одной цифрой
В ответе запишите число - порядковый номер в файле первого символа найденной последовательности.
В прилагаемом файле нумерация символов начинается с нуля.
"""