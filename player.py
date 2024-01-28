class Player():
    def __init__(self):
        self._player_class = None
        self._player_level = 1
        self._player_xp = 0
        self._player_health = 100
        self._player_attack = 10
        self._player_mana = 10

    def _warrior(self):
        self._player_class = 0
        self._player_attack = 20

    def _wizard(self):
        self._player_health = 80
        self._player_mana = 50

    def _level_up(self):
        levels = {}
        for i in range(10):
            levels[i] = i * 10
        if self._player_xp > levels[self._player_level + 1]:
            self._player_level += 1
            if self._player_class == 0:
                self._player_health += 40
                self._player_attack += 5
            if self._player_class == 1:
                self._player_health += 25
                self._player_mana += 20





