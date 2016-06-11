class Enemy:
    def __init__(self, name, health, attack, power, armor, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.power = power
        self.armor = armor
        self.defense = defense
        self.alive = True

    def lost_health(self, e_health):
        if self.health > 0:
            if e_health < 0:
                self.health += e_health
        else:
            self.alive = False

    def eattack(self):
        return (self.power)*(self.attack/2)

    def edefense(self):
        return (self.health+self.armor)*(self.defense/10)

