def f(a, x): return (x%128==0) <= ((x%a!=0) <= (x%80!=0))


print(max(a for a in range(1, 999) if all(f(a, x) for x in range(1, 999))))