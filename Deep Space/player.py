class player:
    def __init__(self, vit, hp, atk, dfs, sci, dex, lck):
        self.vit = vit
        self.hp = hp
        self.atk= atk
        self.dfs = dfs
        self.sci = sci
        self.dex = dex
        self.lck = lck

mc = player(5, 10, 5, 5, 5, 5, 5)

mc.hp = (mc.vit*10)