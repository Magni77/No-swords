from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from Hero import Hero
import GameScrean
import Item
from kivy.clock import Clock
import Hero


class EqScr(Screen):
    def __init__(self, **kwargs):
        super(EqScr, self).__init__(**kwargs)
        self.head = self.ids['head']
        self.armor = self.ids['armor']
        self.eq = []
        self.eq_n = []
        self.eq_weapon = []
        self.eq_armor = []
        self.eq_armor_n = []
        self.get_hero_eq()
        self.print_armor()
        self.print_lhand()

        Clock.schedule_interval(self.update, 1 / 1.0)

    def get_hero_eq(self):
        if len(Hero.Magni.eq) != len(self.eq):
            self.eq.clear()
            self.eq_n.clear()
            for x in range(len(Hero.Magni.eq)):
                self.eq.append(Hero.Magni.return_full_eq(x))
            for x in range(len(self.eq)):
                if type(self.eq[x]) is Item.Weapon:
                    self.eq_n.append(str(self.eq[x].name))
                    self.eq_weapon.append(Hero.Magni.return_full_eq(x))
                elif type(self.eq[x]) is Item.Armor:
                    self.eq_armor_n.append(str(self.eq[x].name))
                    self.eq_armor.append(Hero.Magni.return_full_eq(x))

    def print_lhand(self):
        self.head.clear_widgets()
        self.spinner = Spinner(
            text='Left Hand',
            values=map(str, self.eq_n),
            size_hint=(None, None),
            size=(150, 44),
            pos_hint={'center_x': .5, 'center_y': .5})

        def show_selected_value(spinner, text):
            print('The spinner', self.spinner, 'have text', text)
            print(self.eq_n.index(text))
            index = self.eq_n.index(text)
         #

            if self.all_same(self.eq_weapon, Hero.Magni.lhand_weapon ):
                Hero.Magni.remove_weapon("left", self.old_weapon, Hero.Magni)
            Hero.Magni.add_weapon("left", self.eq_weapon[index], Hero.Magni)
            self.old_weapon = self.eq_weapon[index]
            Hero.Magni.print_eq2()

        self.spinner.bind(text=show_selected_value)
        self.head.add_widget(self.spinner)

    def print_armor(self):
        self.armor.clear_widgets()
        self.a_spinner = Spinner(
            text='Armor',
            values=map(str, self.eq_armor_n),
            size_hint=(None, None),
            size=(150, 44),
            pos_hint={'center_x': .5, 'center_y': .5})

        def show_selected_value(spinner, text):
            print('The spinner', self.spinner, 'have text', text)
            print(self.eq_armor_n.index(text))
            index = self.eq_armor_n.index(text)

            if self.all_same(self.eq_armor, Hero.Magni.armory):
                Hero.Magni.remove_armor(self.old_arm, Hero.Magni)
            Hero.Magni.add_armor(self.eq_armor[index], Hero.Magni)
            self.old_arm = self.eq_armor[index]
            Hero.Magni.print_armor()

        self.a_spinner.bind(text=show_selected_value)
        self.armor.add_widget(self.a_spinner)

    def all_same(self, itm1, itm2):
       # return all(items2[0] == items[0])
        for i in set(itm1) & set(itm2):
            return True


    def update(self, *args):
        if len(Hero.Magni.eq) != len(self.eq):
            self.get_hero_eq()
            self.print_lhand()
            self.print_armor()



