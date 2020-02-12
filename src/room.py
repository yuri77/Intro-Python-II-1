# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to

    def __repr__(self):
        return f'{self.name} \n{self.description}'

    def assign_room(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'w':
            return self.w_to
        elif direction == 'e':
            return self.e_to

    def available_exit(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.w_to:
            exits.append("w")
        if self.e_to:
            exits.append("e")
        return exits
