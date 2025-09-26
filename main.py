# main.py - main program
from mod import is_prime, calculate_z

print("=== Mathematical Functions Program ===")
print()

# Function 1: Calculate z
print("1. Calculate z = 1 / sqrt(m + sqrt(2))")
try:
    m = float(input("Enter number m: "))
    z_result = calculate_z(m)
    if z_result is not None:
        print(f"Result: z = {z_result:.6f}")
    else:
        print("Error: expression under root must be positive")
except ValueError:
    print("Error: please enter a valid number")
print()

# Function 2: Check prime number
print("2. Check if number is prime")
try:
    n = int(input("Enter number n: "))
    if is_prime(n):
        print(f"Number {n} is prime")
    else:
        print(f"Number {n} is not prime")
except ValueError:
    print("Error: please enter an integer")