for n in range(1, 222):
    b = f"{n:b}"
    b += str(b.count('1')%2)
    b += str(b.count('1')%2)
    r = int(b, 2)  # 110110
    if r > 77:
        print(n)  #19
        break