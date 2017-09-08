def test_a_deck(deck):
    forward_deck = [i for i in range(13)]
    backward_deck = [12-i for i in range(13)]
    forward_score = sum([ deck[i]>forward_deck[i] for i in range(len(deck))])
    backward_score = sum([ deck[i]>backward_deck[i] for i in range(len(deck))])
    return min([forward_score, backward_score])

def compare_decks(deck1,deck2):
    score = sum([ deck1[i]>deck2[i] for i in range(len(deck1))])+sum([ deck1[i]==deck2[i] for i in range(len(deck1))])/2.
    return score > 6

successful_decks = []
for i in range(10000):
    random_deck = random.sample([i for i in range(13)],13)
    if test_a_deck(random_deck) > 6:
        successful_decks = successful_decks + [random_deck]
        
win_percent = []
for i in successful_decks:
    num_tries = 0
    num_wins = 0
    for j in successful_decks:
        num_tries = num_tries + 1
        if compare_decks(i,j):
            num_wins = num_wins+1
    win_percent = win_percent + [num_wins/num_tries]
    
blah = [successful_decks[i] for i in range(len(successful_decks)) if win_percent[i] == max(win_percent)]
blah = blah[0]
print(blah)
