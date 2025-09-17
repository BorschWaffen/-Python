def main():
    # Reading input number N
    try:
        N = int(input("Enter integer N (1 < N < 9): "))
        if N <= 1 or N >= 9:
            print("Error: N must be between 2 and 8!")
            return
    except ValueError:
        print("Error: Please enter a valid integer!")
        return
    
    print(f"\nPattern for N = {N}:")
    print()
    
    # Generating the pattern
    for i in range(N):
        # Create numbers starting from (i+1) and decreasing the length each line
        line = ""
        current_number = i + 1
        for j in range(N - i):
            line += str(current_number)
            current_number += 1
        print(line)

if __name__ == "__main__":
    main()