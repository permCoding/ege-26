s = open("24_21908.txt").readline().strip()

l = 0
ln_mx = 0

for r in range(len(s)):
    if s[r] not in '0123456789ABCD':
        l = r+1
    else:
        substr = s[l:r+1].lstrip('0')
        if (substr != '') and (substr[-1] in '02468AC'):
            ln_mx = max(ln_mx, len(substr))

print(ln_mx)  # 2598
    
"""
    

l = 0
for r in range(len(s)):

"""