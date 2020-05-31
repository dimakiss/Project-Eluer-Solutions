# Solution to problem 19
# https://projecteuler.net/problem=19
# Run time 19.29 ms

counter=0

day_index=1 # the index of the day 0-6 then 0 is Sunday
days_by_month_index=[0,31,28,31,30,31,30,31,31,30,31,30,31]  # days in the month
for year in range(1900,2001):
    if year%4==0 and year%100==0 and year%400==0 or year%4==0 and year%100!=0: # leap year
        days_by_month_index[2]=29
    data_index=0
    for i in days_by_month_index:
        for j in range(i):
            data_index+=1
            day_index+=1
            day_index%=7
            if year>1900 and day_index==0 and data_index==1: # if Sunday on the first day of the month
                counter+=1
        data_index=0
    days_by_month_index[2] = 28 # fix the non-leap years

print(counter)
# Answer: 171
