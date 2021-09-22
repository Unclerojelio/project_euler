#Project Euler Problem #002

fibs = []
next_fib = 0
fibs.append(1)
fibs.append(2)
i = 2
while next_fib < 4000000:
    next_fib = fibs[i-1] + fibs[i-2]
    fibs.append(next_fib)
    i += 1

print(sum(x for x in fibs if x % 2 == 0))
