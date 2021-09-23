from itertools import permutations

perms = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

count = 0
for perm in perms:
    items = ""
    for item in perm:
        items += str(item)
    count += 1
    if count == 1000000:
        print(items)
