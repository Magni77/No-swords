import Hero
import Enemy
from random import Random
import random
import GameScrean
from kivy.uix.screenmanager import Screen
import math

class Arena(Screen):
    def __init__(self, **kwargs):
        super(Arena, self).__init__(**kwargs)
        self.t = []
        Enemy1 = Enemy.Enemy("Boss", 500, 40, 10, 50, 7)

        self.start_battle(GameScrean.Magni, Enemy1)

    def fight(self, Hero, Enemy, who):
        hero_attack = Hero.hattack()
        print("HA", hero_attack)
        hero_defense = Hero.hdefense()
        print("HD",  hero_defense)
        enemy_attack = Enemy.eattack()
        print("EA" , enemy_attack)
        enemy_defense = Enemy.edefense()
        print("ed   ", enemy_defense)
        if who % 2 == 0:
            Hero.lost_health(abs(enemy_defense - hero_attack))
        else:
            Enemy.lost_health(abs(hero_defense - enemy_attack))

    def start_battle(self, Hero, Enemy):
        who_f = random.randint(0,1)
        while(Hero.health > 0 and Enemy.health > 0):
            print(who_f)
            self.fight(Hero, Enemy, who_f)
            who_f += 1
            print(Hero.health)
            print(Enemy.health)

        print(Hero.health)
        print(Enemy.health)