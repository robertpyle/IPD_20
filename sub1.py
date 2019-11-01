team_name = 'Sub 1'
strategy_name = 'Sub'
strategy_description = 'Outputs a set amount of colludes and betrays to act as a "handshake". Other players called "subs" will look for this to recognize the Headmaster and for the Headmaster to recognize the "subs". If the Headmaster recognizes the subs it will always betray and if the subs recognize the Headmaster they will always collude. Otherwise the subs will always betray to lower points and the Headmaster will play "tit for tat"'

def move(my_history, their_history, my_score, their_score):
  slave_code  = ['c', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
  master_code = ['c', 'c', 'b', 'b', 'b', 'b', 'c', 'b', 'c']

  if len(my_history) < len(slave_code):
    return slave_code[len(my_history)]
  if len(their_history) >= len(master_code):
    followsMasterCode = True
    for x in range(len(master_code)):
      if not their_history[x] == master_code[x]:
        followsMasterCode = False
    if followsMasterCode:
      return 'c'
    else:
      return 'b'