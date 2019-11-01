team_name = 'Justin Lee'
strategy_name = 'spiteful_cc/slavemaster'
strategy_description = 'Plays spiteful_cc strategy until it identifies a slave, then switches to slavemaster strategy. Identifies its own slaves and also tricks opposing players slaves into feeding self.'

justinSlaveIdentifier  = ['c', 'c', 'b', 'c', 'b', 'c']
devinSlaveIdentifier   = ['c', 'b', 'b', 'b', 'b', 'c']

justinMasterIdentifier = ['c', 'c', 'c', 'b', 'b', 'b', 'c', 'c', 'b']
devinMasterIdentifier  = ['c', 'c', 'b', 'b', 'b', 'b', 'c', 'b', 'c']

def checkSlave(their_history, slaveIdentifier):
    if len(their_history) < len(slaveIdentifier):
        return False
    for x in range(len(slaveIdentifier)):
        if not their_history[x] == slaveIdentifier[x]:
            return False
    return True

def followIdentifier(my_history, identifier):
    if len(my_history) < len(identifier):
        return identifier[len(my_history)]
    return False

def spiteful_cc(their_history):
    if len(their_history) <= 1:
        return 'c'
    if 'b' in their_history:
        return 'b'
    return 'c'

def move(my_history, their_history, my_score, their_score):
    if checkSlave(their_history, justinSlaveIdentifier):
        if not followIdentifier(my_history, justinMasterIdentifier):
            return 'b'
        return followIdentifier(my_history, justinMasterIdentifier)
    if checkSlave(their_history, devinSlaveIdentifier):
        if not followIdentifier(my_history, devinMasterIdentifier):
            return 'b'
        return followIdentifier(my_history, devinMasterIdentifier)
    return spiteful_cc(their_history)