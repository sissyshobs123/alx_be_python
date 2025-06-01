# pattern_drawing.py

# Ask the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Start from row 0
row = 0

# Outer loop: while loop for each row
while row < size:
    # Inner loop: for loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
