for x in '0123456789ABCDEF':
    a = int(f'761{x}035', 23)
    b = int(f'338{x}932', 23)
    if (a+b)%22 == 0:
        print(x, (a+b)/22)  # 70045642