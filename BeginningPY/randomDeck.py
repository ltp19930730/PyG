# A python script to simulate a poke 
import random
from pprint import pprint

class poke(object):
    def __init__(self):
        values = range(1,11)+'Jack Queen King'.split()
        suits = 'diamonds clubs hearts spades'.split()
        self.deck = ['%s of %s' % (v,s) for v in values for s in suits]
    
    def get_deck(self):
        return self.deck

    def draw_card(self):
        return self.deck.pop()

    def left(self):
        return len(self.deck)
 
if __name__ == '__main__':
    pok = poke()
    while pok.get_deck:
        a= raw_input("Draw a card ? Y/N")
        if a == "y":
            print pok.draw_card()
            print "card left:"+str(pok.left())
        else:
            break
