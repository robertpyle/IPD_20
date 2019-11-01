####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'ethan'
strategy_name = 'Stay Ahead'
strategy_description = 'Always betray unless ahead'

def move(my_history, their_history, my_score, their_score):
  my_b = 0
  their_b = 0
  for my_move in my_history:
    if my_move == 'b':
      my_b += 1
  for their_move in their_history:
    if their_move == 'b':
      their_b += 1
  if my_b < their_b:
    if my_score < their_score:
      return 'b'
    else:
      return 'c'
