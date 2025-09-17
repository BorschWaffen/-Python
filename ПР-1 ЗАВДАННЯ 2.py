def main():
    print("Calculation of student expenses for 10 months")
    print("Initial data:")
    print("- Monthly stipend: 50 UAH")
    print("- Monthly expenses: 80 UAH")
    print("- Expenses increase by 2% each month")
    print()
    
    # Initial values
    stipend = 50  # monthly stipend in UAH
    initial_expenses = 80  # initial monthly expenses in UAH
    months = 10  # number of months
    expense_increase = 0.02  # 2% monthly increase
    
    # Calculate total stipend (constant)
    total_stipend = stipend * months
    
    # Calculate total expenses with 2% monthly increase
    total_expenses = 0
    current_expenses = initial_expenses
    
    print("Month-by-month calculation:")
    print("Month | Expenses (UAH) | Cumulative Expenses (UAH)")
    print("-" * 45)
    
    for month in range(1, months + 1):
        total_expenses += current_expenses
        print(f"{month:4} | {current_expenses:13.2f} | {total_expenses:21.2f}")
        current_expenses *= (1 + expense_increase)  # increase by 2%
    
    # Calculate the amount student needs to borrow
    amount_to_borrow = total_expenses - total_stipend
    
    print("\nResults:")
    print(f"Total stipend for {months} months: {total_stipend:.2f} UAH")
    print(f"Total expenses for {months} months: {total_expenses:.2f} UAH")
    print(f"Amount student needs to borrow: {amount_to_borrow:.2f} UAH")
    
    return amount_to_borrow

if __name__ == "__main__":
    main()