import Hero


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    #def use(self):
     #   Hero.Hero.attack += self.extra_attack

    def check(self, other):
        return self.name == other.name


class Weapon(Item):
    def __init__(self, name, e_attack, price):
        super(Item, self).__init__()
        self.name = name
        self.extra_attack = e_attack
        self.price = price

    def use(self, Hero):
        Hero.attack += self.extra_attack
        #Hero.add_attack(self.extra_attack)

    def remove(self, Hero):
        Hero.attack -= self.extra_attack

    def get_inf(self):
        return self.extra_attack

class Armor(Item):
    def __init__(self, name, e_armor, price):
        super(Item, self).__init__()
        self.name = name
        self.extra_armor = e_armor
        self.price = price

    def use(self, Hero):
        Hero.armor+=self.extra_armor

    def remove(self, Hero):
        Hero.armor -= self.extra_armor

    def get_inf(self):
        return self.extra_armor
