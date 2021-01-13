#Problem029
the_set = {0}
for a in range(2,101):
    for b in range(2,101):
        the_set.add(a**b)

print(f'The number of terms is: {len(the_set)-1}')
