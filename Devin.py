####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Devin'
strategy_name = 'Headmaster'
strategy_description = 'Outputs a set amount of colludes and betrays to act as a "handshake". Other players called "subs" will look for this to recognize the Headmaster and for the Headmaster to recognize the "subs". If the Headmaster recognizes the subs it will always betray and if the subs recognize the Headmaster they will always collude. Otherwise the subs will always betray to lower points and the Headmaster will play "tit for tat"'

def move(my_history, their_history, my_score, their_score):
  slave_code  = ['c', 'b', 'b', 'b', 'b', 'c']
  master_code = ['c', 'c', 'b', 'b', 'b', 'b', 'c', 'b', 'c']
  slaveIdentifier  = ['c', 'c', 'b', 'b', 'c', 'c']
  masterIdentifier = ['c', 'c', 'c', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'c']
  if len(their_history) >= len(slave_code):
    followsSlaveCode = True
    for x in range(len(slave_code)):
      if not their_history[x] == slave_code[x]:
        followsSlaveCode = False
    if followsSlaveCode and len(my_history) < len(master_code):
      return master_code[len(my_history)]
    elif followsSlaveCode:
      return 'b'
    else:
      return their_history[-1]
  if len(their_history) >= len(slaveIdentifier):
    followsJustinCode = True
    for x in range(len(slaveIdentifier)):
      if not their_history[x] == slaveIdentifier[x]:
        followsJustinCode = False
      if followsJustinCode and len(my_history) < len(masterIdentifier):
        return masterIdentifier[len(my_history)]
      elif followsJustinCode:
        return 'b'
      else:
        return their_history[-1]
  if len(their_history) >= 1:
    return their_history[-1]
  else:
    return 'c'