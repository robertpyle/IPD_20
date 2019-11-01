####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Justin Taing'
strategy_name = 'Stop Snitching'
strategy_description = 'Start out with a betray, then switch to colluding twice to test out if the strategy '

def move(my_history, their_history, my_score, their_score):
    if len(my_history) <= 1:
        return 'c'
    if 'b' in their_history:
        return 'b'
    return 'c'