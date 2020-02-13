# Implement a class to hold room information. This should have name and
# description attributes.


class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = None

    def __repr__(self):
        return f'{self.name} \n\n{self.description}\nItems in the Room: {self.items}\nAvailable Exists Ahead: {self.available_exit()}'

    def assign_room(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 's':
            return self.s_to
        elif direction == 'w':
            return self.w_to
        elif direction == 'e':
            return self.e_to
        else:
            return None

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

    # def available_exit_string(self):
    #     return f"Exits: {self.available_exit()}"
