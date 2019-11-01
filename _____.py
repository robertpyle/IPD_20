team_name = '_____'
strategy_name = 'Collude unless betrayed.'
strategy_description = '''\
Betray if ever betrayed.
If I haven't been betrayed yet, I'll collude.
'''

def move(my_history, their_history, my_score, their_score):
    if 'b' in their_history > 0: # If I am betrayed
        return 'b'               # Betray.
    else:
        return 'c'               # Collude