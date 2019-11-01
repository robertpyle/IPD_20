team_name = 'Maggie'
strategy_name = 'strat'
strategy_description = 'return \'\', \' \', or int 4'

import random

def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history[-5:]:
     return 'b'
    else:
        if random.random()<0.30:
            return 'b'
        else:
            return 'c'
