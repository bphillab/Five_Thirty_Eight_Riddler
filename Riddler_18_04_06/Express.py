import numpy as np

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
days_in_month_leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]

year_month = []
days = 0
for i in range(1,99):
    for j in range(12):
        if i%4==0:
            for k in range(days_in_month_leap_year[j]):
                days = days + 1
                year_month = year_month + [(i,j+1,k,days)]
        else:
            for k in range(days_in_month[j]):
                days = days + 1
                year_month = year_month + [(i,j+1,k,days)]
bad_days = [(i[0],i[1],i[2],i[3]) for i in year_month if i[0] == i[1]*i[2]]


print("Number of bad days: ", len(bad_days))
print("Distribution of bad days by year",
      [i for i in zip(range(1,100),np.bincount([i[0] for i in bad_days],minlength=100)[1:])])
worst_yr = np.max(np.bincount([i[0] for i in bad_days],minlength=100)[1:])
worst =  [i[0] for i in zip(range(1,100),np.bincount([i[0] for i in bad_days],minlength=100)[1:]) if i[1]==worst_yr]
print("Worst years: ", worst)
best =  [i[0] for i in zip(range(1,100),np.bincount([i[0] for i in bad_days],minlength=100)[1:]) if i[1]==0]
print("Best years: ", best)
days_btwn = [(bad_days[i+1][3]-bad_days[i][3],bad_days[i][0],bad_days[i][1],bad_days[i][2],bad_days[i][3]) for i in range(len(bad_days)-1)]
max_days_btwn = max([i[0] for i in days_btwn])
print("Most days between: ", [i for i in days_btwn if i[0]==max_days_btwn])
