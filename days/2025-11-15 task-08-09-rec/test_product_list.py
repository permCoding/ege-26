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
print(len(words))
