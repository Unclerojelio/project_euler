#Project Euler Problem #001
mults35 = (x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
print(sum(mults35))
