t = [int(e) for e in open('./17_23952.txt')]
# mx = max(e for e in t if str(e)[-2:]=='93')
mx = max(e for e in t if e%100==93)

cnt, sm = 0, 0
for i in range(len(t)-1):
    u1 = (t[i]>mx) ^ (t[i+1]>mx)
    u2 = (str(abs(t[i]))[0] == '9') or (str(abs(t[i+1]))[0] == '9')
    if u1 and u2:
        cnt += 1
        sm += t[i] if t[i] > mx else t[i+1]
print(cnt, sm)
"""
затем сумму элементов этих пар, 
которые больше значения 
максимального элемента последовательности, 
оканчивающегося на 93.
"""