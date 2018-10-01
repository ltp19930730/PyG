#! /usr/local/bin/python3
# Mini-project #6 - Blackjack

import simpleguitk as simplegui
import random


# load card sprite - 950x392 - source: jfitz.com
CARD_SIZE = (73, 98)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize global variables
deck = []
in_play = False
score = 0

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            print ("Invalid card: ", self.suit, self.rank)

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_SIZE[0] * (0.5 + RANKS.index(self.rank)), CARD_SIZE[1] * (0.5 + SUITS.index(self.suit)))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_SIZE[0] / 2, pos[1] + CARD_SIZE[1] / 2], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self, pos):
        self.cards = []
        self.pos = pos

    def __str__(self):
        res = 'Hands contains '
        for card in self.cards:
            res += str(card)
        return res

    def add_card(self, card):
        self.cards.append(card)

    # count aces as 1, if the hand has an ace, then add 10 to hand value if don't bust
    def get_value(self):
        value = 0
        num_ace = 0
        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]
            if rank == 'A':
                num_ace += 1
        
        for i in range(num_ace):
            if value + 10 <= 21:
                value += 10
        return value

    # if hand buster showed 
    def busted(self):
        pass
    
    def draw(self, canvas):
        x_bias = 0
        y_bias = 0
        for card in self.cards:
            card.draw(canvas, [x_bias + self.pos[0],y_bias + self.pos[1]])
            if x_bias + CARD_SIZE[0] >= 200:
                x_bias = 0
                y_bias += 100
            else:
                x_bias += 100


    def clean(self):
        self.cards = []
 
        
# define deck class
class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in SUITS for rank in RANKS]
        self.pos = 0

    # add cards back to deck and shuffle
    def shuffle(self):
        random.shuffle(self.deck)
        self.pos = 0

    def __str__(self):
        res = 'Deck contains '
        for card in self.deck:
            res += str(card) + ' '
        return res

    def deal_card(self):
        card = self.deck[self.pos]
        self.pos += 1
        return card


deck = Deck()
player = Hand([20,100])
dealer = Hand([340,100])

#define callbacks for buttons
def deal():
    global outcome, in_play, deck
    deck.shuffle()
    player.clean()
    dealer.clean()
    print(deck)
    
    # add two cards from deck to player
    for i in range(2):
        player.add_card(deck.deal_card())

    # add two cards from deck to dealer
    for i in range(2):
        dealer.add_card(deck.deal_card())

    print (player)
    print (dealer)

    # your code goes here
    
    outcome.set_text("IN GAME")
    in_play = True

def hit():
    global player, deck, score, in_play
    if in_play == False:
        return
    if player.get_value() <= 21:
        player.add_card(deck.deal_card())
    if player.get_value() > 21:
        player.busted()
        in_play = False
        outcome.set_text("You have busted!!")
        score -= 1
        score_l.set_text("Score : " + str(score))
        
   
    # if busted, assign an message to outcome, update in_play and score
       
def stand():
    global in_play, dealer, score
    if in_play == True:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        res_d = dealer.get_value()
        if res_d > 21 or player.get_value() > res_d:
            outcome.set_text("You win !!")
            score += 1
        else:
            outcome.set_text("You lost !!")
            score -= 1
        score_l.set_text("Score : " + str(score))
        in_play = False

   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

def draw(canvas):
    ##card = Card("S", "A")
    ##card.draw(canvas, [300, 300])
    global player, dealer
    player.draw(canvas)
    dealer.draw(canvas)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)
score_l = frame.add_label("Score : 0")
outcome = frame.add_label("IN GAME")

# deal an initial hand

# get things rolling
frame.start()


# Grading rubric - 18 pts total (scaled to 100)

# 1 pt - The program opens a frame with the title "Blackjack" appearing on the canvas.
# 3 pts - The program displays 3 buttons ("Deal", "Hit" and "Stand") in the control area. (1 pt per button)
# 2 pts - The program graphically displays the player's hand using card sprites. 
#		(1 pt if text is displayed in the console instead) 
# 2 pts - The program graphically displays the dealer's hand using card sprites. 
#		Displaying both of the dealer's cards face up is allowable when evaluating this bullet. 
#		(1 pt if text displayed in the console instead)
# 1 pt - Hitting the "Deal" button deals out new hands to the player and dealer.
# 1 pt - Hitting the "Hit" button deals another card to the player. 
# 1 pt - Hitting the "Stand" button deals cards to the dealer as necessary.
# 1 pt - The program correctly recognizes the player busting. 
# 1 pt - The program correctly recognizes the dealer busting. 
# 1 pt - The program correctly computes hand values and declares a winner. 
#		Evalute based on player/dealer winner messages. 
# 1 pt - The dealer's hole card is hidden until the hand is over when it is then displayed.
# 2 pts - The program accurately prompts the player for an action with the messages 
#        "Hit or stand?" and "New deal?". (1 pt per message)
# 1 pt - The program keeps score correctly.
