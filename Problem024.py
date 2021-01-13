import random
def permutations(items):
    while True:
        random.shuffle(items)
        yield items

perms = []
for i, permutation in enumerate(permutations(list('0123456789'))):
    s = ''
    for item in permutation:
        s += item
    perms.append(s)
    if i == 1000000:
        break
    #print(perms)

perms.sort()
print(perms[999999])
