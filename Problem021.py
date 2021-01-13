#Problem021
def proper_divisors(n):
    proper_divisors = []
    for i in range(1, n//2+1):
        if n%i == 0:
            proper_divisors.append(i)

    return proper_divisors

numbers = {}
for i in range(1, 10000):
    numbers[i] = sum(proper_divisors(i))

# print(numbers[220])
# print(numbers[284])
assert(220 == numbers[284] and numbers[220] == 284)

sum = 0
for i in range(1, 10000):
    result1 = numbers[i]
    if result1 in numbers and i == numbers[result1] and i != result1:
        print(f'{i} : {result1} : {numbers[result1]}')
        sum += i
print(sum)
