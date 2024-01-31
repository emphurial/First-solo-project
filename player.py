from items import *

class Player():
    def __init__(self):
        self._player_name = None
        self._player_class = None
        self._player_gender = None
        self._player_level = 1
        self._player_xp = 0
        self._player_gold = 0
        self._player_max_health = 100
        self._player_current_health = 100
        self._player_max_mana = 10
        self._player_current_mana = 10
        self._player_attack = 10
        self._player_defence = 10

    def _warrior(self):
        self._player_class = 'Warrior'
        self._player_attack = 20

    def _wizard(self):
        self._player_class = 'Wizard'
        self._player_max_health = 80
        self._player_max_mana = 50

    def _level_up(self):
        levels = [0, 10, 40, 100, 180, 280, 400, 540, 700, 880]
        if self._player_xp > levels[self._player_level + 1]:
            self._player_level += 1
            if self._player_class == 'Warrior':
                self._player_max_health += 40
                self._player_attack += 5
            if self._player_class == 'Wizard':
                self._player_max_health += 25
                self._player_max_mana += 20





