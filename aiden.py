import random

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####




team_name = '2/3_Send'
strategy_name = 'Double Betray'
strategy_description = 'Betray twice then collude.'

    
def move(my_history, their_history, my_score, their_score):
  move_num=[1, 2, 3]
  x = random.choice(move_num)
   
  if x == 1 or x == 2:
    return 'b' 
  else:
    return 'c'

