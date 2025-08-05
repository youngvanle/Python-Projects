# Program: Fantasy Text Adventure Game – Legacy v2
# Description: A milestone version of a dungeon crawler where the player collects mystical artifacts
#              and must seal the portal before confronting the Demon Overlord. Includes inventory,
#              auto-pickup, and conditional win/lose logic.

# Dictionary mapping each room to its exits and any artifacts found there
rooms = {
    'Sanctuary of Light': {
        'North': 'Obsidian Keep',
        'South': 'Crystal Cavern',
        'East': 'Weeping Woods',
        'West': 'Hall of Heroes',
        'artifact': None
    },
    'Obsidian Keep': {
        'South': 'Sanctuary of Light',
        'East': 'Sunken Ruins',
        'North': None,
        'West': None,
        'artifact': 'Blade of Light'
    },
    'Sunken Ruins': {
        'West': 'Obsidian Keep',
        'East': None,
        'North': None,
        'South': None,
        'artifact': 'Sealing Stone'
    },
    'Hall of Heroes': {
        'East': 'Sanctuary of Light',
        'North': None,
        'South': None,
        'West': None,
        'artifact': 'Orb of Life'
    },
    'Crystal Cavern': {
        'North': 'Sanctuary of Light',
        'East': 'Forgotten Library',
        'South': None,
        'West': None,
        'artifact': 'Shining Elixir'
    },
    'Forgotten Library': {
        'West': 'Crystal Cavern',
        'North': None,
        'South': None,
        'East': None,
        'artifact': 'Invisible Tome'
    },
    'Weeping Woods': {
        'West': 'Sanctuary of Light',
        'North': 'Lake of Negative',
        'East': None,
        'South': None,
        'artifact': 'Amulet of Eternity'
    },
    # Final room with villain
    'Lake of Negative': {
        'South': 'Weeping Woods',
        'North': None,
        'East': None,
        'West': None,
        'artifact': 'Demon Overlord'
    }
}

# Set initial game state
current_room = 'Sanctuary of Light'
inventory = []

# List of required artifacts needed to win
required_artifacts = [
    'Blade of Light',
    'Sealing Stone',
    'Orb of Life',
    'Shining Elixir',
    'Invisible Tome',
    'Amulet of Eternity'
]

# Function to display game instructions
def show_instructions():
    message = (
        "Fantasy Text Adventure Game\n"
        "Collect all 6 mystical artifacts to seal the portal before confronting the Demon Overlord!\n"
        "Move commands: go North, go South, go East, go West\n"
        "To collect an artifact: Take\n"
        "Type 'exit' to leave the game.\n"
    )
    print(message)

# Function to show current status of the player
def show_status():
    print("------------------------------------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)

    # Display artifact in the room if not yet collected
    if rooms[current_room].get('artifact') and rooms[current_room]['artifact'] not in inventory:
        print("You see an artifact: The", rooms[current_room]['artifact'])

    # Show available directions from current room
    directions = [compass for compass in ['North', 'South', 'East', 'West'] if rooms[current_room].get(compass)]
    print("Available directions:", directions)
    print("------------------------------------------------------")

# Function to handle room transitions
def get_new_state(direction_from_user, current_location):
    if direction_from_user in rooms[current_location] and rooms[current_location][direction_from_user]:
        return rooms[current_location][direction_from_user]
    else:
        return None

# Start the game
show_instructions()

# Game loop
while True:
    show_status()

    # Auto-pickup artifact if found and not already in inventory
    artifact = rooms[current_room].get('artifact')
    if artifact and artifact not in inventory and artifact != 'Demon Overlord':
        inventory.append(artifact)
        print(artifact, "obtained!")

    # Win/lose game conditions
    if current_room == 'Lake of Negative' or len(inventory) == len(required_artifacts):
        if current_room == 'Lake of Negative' and len(inventory) == len(required_artifacts):
            print("\nYou have successfully sealed the portal and prevented the Demon Overlord from crossing into our world!")
            print("YOU WIN!")
        elif current_room == 'Lake of Negative':
            print("\nYou were unsuccessful in sealing the portal and the Demon Overlord has crossed into our world!")
            print("GAME OVER")
        else:
            print("\nYou have collected all the artifacts! You must now find and seal the portal.")
        break

    # Prompt user for next move
    user_input = input("Enter direction or command (Take/Exit): ").strip()

    # Exit game on user command
    if user_input.lower() == 'exit':
        print("You are exiting the game.")
        break

    # Handle movement command
    if user_input.lower().startswith('go '):
        direction = user_input[3:].strip().capitalize()
        new_room = get_new_state(direction, current_room)
        if new_room:
            current_room = new_room
        else:
            print("You can’t go that way.")
    else:
        print("Invalid command. Use a direction ('go North', etc.) or 'exit'.")