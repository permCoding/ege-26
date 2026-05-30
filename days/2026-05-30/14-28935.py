from string import ascii_uppercase, digits

al = f"{digits}{ascii_uppercase}"[:23]

for x in al:
    a = "761" + x + "035"
    b = "338" + x + "932"
    v = int(a, 23) + int(b, 23)
    if v % 22 == 0:
        print(x, v//22)  # 70045642
