# Program: Exact Change
# Description: Takes an amount in cents and calculates the exact number of dollars, quarters,
#              dimes, nickels, and pennies. Handles singular/plural formatting and cases with no change.

# Get user coin amount in cents
user_amount = int(input())

# Proceed only if the amount is greater than zero
if user_amount > 0:
    # Calculate number of dollars
    coin_dollar = user_amount // 100
    user_amount = user_amount % 100

    # Calculate number of quarters
    coin_quarter = user_amount // 25
    user_amount = user_amount % 25

    # Calculate number of dimes
    coin_dime = user_amount // 10
    user_amount = user_amount % 10

    # Calculate number of nickels
    coin_nickel = user_amount // 5
    user_amount = user_amount % 5

    # Remaining amount is in pennies
    coin_penny = user_amount

    # Print dollars with correct singular/plural
    if coin_dollar == 1:
        print('1 Dollar')
    elif coin_dollar > 1:
        print(coin_dollar, 'Dollars')

    # Print quarters with correct singular/plural
    if coin_quarter == 1:
        print('1 Quarter')
    elif coin_quarter > 1:
        print(coin_quarter, 'Quarters')

    # Print dimes with correct singular/plural
    if coin_dime == 1:
        print('1 Dime')
    elif coin_dime > 1:
        print(coin_dime, 'Dimes')

    # Print nickels with correct singular/plural
    if coin_nickel == 1:
        print('1 Nickel')
    elif coin_nickel > 1:
        print(coin_nickel, 'Nickels')

    # Print pennies with correct singular/plural
    if coin_penny == 1:
        print('1 Penny')
    elif coin_penny > 1:
        print(coin_penny, 'Pennies')

# Handle case where no change is needed
else:
    print('No change')