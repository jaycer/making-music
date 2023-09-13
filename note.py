# let's make a class to represent a sound or a note
# a sound or a note have these properties
# duration
# root pitch

class note:
    def __init__(self, name, duration):
        self.duration = duration
        self.name = name

    def __str__(self): 
        return f"duration {self.duration} name {self.name})"
