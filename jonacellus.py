####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'jonacellus'
strategy_name = 'betray after a certain amount of confessions'
strategy_description = 'whenever the person concludes more than two times it will betray. Also when betrayed more than once it will start betraying from that point on'


import random



def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.

    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty.
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]

    Returns 'c' or 'b' for collude or betray.
    '''



    # This player will betray after a number of times of concluded
    if len(my_history)==0: # It's the first round:collude
        return 'c'

    if 'b' in their_history[-5:]: # If the other player has betrayed within last 5 rounds
      return 'b'               # Betray.
    else:
      if random.random()<0.01:
        return 'b' # 1% of the other round
      else:
        return 'c'         # but 85% of the time collude
    if len(my_history)==0: # It's the first round: collude
        return 'c'
    else:
        # If there was a previous round just like the last one,
        # do whatever they did in the round that followed it

        # Reference last round
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]

        # Look at rounds before that one
        for round in range(len(my_history)-1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            # If one matches
            if (prior_round_me == recent_round_me) and \
                    (prior_round_them == recent_round_them):
                return their_history[round]
        # No match found
        if my_history[-1]=='c' and their_history[-1]=='b':
            return 'b' # Betray if they were severely punished last time
        else:
            return 'c' # Otherwise collude.

    # This player will betray after a number of times of concluded and when betrayed the player will betray from that point on
        if my_history[-1] == 'b' and their_history[-1] == 'b':
            return b  #when the player betrays it will betray from that point one

