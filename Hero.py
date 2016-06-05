import Item


class Hero:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.armor = 50
        self.power = 10
        self.eq = []
        self.alive = True
        self.mana = 10
        self.gold = 10000
        self.lhand_weapon = []
        self.rhand_weapon = []
        self.armory = []

    def lost_health(self, health):
        if self.health > 0:
            self.health -= health
        else:
            self.alive = False

    def hattack(self):
        return (self.power)*(self.attack/2)

    def hdefense(self):
        return (self.armor)*(self.defense/10)

    def add_weapon(self, hand, Item, Hero):
        if hand == "left":
            if not self.lhand_weapon:
                self.lhand_weapon.append(Item)
              #  self.remove_item(Item)
                Item.use(Hero)
            else:
                return False
        elif hand == "right":
            if not self.rhand_weapon:
                self.rhand_weapon.append(Item)
                self.remove_item(Item)
                Item.use(Hero)
            else:
                return False

    def add_armor(self, Item, Hero):
        if not self.armory:
            self.armory.append(Item)
          #  self.remove_item(Item)
            Item.use(Hero)
        else:
            return False

    def remove_weapon(self, hand, Item, Hero):
        if hand == "left":
            if self.lhand_weapon:
                self.lhand_weapon.remove(Item)
             #   self.add_item(Item)
                Item.remove(Hero)
            else:
                return False
        if hand == "right":
            if self.rhand_weapon:
                self.rhand_weapon.remove(Item)
                self.add_item(Item)
                Item.remove(Hero)
            else:
                return False

    def remove_armor(self, Item, Hero):
        if self.armory:
            self.armory.remove(Item)
        #    self.add_item(Item)
            Item.remove(Hero)

    def add_attack(self, attack):
        self.attack += attack

    def add_defense(self, defense):
        self.defense += defense

    def add_item(self, item):
        self.eq.append(item)

    def remove_item(self, item):
        self.eq.remove(item)

    def add_mana(self, mana):
        self.mana += mana

    def return_eq(self, i):
            return self.eq[i].name

    def return_full_eq(self, i):
            return self.eq[i]

    def print_eq(self):
        if not self.eq:
            print ("eq is empty")
        else:
            for x in self.eq:
                print (x.name)

    def print_eq2(self):
        if not self.lhand_weapon:
            print ("No weapon in right hand")
        else:
            for x in self.lhand_weapon:
                print (x.name)

    def print_armor(self):
        if not self.armory:
            print ("No armor")
        else:
            for x in self.armory:
                print (x.name)

    def check(self, other):
        return self.lhand_weapon[0].name == other.name
