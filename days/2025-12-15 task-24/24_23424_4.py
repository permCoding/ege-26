import re

s = open("24_23424.txt").readline().strip()

ln_mx = 0

# ptn = "[AEIOUY][0-9]{1,}[AEIOUY]"
# ptn = "[AEIOUY][0-9]+[AEIOUY]"

ptn = "(?=([AEIOUY][0-9]{1,}[AEIOUY]))"

lst = []
for m in re.finditer(ptn, s):
    substr = m.group(1)
    if substr[0] == substr[-1]:
        lst.append(substr)
lst.sort(key=len)
print(lst[-1], len(lst[-1]))
    