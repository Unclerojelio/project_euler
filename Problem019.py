def days_in_month(month, year):
    if month in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
        return 31
    elif month == 'February':
        if is_leap(year):
            return 29
        return 28
    else:
        return 30

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap =  False
    if year % 400 == 0:
        leap = True
    return leap
    
def is_Sunday(day):
    if day % 6 == 0:
        return True
    return False

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

num_days = 0
count = 0
for year in range(1900, 2001):
    for month in months:
        days = days_in_month(month, year)
        for day in range(1, days+1):
            num_days += 1
            dow = num_days % 7
            if day == 1 and dow == 0 and year >= 1901:
                count += 1

print("Count: {}".format(count))
