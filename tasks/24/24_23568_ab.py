s = open('./24_23568.txt').read()

kb, kd = 0, 0  # кол-во букв, кол-во цифр в цепочке
kd_mx, i_mx = 0, 0
for i in range(len(s)):  # тек поз
    if s[i] in '0123456789':
        kd += 1
    else:  # если буква
        kb += 1
        if kb == 2:
            if kd > kd_mx:
                kd_mx = kd
                i_mx = i - kd - 1
                if s[i_mx] == s[i_mx+kd+1]:
                    print(kd+2, i_mx)
            kd = 0
            kb = 1  # начинаем новую цепочку c буквы
