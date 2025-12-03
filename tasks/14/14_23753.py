from string import *
al = digits + ascii_uppercase
# print(al[:29])
for x in al[:29]:
    s = int(f"923{x}874", 29) + int(f"524{x}6152", 29)
    if s % 28 == 0:
        print(x, s // 28)