from room import Room
from player import Player
from item import Item


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

item = {
    'potion': Item("potion", "Restore HP by 100"),
    'ether': Item("ether", "Restore Magic Power by 100"),
    'antidote': Item("antiDote", "Removes Poison from one target"),
    'apocalypse': Item("apocalypse", "Sword with triple darkness damage"),
    'fairytail': Item('fairy tail', 'weapon for the wizard')

}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# association - room's inventory items
room['outside'].items = [item['potion'], item['ether']]
room['foyer'].items = [item['antidote'], item['potion']]
room['treasure'].items = [item['apocalypse'], item['fairytail']]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print("Welcome to the adventure game")
# player_name = str(input("Please pick a name for the player: "))
player = Player("yurika", room["outside"])

directions = ['n', 's', 'e', 'w']
options = ['move [n,s,e,w]', 'inventory(i)', 'take', 'drop', 'quit(q)']

print(f"\nPlayer_Name: {player.name}\nCurrent Room: {player.current_room}")

playing = True

while playing:
    if player.current_room.items:
        print(f"\nAs you look around you see:")
        for i in player.current_room.items:
            print(i)

    print("~~~~~~~~~~~~~~~~~~~~~~~\n")
    print(f"Options: {','.join(options)}\n")
# obtain user input for next move
    cmd = input("---> ").lower()
    print("~~~~~~~~~~~~~~~~~~~~~~~\n")

# check the the cmd action from user
    if len(cmd.split()) > 1:
        cmd = cmd.split()
        print(f"cmd: {cmd}")

        if cmd[0] == 'move':
            if cmd[1] in directions:
                player.travel(cmd[1])

        elif cmd[0] == 'take':
            item_in_room = False

            for item in player.current_room.items:
                if item.name == cmd[1]:
                    player.take_item(item)
                    item_in_room = True
            if not item_in_room:
                print("item selected is not in the current room")

        else:
            print("please provide a proper command")

    elif cmd == 'i' or cmd == 'inventory':
        print(f"You currently have: {player.inventory}")

    elif cmd == 'q' or cmd == 'quit':
        print("Good Bye @_@")
        playing = False

    else:
        print("Please provide an appropriate input")
