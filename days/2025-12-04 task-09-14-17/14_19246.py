al = '0123456789ABCDEFGHIJKLMNO'
print(len(al))
for x in al:
    v = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if v % 24 == 0:
        print(x, v // 24)  # 266249847
    
    
    
# v = f'135{x}21'