####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Mirna'
strategy_name = 'Collude but retaliate okay'
strategy_description = '''\
Collude first round. Betray second round. If player returns the same for the first two rounds, betray if they betrayed and collude if they colluded for those two rounds. Else, always betray.'''

def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.

    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty.
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]

    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0:
      return 'c'
    elif len(my_history)==1:
      return 'b'
    elif their_history[-1]==their_history[-2]:
      if my_history[-1]=='c' and their_history[-1]=='b':
        return 'b'
      else:
        return 'c'
    else:
      return 'b'