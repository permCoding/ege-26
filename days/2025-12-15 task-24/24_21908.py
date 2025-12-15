s = open("24_21908.txt").readline().strip()

ln_mx = 0
substr = ''

for ch in s:
    if ch not in '0123456789ABCD':
        substr = ''
    else:
        substr = (substr+ch).lstrip('0')
        if (substr != '') and (substr[-1] in '02468AC'):
            ln_mx = max(ln_mx, len(substr))

print(ln_mx)  # 2598
    
"""
    

l = 0
for r in range(len(s)):

"""