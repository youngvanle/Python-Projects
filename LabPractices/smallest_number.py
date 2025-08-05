# Program: Smallest Number Finder
# Description: Prompts the user for three integers and determines which one is the smallest.

# Initialize variable to store the smallest value
smallest_value: int = 0

# Prompt user for three integer inputs
x = int(input('Enter first value: '))
y = int(input('Enter second value: '))
z = int(input('Enter third value: '))

# Check if x is the smallest
if x <= y and x <= z:
    smallest_value = x
# Check if y is the smallest
elif y <= x and y <= z:
    smallest_value = y
# Otherwise, z is the smallest
else:
    smallest_value = z

# Output the result
print('The smallest value is', smallest_value)