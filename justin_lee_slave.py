team_name = 'Justin Lee'
strategy_name = 'j_slave'
strategy_description = 'Identifies slavemaster and feeds them.'

justinSlaveIdentifier  = ['c', 'c', 'b', 'c', 'b', 'c', 'c', 'c', 'c']
justinMasterIdentifier = ['c', 'c', 'c', 'b', 'b', 'b', 'c', 'c', 'b']

def checkMaster(their_history, masterIdentifier):
    if len(their_history) < len(masterIdentifier):
        return False
    for x in range(len(masterIdentifier)):
        if not their_history[x] == masterIdentifier[x]:
            return False
    return True

def followIdentifier(my_history, identifier):
    if len(my_history) < len(identifier):
        return identifier[len(my_history)]
    return False

def move(my_history, their_history, my_score, their_score):
    if not followIdentifier(my_history, justinSlaveIdentifier):
        if checkMaster(their_history, justinMasterIdentifier):
            return 'c'
        else:
            return 'b'
    return followIdentifier(my_history, justinSlaveIdentifier)