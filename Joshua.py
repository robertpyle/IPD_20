team_name = 'Joshua'
strategy_name = 'Collude 2% unless betrayed within last 2 rounds.'
strategy_description = '''\
Betray if ever betrayed.
If I have not been betrayed yet, I'll betray starting with the 15th round.
'''

import random

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.

    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty.
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]

    Returns 'c' or 'b' for collude or betray.
    '''
    #return random.choice(['', ' ', 4])

    while 'b' in their_history[-2:]: # while the other player has betrayed within last 2 rounds,
        return 'b'               # Betray.
    else:
        if random.random()<0.02: # 2% of the other rounds
            return 'c'         # Betray
        else:
            if 'b' in their_history:
              return 'b'
            else:
               return 'c'


