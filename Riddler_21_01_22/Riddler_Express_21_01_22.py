"""
Riddler Express
From Ernie Cohen comes a scintillating stumper of a survey:

You’re reviewing some of the survey data that was randomly collected from the residents of Riddler City. As you’ll
recall, the city is quite large.

Ten randomly selected residents were asked how many people (including them) lived in their household. As it so
happened, their answers were 1, 2, 3, 4, 5, 6, 7, 8, 9 and 10.

It’s your job to use this (admittedly limited) data to estimate the average household size in Riddler City. Your
co-worker suggests averaging the 10 numbers, which would give you an answer of about 5.5 people. But you’re not so sure.

Would your best estimate be exactly 5.5, less than 5.5 or greater than 5.5?

The answer to this is less than 5.5 because the weighting here is on people, whereas you want a weighting on
households.  Code isn't necessary and the odds of this draw are small, but let's play around for a bit.
"""
import numpy as np


def generate_a_pop(num_household, household_size):
    pop = np.random.choice(range(1, household_size + 1), num_household, replace = True)
    return sum([[i] * i for i in pop], [])


def sample_pop(pop, sample_size):
    return np.random.choice(pop, sample_size, replace = False)
