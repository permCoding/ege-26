def toInt(s):
    return sum(al.index(e) * 22**p for p, e in enumerate(s[::-1]))
    

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
# s = '12345'
# for i, e in enumerate(s):
#     print(i, e)

# var 1 - самому написать toInt
# var 2 - использовать int("J", 21)

# print(ord("A"))
# al = ''.join(chr(i) for i in range(65, 65+26))