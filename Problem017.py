def letter_count(n):
    words = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
            'nineteen']
    decades = ['pad', 'pad', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    count = 0
    if n < 20:
        count = len(words[n])
    elif n >= 20 and n < 100:
        count = len(decades[n//10]) + len(words[n%10])
    elif n >= 100 and n < 1000:
        if n%100 == 0:
            count = len(words[n//100] + 'hundred')
        else:
            count = len(words[n//100] + 'hundredand') + letter_count(n%100)
    elif n == 1000:
        count = len('onethousand')

    return count
    
assert letter_count(1) == 3
assert letter_count(19) == 8
assert letter_count(20) == 6
assert letter_count(21) == 9
assert letter_count(99) == 10
assert letter_count(100) == 10
assert letter_count(101) == 16
assert letter_count(115) == 20
assert letter_count(342) == 23
assert letter_count(999) == 24
assert letter_count(1000) == 11

total = 0
for i in range(1,1001):
    total += letter_count(i)
print(f'The total number of letters is {total}.')
