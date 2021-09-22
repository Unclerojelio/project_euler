import math

for j in range(1, 50000):
    triangle_number = sum(i for i in range(j+1))
    factors = [k for k in range(1, math.floor(math.sqrt(triangle_number+1))) if triangle_number % k == 0]
    more_factors = []
    for factor in factors:
         more_factors.append(triangle_number/factor)
    factors = factors + more_factors
    if len(factors) > 500:
        print(triangle_number, len(factors))
        break
print("Done")
