def toInt(s):
    p = 0
    res = 0
    for e in s[::-1]:  # enumerate(s)
        res += al.index(e) * 22**p
        p += 1
    return res
    

al = '0123456789'
al += ''.join(chr(i) for i in range(65, 65+12))
print(al, len(al))  # 0123456789ABCDEFGHIJKL 22

for x in al[::-1]:
    a = '12313' + x + '57'
    b = '1' + x + '34561'
    val = toInt(a) + toInt(b)
    if val % 21 == 0:
        print(val // 21)  # 140914722
        break
        
# 1010 => 


# var 1 - самому написать toInt
# var 2 - использовать int("J", 21)

# print(ord("A"))
# al = ''.join(chr(i) for i in range(65, 65+26))