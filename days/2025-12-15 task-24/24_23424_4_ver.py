import re

s = open("24_23424.txt").readline().strip()

ptn = "(?=([AEIOUY][0-9]+[AEIOUY]))"

ln_mx = 0
for m in re.finditer(ptn, s):
    substr = m.group(1)
    if substr[0] == substr[-1]:
        ln_mx = max(ln_mx, len(substr))
print(ln_mx)  # 185
    