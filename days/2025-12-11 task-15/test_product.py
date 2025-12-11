from itertools import product

# pairs = []
# for pair in product(range(1, 200), repeat=2):
#     if pair[0] < pair[1]:
#         pairs.append(pair)
# print(pairs, len(pairs))


pairs = []
for l in range(1, 199):
    for r in range(l+1, 200):
        pairs.append((l, r))
print(pairs, len(pairs))
