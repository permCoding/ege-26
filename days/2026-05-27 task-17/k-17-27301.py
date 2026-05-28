t = [int(e) for e in open('./17_27301.txt')]
r = []
for i in range(len(t)-2):
    if sum(e<0 for e in t[i:i+3])==1:
        if sum(t[i:i+3]) >= 45996:
            r += [sum(t[i:i+3])]
print(len(r), min(e for e in r if abs(e)%100==45))


# print(sum([True, True, False]))

# r = []
# for e in open('./17_27301.txt'):
#     if str(abs(int(e)))[:2] == '45':
#         r.append(int(e))
# print(max(r))  # 45996
    
"""
максим элемент, 
начинающегося на 45
"""