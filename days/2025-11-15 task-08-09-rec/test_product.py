def get_lst(s):
    if len(s) == 5:
        print(s)
    else:
        for ch in al:
            s += ch
            get_lst(s)
            s = s[:-1]

# al = "ABC"  # 'АКОРСТ'
al = 'АКОРСТ'
get_lst("")