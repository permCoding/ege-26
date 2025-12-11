def f(a, x):
    return (x%128==0) <= ((x%a!=0) <= (x%80!=0))


for a in range(1_999, 0, -1):
    if all(f(a, x) for x in range(1, 1_999)):
        print(a)  # 640
        break