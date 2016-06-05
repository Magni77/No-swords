import Hero
import Item
import kivy
import ShopScr

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

global Magni
Magni = Hero.Hero("Magni", 500, 50, 10)
miecz = Item.Weapon("K.W. Miecz", 50, 300)
zbroja = Item.Armor("Zbroja", 100, 300)
#Magni.add_item(miecz)
#Magni.add_item(zbroja)

class GameScrean(Screen):

    def __init__(self, **kwargs):
        super(GameScrean, self).__init__(**kwargs)

        self.rig = self.ids['right_box']
        self.lbl = self.ids['left_box']
        self.print_eq()
        self.print_stats()
        self.lbl.text = Magni.name
        Clock.schedule_interval(self.update, 1 / 1.0)

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
        print("niby dziala")

    def get_hero_eq(self):
        for x in range(len(Magni.eq)):
           self.h_eq = Magni.return_full_eq(x)

    def update(self, *args):
        GameScrean.print_eq(self)
        GameScrean.print_stats(self)

