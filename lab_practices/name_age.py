# Program: Name and Birth Year Estimator
# Description: Asks the user for their name and age, then calculates and displays their birth year.

# Prompt user for their name and capitalize the first letter
user_name = input('What is your name? ').capitalize()

# Prompt user for their age
user_age = int(input('How old are you? '))

# Import date module to get the current year
from datetime import date

# Get the current year
current_yr = date.today().year

# Calculate user's birth year
user_birthYear = current_yr - user_age

# Display greeting and estimated birth year using formatted output
print(f'Hello {user_name}! You were born in {user_birthYear}.')