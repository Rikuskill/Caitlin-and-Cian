class enemy:
    def __init__(self, name, desc, hp, atk, dfs, dex):
        self.name = name
        self.desc = desc
        self.hp = hp
        self.atk= atk
        self.dfs = dfs
        self.dex = dex

slime = enemy("Slime", "A slime oozes toward you.", 5, 1, 2, 1)

jerboa = enemy("Giant Jerboa", "A giant jerboa hops toward you.", 6, 1, 1, 3)