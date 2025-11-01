w = ["ААААА", "ААААК", "ОАСТО", "ОАСТР", "КАСТО", "РАСОО"]

for i in range(len(w)):
    if (i+1) % 2 == 0:
        s = w[i]
        if s[0] not in 'АСТ':
            if s.count('О') == 2:
                print(i+1, w[i])

##s = 'ОАСТО'
##print(s[0] == 'А')
##print(s[0] != 'А')
##print(s[0] != 'А' and s[0] != 'С' and s[0] != 'Т')
##print(s[0] in 'АСТ')
##print(s[0] not in 'АСТ')
##print(not(s[0] in 'АСТ'))
