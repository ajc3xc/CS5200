#!/usr/bin/python3

import os, sys
from math import isqrt
import multiprocessing as mp
from random import randint
from primality import miller_rabin_prob
from checker import check_deterministic

#I think that using a power to generate the numbers in the first place is excusable
numbers = tuple(randint(1, 2**32 - 1) for i in range(10000))

#generate results
results = tuple(miller_rabin_prob(number) for number in numbers)
checked_results = tuple(check_deterministic(number) for number in numbers)

def count_true_scenarios(list1, list2):
    both_true = 0
    first_true_second_false = 0
    
    for a, b in zip(list1, list2):
        if a and b:
            both_true += 1
        elif a and not b:
            first_true_second_false += 1
    
    percentage_correct = ((both_true) / (both_true + first_true_second_false)) * 100
    return percentage_correct

# Calculate counts
percentage_correct = count_true_scenarios(results, checked_results)
print(f"Percentage Correct: {percentage_correct}")