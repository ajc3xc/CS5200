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