#http://www.codeskulptor.org/#user26_iTYAIqe00eD3xZL.py
# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

global outcome, in_play, new_deck, hand_dealer, hand_player, score
# initialize some useful global variables
in_play = False
outcome = "Hit or stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        
        
    def __str__(self):
        cards_info = ' '
        for card in self.cards:
            cards_info  = cards_info + str(card) + ' '
        return 'Hand contains '+ cards_info
            # return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)	# add a card object to a hand

    def get_value(self):
        hand_value = 0 
        #print len(self.cards)
        for i in range(len(self.cards)):
            hand_value = hand_value + int(VALUES[self.cards[i].rank])
        
        for i in range(len(self.cards)):
            if int(VALUES[self.cards[i].rank]) == 1 and hand_value <= 11:
                hand_value = hand_value + 10
        #print 'Hand_value: ' + str(hand_value)        
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        return hand_value	# compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, [pos[0]+100*i,pos[1]])
            # draw a hand on the canvas, use the draw method for cards
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for i in SUITS:
            for j in RANKS:
                self.deck.append(Card(i,j))# create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        self.deck.pop()
        return self.deck[-1]
    
    def __str__(self):
        deck_info = ' '
        for card in self.deck:
            deck_info  = deck_info + str(card) + ' '
        return 'Deck contains '+ deck_info



#define event handlers for buttons
def deal():
    global outcome, in_play, score, new_deck, hand_dealer, hand_player
    if in_play:
        outcome = 'You Forfeit! New Deal?'
        in_play = False
        score = score - 1
        print 'Dealer Hand Value: ' + str(hand_dealer.get_value())
        print 'Player Hand Value: ' + str(hand_player.get_value())
        print outcome
        print
    else:
        in_play = True
        new_deck = Deck()
        new_deck.shuffle()
        hand_dealer = Hand()
        hand_dealer.add_card(new_deck.deal_card())
        hand_dealer.add_card(new_deck.deal_card())
        hand_player = Hand()
        hand_player.add_card(new_deck.deal_card())
        hand_player.add_card(new_deck.deal_card())
        print 'Dealer ' + str(hand_dealer)
        print 'Player ' + str(hand_player)
        outcome = 'Hit or Stand?'

def hit():
    global outcome, in_play, score, new_deck, hand_dealer, hand_player# replace with your code below
    if in_play:
        if hand_player.get_value() <= 21:
            hand_player.add_card(new_deck.deal_card())
            print 'Player ' + str(hand_player)
            if hand_player.get_value() > 21:
                in_play = False
                outcome = "You Have Busted!"
                outcome = outcome + ' New Deal?'
                print 'Dealer Hand Value: ' + str(hand_dealer.get_value())
                print 'Player Hand Value: ' + str(hand_player.get_value())
                print outcome
                print
                
                score = score - 1
    else:
        pass 
    # if the hand is in play, hit the player   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome, in_play, score, new_deck, hand_dealer, hand_player	# replace with your code below
    if in_play:
        in_play = False
        #if outcome == "You Have Busted!":
        #    print outcome
        #else:
        while (hand_dealer.get_value() < 17):
            hand_dealer.add_card(new_deck.deal_card())
        if hand_dealer.get_value() > 21:
            outcome = "Dealer Busted!"
            score = score + 1
        elif hand_dealer.get_value()<=21 and hand_dealer.get_value() >= hand_player.get_value():
            outcome = "Dealer Won!"
            score = score - 1
        elif hand_dealer.get_value()<=21 and hand_dealer.get_value() <  hand_player.get_value():
            outcome = "You Won!"
            score = score + 1
        print 'Dealer ' + str(hand_dealer)
        print 'Dealer Hand Value: ' + str(hand_dealer.get_value())
        print 'Player Hand Value: ' + str(hand_player.get_value())
        outcome = outcome + ' New Deal?'
        print outcome
        print
    else:
        pass
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Score: ' + str(score), (400, 50), 30, 'Black')
    canvas.draw_text('Blackjack', (100, 50), 30, 'Black')
    canvas.draw_text('Dealer', (100, 80), 20, 'Black')
    canvas.draw_text('Player', (100, 370), 20, 'Black')
    canvas.draw_text(outcome, (100, 300), 30, 'Black')
    
    hand_dealer.draw(canvas, [100, 100])
    hand_player.draw(canvas,[100, 400])
    if in_play:
        canvas.draw_image(card_back, (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1]), CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
