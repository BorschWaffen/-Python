# mod.py - module with mathematical functions

def is_prime(n):
    """Check if number is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def calculate_z(m):
    """Calculate z = 1 / sqrt(m + sqrt(2))"""
    import math
    if m + math.sqrt(2) <= 0:
        return None
    return 1 / math.sqrt(m + math.sqrt(2))