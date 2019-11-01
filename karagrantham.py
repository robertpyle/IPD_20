####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'KaraGrantham'
strategy_name = 'Collude with predictions'
strategy_description = '''\Collude first round. Collude and check their values to try and predict their strategy and form a new strategy based off their moves.'''

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.

    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty.
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]

    Returns 'c' or 'b' for collude or betray.
    '''
    actionOpp = len(their_history)
    countC = their_history.count('c')
    countB = their_history.count('b')
    if actionOpp < 10:
        return 'c'
    else:
        if 'b' not in their_history:
            return 'c'
        elif 'c' not in their_history:
            return 'b'
        else:
            if countB > 0.5 * actionOpp:
                if my_history[-1] == 0:
                    return 'c'
                else:
                    return 'b'
            elif countC > 0.5 * actionOpp:
                return 'b'
            else:
               return 'c'
