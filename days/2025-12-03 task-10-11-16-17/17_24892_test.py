t = [int(line) for line in open('./17_24892.txt')]

mx = -9999999
for elm in t:
    if elm < 0:
        if -10000 < elm < -999:
            if elm % 9 == 0:
                if elm > mx:
                    mx = elm
print(mx)
