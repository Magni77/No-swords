import Item
import Hero
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from functools import partial


class ShopScr(Screen):
    def __init__(self, **kwargs):
        super(ShopScr, self).__init__(**kwargs)
        self.hero_eq = self.ids['myeq']
        self.shop_eq = self.ids['shopeq']
        self.test = self.ids['label1']
        self.stock = []
        self.start()
        self.print_eq()
        self.print_shop_stock()
        self.test.text = str(Hero.Magni.gold)

    def start(self):
        KWSword = Item.Weapon("K.W. Sword", 40, 200)
        self.stock.append(KWSword)
        Sword2 = Item.Weapon("Bilgewater Cutlass", 50, 400)
        self.stock.append(Sword2)
        Sword3 = Item.Weapon("Infinity Edge", 80, 500)
        self.stock.append(Sword3)
        Sword4 = Item.Weapon("Hexdrinker", 100, 700)
        self.stock.append(Sword4)
        Hammer = Item.Weapon("Warhammer", 100, 600)
        self.stock.append(Hammer)
        Hammer2 = Item.Weapon("Frozem Mallet", 110, 700)
        self.stock.append(Hammer2)
        armor1 = Item.Armor("Chain Vest", 40, 100)
        self.stock.append(armor1)
        armor2 = Item.Armor("Randuin's Omen", 80, 300)
        self.stock.append(armor2)
        Hero.Magni.print_eq()

    def get_item(self, x):
            return self.stock[x]

    def get_hero_eq(self):
        for x in range(1):
           self.h_eq = Hero.Magni.return_full_eq(x,x)

    def print_eq(self):
        try:
            self.hero_eq.clear_widgets()
            self.hero_eq.add_widget(Button(text = "Equipment", height='200sp', font_size = '15sp', markup=False))

            for x in range(len(Hero.Magni.eq)):
                self.hero_eq.add_widget(Button(text = str(Hero.Magni.return_eq(x)), height='200sp', font_size = '15sp'))
        except:
            pass
        self.hero_eq.height = len(Hero.Magni.eq)*70

    def print_shop_stock(self):
        try:
            self.shop_eq.clear_widgets()
            self.shop_eq.add_widget(Button(text="Shop", height='200sp', font_size='15sp', markup=False))
            inf =""
            for x in range(len(self.stock)):
                if type(self.stock[x]) is Item.Weapon:
                    inf = " Attack"
                elif type(self.stock[x]) is Item.Armor:
                    inf = " Armor"
                butt = Button(text=str(self.stock[x].name) + ' ' + str(self.stock[x].price) + 'g \n    +'
                                     +str(self.stock[x].get_inf()) + inf, height='200sp', font_size='15sp')
                itm = self.get_item(x)
                butt.bind(on_press=partial(self.buy_item, itm))
                self.shop_eq.add_widget(butt)

            Hero.Magni.print_eq()
            print(self.shop_eq[0])
        except:
             print("print sjop stock error")
        self.shop_eq.height = len(self.stock)*50

    def buy_item(self, Item, *args):
        if(Item.price <= Hero.Magni.gold):
          #  popup = Popup(title='Are You sure', content= Button(text='BUY!'))
           # popup.open()
            Hero.Magni.eq.append(Item)

            self.stock.remove(Item)
            Hero.Magni.gold -= Item.price
            self.test.text = '[color=00ff00]' + '[size=50]' + str(Hero.Magni.gold) + '[/color]' + '[/size]'
            self.print_eq()
            self.print_shop_stock()
        else:
            self.test.text =  '[color=ff0000]' + '[size=50]' + str(Hero.Magni.gold) + '[/color]' + '[/size]'

