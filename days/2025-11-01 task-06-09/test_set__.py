tpl = ('А', 'И' ,'С', 'И')
# tpl = ('А', 'И' ,'С', 'Т')

print( all(tpl.count(ch)==1 for ch in tpl) )

print( len(set(tpl)) == len(tpl) )

# [True,True,True,True] = АИСТ
# [True,False,True,False] = АИСИ