import Hero
import Enemy
import random
from kivy.uix.screenmanager import Screen

Enemy1 = Enemy.Enemy("Boss", 1000, 40, 10, 50, 7)

class Arena(Screen):
    def __init__(self, **kwargs):
        super(Arena, self).__init__(**kwargs)
        self.label = self.ids['label']
        self.label2 = self.ids['label2']
        self.label3 = self.ids['label3']
        self.t = []

        self.enemy_tab = []
       # self.start_battle(Hero.Magni, Enemy1)
        self.label.text = '[size=30]' + "Your Health: " + str(Hero.Magni.health)\
                          + '\n' + "Enemy health: "  + str(Enemy1.health)
        self.who_f = random.randint(0,1)

    def choose_attack(self, atc):
        if atc == "normal":
            self.e_atc = 1
            self.e_def = 1
        elif atc == "strong":
            self.e_atc = 1.5
            self.e_def = 0.9
        elif atc == "light":
            self.e_atc = 0.8
            self.e_def = 1.1
        elif atc == "defend":
            self.e_atc = 0
            self.e_def = 1.5

    def fight(self, Hero, Enemy, who, a_power, d_power):
        hero_attack = Hero.hattack() *a_power
        print("Herro Attac", hero_attack)
        hero_defense = Hero.hdefense() * d_power
        print("Her Def",  hero_defense)
        enemy_attack = Enemy.eattack() * a_power
        print("Enem Atta" , enemy_attack)
        enemy_defense = Enemy.edefense() * d_power
        print("enemy defd", enemy_defense)
        crit = random.randint(0, 5)

        if crit == 4:
            x = 1.5
            print("CRIT")
        else:
            x = 1

        if who % 2 != 0:
            hp = enemy_defense - x*hero_attack
            Enemy.lost_health(hp)
            self.label2.text = '[size=25]' + "Hero hit for " + str(abs(hp))
        else:
            ep = hero_defense - x*enemy_attack
            Hero.lost_health(ep)
            self.label3.text = '[size=25]' + "Enemy hit for " + str(abs(ep))

    def battle(self):
        if(Hero.Magni.health > 0 and Enemy1.health > 0):
            print(self.who_f)
            self.fight(Hero.Magni, Enemy1, self.who_f, self.e_atc, self.e_def)
            self.who_f += 1
            self.fight(Hero.Magni, Enemy1, self.who_f, self.e_atc, self.e_def)
            self.update()
        if Enemy1.health < 0:
            Hero.Magni.gold += 500
            self.label.text = '[size=50]' + "HERO WIN"
        elif Hero.Magni.health < 0:
            self.label.text = '[size=50]' + "ENEMY WIN"

    def update(self, *args):
        self.label.text = '[size=30]' + "Your Health: " + str(Hero.Magni.health)\
                          + '\n' + "Enemy health: "  + str(Enemy1.health)

    def sleep(self, *args):
        Enemy1.health = 1000



