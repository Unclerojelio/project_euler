#Problem030
def digits(n):
    digits = []
    for digit in str(n):
        digits.append(int(digit))
    return digits


def fifth_powers():
    n = 1000
    while True:
        sum = 0
        for digit in digits(n):
            sum += digit**5
        if n == sum:
            yield n
        n += 1

sum = 0
for result in fifth_powers():
    sum += result
    print(f'Sum: {sum}')
