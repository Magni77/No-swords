
import GameScrean
import Item
from kivy.uix.button import Button
import save
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from Arena import Arena


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
        self.gold = 1000
        self.lhand_weapon = []
        self.rhand_weapon = []
        self.armory = []

    def lost_health(self, health):
        if self.health > 0:
            if health < 0:
                self.health += health
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

global Magni
Magni = Hero("Magni", 1000, 50, 10)
miecz = Item.Weapon("K.W. Miecz", 50, 300)
zbroja = Item.Armor("Zbroja", 100, 300)


class GameScrean(Screen):

    def __init__(self, **kwargs):
        super(GameScrean, self).__init__(**kwargs)

        self.rig = self.ids['right_box']
        self.lbl = self.ids['left_box']
        self.print_eq()
        self.print_stats()
        self.lbl.text = Magni.name
        Clock.schedule_interval(self.update, 1 / 1.0)

    def save_game(self):
        #Magni.save_game()
        save.save.save_game(self, Magni)

    def print_eq(self):
        try:
            self.rig.clear_widgets()
            self.rig.add_widget(Button(text = "Equipment", height='200sp', font_size = '15sp', markup=False))

            for x in range(len(Magni.eq)):
                self.rig.add_widget(Button( text = str(Magni.return_eq(x)), height='200sp', font_size = '15sp'))

        except:
            pass
       #self.rig.size = (100,100)
        self.rig.height = len(Magni.eq)*75

    def print_stats(self):
        self.lbl.clear_widgets()
        stats_list = [' ','Health', 'Attack', 'Defense', 'Armor', 'Mana', 'Gold']
        stats_list2 = [Magni.name, Magni.health, Magni.attack, Magni.defense, Magni.armor, Magni.mana, Magni.gold]
        for x in range(7):
            self.lbl.add_widget(Button(text = str(stats_list[x])+ ": " +str(stats_list2[x]), height='200sp',
                                       font_size = '15sp'))
        self.lbl.height = 7*50

    def change_scr(self):
        self.sm.current = 'MainMenu'

    def get_hero_eq(self):
        for x in range(len(Magni.eq)):
           self.h_eq = Magni.return_full_eq(x)

    def update(self, *args):
        GameScrean.print_eq(self)
        GameScrean.print_stats(self)

    def sleep(self):
        Magni.health = 1000
        Arena.sleep(Arena)


