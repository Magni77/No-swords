
class Enemy:
    def __init__(self, name, health, attack, power, armor, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.power = power
        self.armor = armor
        self.defense = defense
        self.alive = True

    def lost_health(self, health):
        if self.health > 0:
            self.health -= health
        else:
            self.alive = False

    def eattack(self):
        return (self.power)*(self.attack/2)

    def edefense(self):
        return (self.health+self.armor)*(self.defense/10)

