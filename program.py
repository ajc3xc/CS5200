#!/usr/bin/python3

import os, sys
from math import isqrt
import multiprocessing as mp
from random import randint
from mod_exp import mod_exp
from checker import check_deterministic

#I think that using a power to generate the numbers in the first place is excusable
numbers = tuple(randint(1, 2**32 - 1) for i in range(10000))

#implementation of rabin miller primality test
def miller_rabin_prob(num):
    #number is 0 or negative or 4
    if (num < 1 or num == 4):
        return False
    #number is 1-3
    elif (num <= 3):
        return True
    
    # Find r such that n = 
    # 2^d * r + 1 for some r >= 1
    d = num - 1
    #check if d isn't odd yet
    #nothing said about checking the last bit!
    while d & 1 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        d //= 2
    
    #calculate random witness a    
    a = randint(2, num-2)
    
    x = mod_exp(a, d, num)
    
    if (x == 1 or x == num - 1): return True

    while d != num - 1:
        x = mod_exp(x, 2, num)
        d *= 2
        if x == 1:
            return False
        if x == num - 1:
            return True
    return False

    

results = tuple(miller_rabin_prob(number) for number in numbers)
checked_results = tuple(check_deterministic(number) for number in numbers)