import Hero
import Item
import kivy
from ShopScr import ShopScr
from kivy.app import App
from EqScr import EqScr
from Arena import Arena
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
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
        return sm

    def change_scr(self):
        self.sm.current = 'gamescrean'
        print("niby dziala")


if __name__ == '__main__':
    MyApp().run()
