lst = [2, 4, 3, 5, 222, 7]

lst = [21, 43, 3, 5, 221, 70]

print([elm%2 for elm in lst])

print([elm%2 != 0 for elm in lst])

print(all( [elm%2 for elm in lst] ))

print(all( map(lambda elm: elm%2, lst) ))


print(all( [True, False, True] ))
print(all( [True, True, True] ))


print(any( [True, True, True] ))
print(any( [False, True, False] ))
print(any( [False, False, False] ))
