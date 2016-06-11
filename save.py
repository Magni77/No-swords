import Hero
import  pickle

class save:
    def save_game(self, Hero):
        with open('save.pkl', 'wb') as output:
            pickle.dump(Hero, output)

    def load_game(self):
        with open('save.pkl', 'rb') as input_f:
            Hero.Magni = pickle.load(input_f)