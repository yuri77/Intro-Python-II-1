# Write a class to hold player information, e.g. what room they are in
# currently.
"""
the player in the adventure game.

Attributes:
    name: name of the player
    current_room: the room the player is currently at
"""


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
