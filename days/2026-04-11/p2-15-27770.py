def f(A, x):
    return (x%21 == 0) <= ((x%A != 0) <= (x%77 != 0))


for A in range(1255, 0, -1):
    if all(f(A, x) for x in range(1, 1255)):
        print(A)  # 231
        break
