import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Brien'
strategy_name = 'collude first turn then roulette'
strategy_description = 'Always collude on first turn then 50/50 chance to collude or betray.'

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.

    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty.
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]

    Returns 'c' or 'b' for collude or betray.
    '''

    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    else:
        if random.random()<0.50: # 50% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'
