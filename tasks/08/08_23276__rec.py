def p():
    letters = ['А', 'К', 'О', 'Р', 'С', 'Т']
    words = []

    def generate(current):
        if len(current) == 5:  # кол-во букв
            words.append(current[:])
        else:
            for letter in letters:
                current.append(letter)
                generate(current)
                current.pop()

    generate([])
    return words

i, last = 0, 0
for w in p():
    i += 1
    if i%2==1 and w[0] != 'А' and w.count('С') == 1:
        last = i
print(last)  # 7775

"""
Все пятибуквенные слова, составленные из букв С, Т, Р, О, К, А, записаны в алфавитном порядке и пронумерованы.
Вот начало списка:
1. AAAAA
2. ААААК
3. ААААО
4. AAAAP
5. AAAAC
6. AAAAT
Определите, под каким номером этом списке стоит последнее слово с нечетным номером, 
которые не начинается с букв А или Л 
и при этом содержит в своей записи ровно одну букву С.
"""
