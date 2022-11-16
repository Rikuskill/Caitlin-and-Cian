from data import Stats


class Player:
    name = "null"
    location = "Start"
    stats = Stats.Stats(100)

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Player id is {self.id}"
