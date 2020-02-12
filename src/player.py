from room import Room
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

    def travel(self, direction):
        self.current_room = self.current_room.assign_room(direction)
