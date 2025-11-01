tpl = ('А', 'И' ,'С', 'И')

res = True
for ch in tpl:
    if tpl.count(ch) > 1:
        res = False

print(res)