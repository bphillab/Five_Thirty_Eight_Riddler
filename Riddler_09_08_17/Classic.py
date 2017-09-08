import random

class deck:
    cards_in_deck = []
    cards_in_discard = []
    lose_flag = 0
    def __init__(self,cards):
        self.cards_in_deck = cards
    
    def draw_a_card(self):
        if len(self.cards_in_deck) == 0:
            if len(self.cards_in_discard) == 0:
                self.lose_flag = 1
                return -1
            self.shuffle_in_discard()
        card_drawn = self.cards_in_deck[0]
        self.cards_in_deck = self.cards_in_deck[1:]
        return card_drawn
    
    def shuffle_in_discard(self):
        self.cards_in_deck = self.cards_in_deck + random.sample(self.cards_in_discard,len(self.cards_in_discard))
        self.cards_in_discard=[]
        return True
    
    def receive_cards(self,cards):
        self.cards_in_discard = self.cards_in_discard+cards
    
    def lose_check(self):
        if len(self.cards_in_deck) == 0:
            if len(self.cards_in_discard) == 0:
                self.lose_flag = 1
        if self.lose_flag == 1:
            return True
        return False
    
    
class game:
    
    winner = -1
    
    def __init__(self,p1_c,p2_c):
        self.player_1 = deck(p1_c)
        self.player_2 = deck(p2_c)
    
    def round(self):
        p1 = self.player_1.draw_a_card()
        p2 = self.player_2.draw_a_card()
        if p1 > p2:
            self.player_1.receive_cards([p1,p2])
        if p1 < p2:
            self.player_2.receive_cards([p1,p2])
        if p1 == p2:
            self.war([p1,p2])
        if self.player_1.lose_check():
            self.winner = 2
        if self.player_2.lose_check():
            self.winner = 1
    
    def war(self,cards):
        tableau = cards + [self.player_1.draw_a_card()] + [self.player_2.draw_a_card()]
        p1 = self.player_1.draw_a_card()
        p2 = self.player_2.draw_a_card()
        if p1 > p2:
            self.player_1.receive_cards(tableau+[p1,p2])
        if p1 < p2:
            self.player_2.receive_cards(tableau+[p1,p2])
        if p1 == p2:
            self.war([p1,p2])
        if self.player_1.lose_check():
            self.winner = 2
        if self.player_2.lose_check():
            self.winner = 1

    def game_not_over_check(self):
        if self.winner == -1:
            return True
        else: 
            return False
            
            
def play_a_game():
    cards = random.sample([i for i in range(12)]*4,13*2)
    p1_c = cards
    p2_c = [12,12,12,12]
    new_game = game(p1_c,p2_c)
    while new_game.game_not_over_check():
        new_game.round()
    return new_game.winner
    

num_games = 40000
winners = []
for i in range(num_games):
    winners = winners + [play_a_game()]

print(len([i for i in winners if i ==1])/(len([i for i in winners if i ==2])+len([i for i in winners if i ==1])))
