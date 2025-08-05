# Program: Dragon Text Game – Legacy v1
# Description: This early milestone version allows a player to move between three rooms
#              using text commands. Room transitions are defined in a simple dictionary.

# Dictionary representing the game map (room connections by direction)
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}

# Set the player's starting location
current_room = 'Great Hall'

# Display game instructions
print("Welcome to the Dragon Text Game")
print("Move commands: go North, go South, go East, go West")
print("To exit the game, type: exit")

# Main game loop
while True:
    # Show current location
    print("\nYou are in the", current_room)

    # Get user input and remove extra spaces
    user_input = input("Enter your move: ").strip()

    # Exit the game if user types 'exit'
    if user_input.lower() == 'exit':
        current_room = 'Exit'
        print("You are exiting the game.")
        break

    # Handle valid movement commands
    elif user_input.lower().startswith('go '):
        # Extract and format direction from input
        direction = user_input[3:].strip().capitalize()

        # Check if the direction is valid from the current room
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You are unable to go that way.")

    # Handle all other invalid input
    else:
        print("Please use 'go' and the direction ('go North') or type 'exit'.")