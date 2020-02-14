# Write a class to hold player information, e.g. what room they are in
# currently.
"""
the player in the adventure game.

Attributes:
    name: name of the player
    current_room: the room the player is currently at
"""


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []

    def travel(self, direction):
        next_room = self.current_room.assign_room(direction)
        if next_room:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("\nThat is not a valid direction input")

    def take_item(self, item):
        self.inventory.append(item)
        self.current_room.items.remove(item)
