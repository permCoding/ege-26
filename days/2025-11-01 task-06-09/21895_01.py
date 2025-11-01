i = 0
for line in open('./9_21895.csv'):
    i += 1
    print(line, end='')
    if i > 9:
        break
