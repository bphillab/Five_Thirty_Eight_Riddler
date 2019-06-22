"""
From Theodore James, some further international intrigue:

Mathematician Dr. Lana Gurtin has a problem to solve. She was hired by British intelligence for a top-secret assignment,
but things have not gone according to plan. The year is 1942 and the Germans are rolling out a new and powerful tank,
the Uberpanzer. Prominently displayed on the back of each Uberpanzer is its serial number, which is simply the number of
tanks that had been built when it rolled off the line. So the first tank built has the serial number 1, the second one
built has a 2, and so on.

Recently, a number of these new tanks were spotted by British scouts who recorded the serial numbers that they saw. They
immediately sent this information to British intelligence, hoping that the serial number data could be used to estimate
the total number of Uberpanzers the Germans have built. This is when Dr. Gurtin was brought on to head the project.

But then the unexpected happened. A German spy intercepted the dossier with the data before it could reach MI6. By the
time British agents caught up with the spy, most of the data had been destroyed. However, two pieces of information were
recovered from the debris. One: The lowest serial number recorded was 22. Two: The highest serial number recorded was
114.

Luckily, Dr. Gurtin knows exactly what to do. Assuming that the original data set was a random sample of serial numbers,
what is Dr. Gurtin’s best estimate of the total number of Uberpanzers the Germans have built?

"""
"""
Let's start by trying to work out some math on this one:
Let N be the number of Uberpanzers, H be the highest serial number records, L be the lowest serial number recorded, and 
let K be the number of Uberpanzers observed.

We want: P(N|H,L)

How we get there requires some thought as to how we observed that H, L which necessitates additional info, K

P(N|H,L) = sum_{K<N} P(N,K|H,L)

In some sense we are fortunate since we should be able to get P(H,L|N,K) = binom(H-L-1, K-1)/binom(N,K) 
P(N,K|H,L) = P(H,L|N,K)P(N,K)/P(H,L) 

We must make some assumptions about P(N,K) that are going to color our analysis. Based on other approaches we could say
something like P(N|K) is uniform for N>K, but then we are left with P(K). We could assume a uniform distribution on 
P(K), but this seems unrealistic. 

Perhaps we could say something like each tank has some probability of being observed, 
use a Jeffery's Prior and average over the p?
 

"""
from scipy.special import binom


def calc_states(min_obs, max_obs, num_tank, num_obs):
    if num_tank >= max_obs and num_tank >= num_obs and max_obs-min_obs+1 >= num_obs:
        return binom(max_obs-min_obs-1, num_obs-2)/binom(num_tank, num_obs)
    return 0


def proposed_exact(min_obs, max_obs, tank_upper_bounds=None, max_num_obs=None):
    if tank_upper_bounds is None:
        tank_upper_bounds = 3*max_obs
    if max_num_obs is None:
        max_num_obs = max_obs - min_obs + 1
    norm = sum([calc_states(min_obs, max_obs, num_tank, num_obs) for num_tank in range(max_obs, tank_upper_bounds+1)
                                                                 for num_obs  in range(2, max_num_obs+1)]
               )
    return sum([calc_states(min_obs, max_obs, num_tank, num_obs)*num_tank/norm for num_tank in range(max_obs, tank_upper_bounds+1)
                                                                               for num_obs  in range(2, max_num_obs+1)]
               )


if __name__ == "__main__":
    problem_min = 22
    problem_max = 114
    mn = proposed_exact(problem_min, problem_max)
    print("Mean number of tanks: ", mn)



