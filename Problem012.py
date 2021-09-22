for j in range(1, 1000):
    triangle_number = sum(i for i in range(j+1))
    factors = [k for k in range(1, triangle_number+1) if triangle_number % k == 0]
    if len(factors) > 120:
        print(j, triangle_number, len(factors))
        break
print("Done")
