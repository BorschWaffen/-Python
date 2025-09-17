def main():
    print("Calculation of value X for variant 17")
    print("X = {")
    print("  2*a/b + 1, if a > b")
    print("  -445, if a = b")
    print("  (b + 5)/a, if a < b")
    print("}")
    print()
    
    # Reading values a and b
    try:
        a = float(input("Enter value a: "))
        b = float(input("Enter value b: "))
    except ValueError:
        print("Error: Please enter numeric values!")
        return
    
    # Check constraints for variant 17 (1-100)
    if a < 1 or a > 100 or b < 1 or b > 100:
        print("Error: Values a and b must be in range from 1 to 100!")
        return
    
    # Calculation of X using formulas
    if a > b:
        X = 2 * a / b + 1
        print(f"a > b: X = 2*{a}/{b} + 1 = {X}")
    elif a == b:
        X = -445
        print(f"a = b: X = -445")
    else:  # a < b
        X = (b + 5) / a
        print(f"a < b: X = ({b} + 5)/{a} = {X}")
    
    print(f"\nResult: X = {X}")

if __name__ == "__main__":
    main()