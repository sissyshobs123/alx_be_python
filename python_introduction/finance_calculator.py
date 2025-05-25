# Ask the user for income and expenses
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate annual savings
annual_savings = monthly_savings * 12

# Calculate 5% interest on annual savings
interest = annual_savings * 0.05

# Final projected savings
projected_savings = annual_savings + interest

# Display the results as integers
print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(projected_savings)}.")
