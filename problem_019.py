"""
Problem 19:

You are given the following information, but you may prefer to do some research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September, April, June and November.
    * All the rest have thirty-one, 
    * Saving February alone, Which has twenty-eight, rain or shine. And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def start_day(year):
    s_day = 0
    for yr in range(1900,year):
        # Leap year
        if (yr%4==0 and yr%100!=0) or (yr%400==0):
            s_day+=366
        else:
            s_day+=365

    return s_day

# Fucntion to get the day of the week given the date
def get_day(full_date):
    [date,month,year] = full_date.split('-')
    date = int(date)
    year = int(year)

    days = ['sun','mon','tue','wed','thu','fri','sat']

    months = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30,
              'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}

    # Finding the start_day of the year
    s_day = start_day(year)

    # Accounting for leap years
    if (year%4==0 and year%100!=0) or (year%400==0):
        months['Feb'] = 29
    else:
        months['Feb'] = 28


    # Adjust the first day of month according to the month
    for key,val in months.items():
        if month==key:
            break
        
        # This will give us day w.r.t start date
        date += val

    # Adding the start_day to the date
    date += s_day

    # Since year starts at mon, 1%7 = 1 -> corresponds to mon in the list
    day = days[date%7]
    
    return day


months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

count = 0
for year in range(1901,2001):
    for month in months:
        day = get_day(f'1-{month}-{year}')

        if day=='sun':
            count+=1

print(count)
