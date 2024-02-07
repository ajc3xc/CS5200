#!/usr/bin/python3

import os, sys
from math import isqrt
import multiprocessing as mp
from random import randint

#I think that using a power to generate the numbers in the first place is excusable
numbers = [randint(1, 2**32 - 1) for i in range(10000)]

def power(base, exponent):
    """
    Calculate base raised to the power of exponent using exponentiation by squaring.
    
    :param base: The base number
    :param exponent: The exponent (can be negative)
    :return: The result of base ** exponent
    """
    if exponent == 0:
        return 1
    elif exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    result = 1
    while exponent > 0:
        # If exponent is odd, multiply the result by the base
        if exponent % 2 == 1:
            result *= base
        # Square the base
        base *= base
        # Divide the exponent by 2
        exponent //= 2
    return result

def mod(a: int, b: int):
    return a - b * (a // b)

#does modular exponentiation
#& used instead of % since % isn't allowed for this assignment
def mod_exp(a: int, b: int, n: int):
    result = 1
    a = mod(a, m)  # Update a if it is more than or equal to m
    
    #keep squaring and multiplying until b = 0
    #if b = 0, then a^0 mod n = 1, so return 1
    while b > 0:
        # If b is odd, multiply the result with the base a
        if b & 1:
            result = mod((result * a), m)
        
        # Square the base
        b = b // 2
        a = mod((a * a), m)
    
    return result

#deterministic prime test
def deterministic_is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = isqrt(n)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

#implementation of rabin miller primality test
def isPrime(num, a):
    #number is 0 or negative or 4
    if (num < 1 or n == 4):
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
    
    x = modexp(a, d, n)
    
    if (x == 1 or x == n - 1): return True

    while()    
    #check if miller test works   
    return millerTest()

    

results = [deterministic_is_prime(number) for number in numbers]