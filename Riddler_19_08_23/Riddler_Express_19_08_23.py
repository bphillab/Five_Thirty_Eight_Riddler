"""
Riddler Express
From Jason Ash, a racket riddle:

You are an expert counterfeiter, and you specialize in forging one of the most ubiquitous notes in global circulation,
the U.S. $100 bill. You’ve been able to fool the authorities with your carefully crafted C-notes for some time, but
you’ve learned that new security features will make it impossible for you to continue to avoid detection. As a result,
you decide to deposit as many fake notes as you dare before the security features are implemented and then retire from
your life of crime.

You know from experience that the bank can only spot your fakes 25 percent of the time, and trying to deposit only
counterfeit bills would be a ticket to jail. However, if you combine fake and real notes, there’s a chance the bank will
accept your money. You have $2,500 in bona fide hundreds, plus a virtually unlimited supply of counterfeits. The bank
scrutinizes cash deposits carefully: They randomly select 5 percent of the notes they receive, rounded up to the nearest
whole number, for close examination. If they identify any note in a deposit as fake, they will confiscate the entire
sum, leaving you only enough time to flee.

How many fake notes should you add to the $2,500 in order to maximize the expected value of your bank account? How much
free money are you likely to make from your strategy?
"""

from scipy.special import binom
from math import floor
import numpy as np


def calc_number_of_ways(num_true, num_fake, num_checked):
    return binom(num_true+num_fake,num_checked)


def calc_prob_get_n_fake(num_true, num_fake, num_fake_taken, num_checked):
    return binom(num_fake, num_fake_taken)*binom(num_true, floor(num_checked)-num_fake_taken)/\
           calc_number_of_ways(num_true, num_fake, num_checked)


def calc_prob_evade_with_n_fake(n_fake, p_caught):
    return (1-p_caught)**n_fake


def calc_expected_value_n_fake(num_true, num_fake, n_fake, num_checked, p_caught):
    return calc_prob_get_n_fake(num_true, num_fake,n_fake, num_checked)*calc_prob_evade_with_n_fake(n_fake, p_caught)*\
           (num_true+num_fake)*100


def calc_total_expected_value(num_true, num_fake, num_checked, p_caught):
    exps = sum([calc_expected_value_n_fake(num_true, num_fake, i, num_checked, p_caught)
                for i in range(min(num_checked, num_fake))])
    return exps


