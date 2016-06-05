import Hero


class Warrior(Hero):
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.armor = 0
        self.eq = []
        self.alive = True
        self.mana = 10
        self.gold = 1000
        self.lhand_weapon = []
        self.rhand_weapon = []
        self.armory = []

    def add_health(self, health):
        self.health += health

    def lost_health(self, health):
        self.health -= health

    def add_attack(self, attack):
        self.attack += attack

    def add_defense(self, defense):
        self.defense += defense

    def add_armor(self, armor):
        self.armor += armor

