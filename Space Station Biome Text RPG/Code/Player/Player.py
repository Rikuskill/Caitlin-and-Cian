import Code.Data.Stats

class Player:
    name = "null"
    location = "Start"
    stats = Code.Data.Stats()

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"Player id is {self.id}" 