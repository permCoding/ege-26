def get_lst():
    def gen_words(s):
        if len(s) == 5:
            lst.append(s)
        else:
            for ch in al:
                s += ch
                gen_words(s)
                s = s[:-1]

    lst, al = [], 'АКОРСТ'
    gen_words("")
    return lst


words = get_lst()
max_num = 0
i = 0
for s in words:
    i += 1
    if i%2 == 0:
        if not(s[0] in 'АСТ'):
            if s.count('О') == 2:
                max_num = i  # 5058
print(max_num)
