import Hero
import Item
import kivy
from ShopScr import ShopScr
from kivy.app import App
from EqScr import EqScr
from Arena import Arena
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
from kivy.uix.listview import ListView
from kivy.adapters.simplelistadapter import *
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.switch import Switch
from kivy.clock import Clock
#from GameScrean import Magni
Builder.load_file("gui.kv")
from Hero import GameScrean
import save
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)

    def change_scr(self):
        self.sm.current = 'gamescrean'
        print("niby dziala")

    def load_game(self):
        save.save.load_game(self)
        print("HALO HALO")
        print(Hero.Magni.gold)



class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='MainMenu'))
        sm.add_widget(GameScrean(name='gamescrean'))
        sm.add_widget(ShopScr(name='Shop'))
        sm.add_widget(EqScr(name='eq'))
        sm.add_widget(Arena(name='Arena'))
       # Clock.schedule_interval(self.update(), 1.0 / 60.0)
        return sm

    def change_scr(self):
        self.sm.current = 'gamescrean'
        print("niby dziala")


if __name__ == '__main__':
    MyApp().run()


'''

mydlo = Item.Item("mydlo")
print (Magni.attack)

#Magni.add_attack(mydlo.extra_attack)
Magni.attack+=10

miecz = Item.Weapon("miesz", 50)
miecz.use(Magni)

Magni.add_item(miecz)
print (Magni.attack)

Magni.add_weapon("right", miecz, Magni)
Magni.print_eq2()
print (Magni.attack)

Magni.print_eq()


zbroja = Item.Armor("Zbroja", 100)
Magni.add_item(zbroja)

Magni.add_armor(zbroja, Magni)

print(Magni.armor)

   list_view = ListView(item_strings=[str(index) for index in Magni.return_eq()])
        self.add_widget(list_view)

        simple_list_adapter = SimpleListAdapter(
        data=["Item #{0}".format(i) for i in Magni.return_eq()],
        cls=Label)

        list_view2 = ListView(adapter=simple_list_adapter)
        self.add_widget(list_view2)




 self.cols = 3

        #self.add_widget(Label(text='User Name'))
        self.lab = Label(text="Obrazenia: " + atc,
                            size_hint=(.3, 1.25),
                            pos=(300, 20))
        self.add_widget(self.lab)
        i=0
        for x in Magni.eq:
            self.itm = Label(text=x.name,
                             size_hint=(.3, .25),
                             pos=(300, 20+i))
            i=+50
            self.add_widget(self.itm)

        self.btn1 = Button(text="zaloz miecz",
                            size_hint=(.3, .25),
                            pos=(20, 400))
        self.add_widget(self.btn1)
        self.lab2 = Label(text= "Obrona: " + arm,
                            size_hint=(.3, 1),
                            pos=(300, 20))
        self.add_widget(self.lab2)
        self.btn2 = Button(text="zaloz zbroje",
                            size_hint=(.3, .25),
                            pos=(20, 200))
        self.add_widget(self.btn2)
        self.btn3 = Button(text="Zdejmic miecz",
                            size_hint=(.3, .25),
                            pos=(500, 400))
        self.add_widget(self.btn3)
        self.btn4 = Button(text="Zdejmic zbroje",
                            size_hint=(.3, .25),
                            pos=(500, 200))
        self.add_widget(self.btn4)
        self.btn1.bind(on_press=partial(self.callback, self.lab))
        self.btn2.bind(on_press=partial(self.callback2, self.lab2))
        self.btn3.bind(on_press=partial(self.callback3, self.lab))
        self.btn4.bind(on_press=partial(self.callback4))

        layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(30):
            btn = Button(text=str(i), size_hint_y=None, height=40)
            layout.add_widget(btn)
        root = ScrollView(size_hint=(None, None), size=(400, 400))
        root.add_widget(layout)


    def callback(label, instance, *args):

        Magni.add_weapon("right", miecz, Magni)
        label.lab.text="Obrazenia: " + str(Magni.attack)

    def callback2(label, instance, *args):
        Magni.add_armor(zbroja, Magni)
        label.lab2.text= "Obrona: " + str(Magni.armor)

    def callback3(label, instance, *args):
        Magni.remove_weapon("right", miecz, Magni)
        label.lab.text="Obrazenia: " + str(Magni.attack)

    def callback4(label, instance, *args):
        Magni.remove_armor(zbroja, Magni)
        label.lab2.text="Obrona: " + str(Magni.armor)



'''