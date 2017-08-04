"""
Riddler Classic
From Dave Moran, a puzzle perfect for your next work break:

There is a bathroom in your office building that has only one toilet. There is a small sign stuck to the outside of the door that you can slide from “Vacant” to “Occupied” so that no one else will try the door handle (theoretically) when you are inside. Unfortunately, people often forget to slide the sign to “Occupied” when entering, and they often forget to slide it to “Vacant” when exiting.

Assume that 1/3 of bathroom users don’t notice the sign upon entering or exiting. Therefore, whatever the sign reads before their visit, it still reads the same thing during and after their visit. Another 1/3 of the users notice the sign upon entering and make sure that it says “Occupied” as they enter. However, they forget to slide it to “Vacant” when they exit. The remaining 1/3 of the users are very conscientious: They make sure the sign reads “Occupied” when they enter, and then they slide it to “Vacant” when they exit. Finally, assume that the bathroom is occupied exactly half of the time, all day, every day.

Two questions about this workplace situation:

If you go to the bathroom and see that the sign on the door reads “Occupied,” what is the probability that the bathroom is actually occupied?
If the sign reads “Vacant,” what is the probability that the bathroom actually is vacant?
Extra credit: What happens as the percentage of conscientious bathroom users changes?


Assumption: People will try to occupy regardless of sign status.
"""


import pandas as pd
from numpy.random import uniform

num_runs = 10000
prob_jerk = 1/3
prob_idiot = 1/3
prob_good = 1/3


def idiots(sign):
    return pd.DataFrame([{'kind':'i','sign':sign,'occupation':1},{'kind':'i','sign':sign,'occupation':0}])


def jerks(sign):
    return pd.DataFrame([{'kind':'j','sign':1,'occupation':1},{'kind':'j','sign':1,'occupation':0}])


def good(sign):
    return pd.DataFrame([{'kind':'g','sign':1,'occupation':1},{'kind':'g','sign':0,'occupation':0}])


def step(sign):
    random_number = uniform()
    if random_number < prob_good:
        return good(sign)
    if random_number < prob_good + prob_idiot:
        return idiots(sign)
    return jerks(sign)


# Bathroom time series is a set of recordings of the bathroom's state and the sign's state
# Let 0 mean vacant and 1 mean occupied
bathroom_ts = pd.DataFrame(columns=['kind','sign','occupation'])
sign = 0
for i in range(num_runs):
    bathroom_ts = bathroom_ts.append(step(sign))
    sign = bathroom_ts.tail(1)['sign'].get_values()[0]

contingency_table = bathroom_ts.groupby(['sign','occupation']).size()

print(contingency_table)

print("Probability occupied given that the sign says occupied: ")
print(bathroom_ts[(bathroom_ts.sign==1)&(bathroom_ts.occupation==1)].count().get_values()[0]/bathroom_ts[(bathroom_ts.sign==1)].count().get_values()[0])
print("Probability vacant given that the sign says vacant: ")
print(bathroom_ts[(bathroom_ts.sign==0)&(bathroom_ts.occupation==0)].count().get_values()[0]/bathroom_ts[(bathroom_ts.sign==0)].count().get_values()[0])




