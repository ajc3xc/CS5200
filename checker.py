#!/usr/bin/python3

from random import randint
from mod_exp import mod_exp

#filter out composite numbers using fermat test
#only carmechial or prime numbers should remain now
def fermat_test(n: int):
    """Perform Fermat's primality test on n using k iterations."""
    if n == 2:
        return True
    if n < 2 or (n & 1) == 0:
        return False
    
    a = randint(2, n - 2)
    if mod_exp(a, n-1, n) != 1:
        return False
    return True

#optimized specifically for 32 bit numbers only at the most
def miller_rabin_deterministic(n: int):
    if n == 2 or n == 3:
        return True
    if n <= 1 or (n & 1) == 0:
        return False

    # Write n - 1 as 2^r * d
    r, d = 0, n - 1
    while (d & 1) == 0:
        r += 1
        d //= 2

    # Optimized list of bases for numbers less than 2^32
    bases = [2, 7, 61]

    for a in bases:
        x = pow(a, d, n)  # Compute a^d % n
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # Composite
    return True  # Probably prime

def check_deterministic(n: int):
    #basic check to see if composite
    if not fermat_test(n): return False
    #tighter check to see if Carmicheal number (composite that passes fermat's theorem)
    elif not miller_rabin_deterministic(n):
        print(f"Carmicheal number {n}")
        return False
    else: return True
    

