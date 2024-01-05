from axelrod.action import Action
from axelrod.player import Player
import axelrod as axl

C, D = Action.C, Action.D


while True:
    state = input()
    episode_len,our_history,their_history = state.split(';')
    if episode_len == '0':
        print('C')
        continue
    cur_state = 3
    for action in their_history:
         cur_state,move = transition_state(cur_state,action)
    print(move)
    
def transition_state(cur_state,action):
    transitions = ((0, 'C', 7, 'C'), (0, 'D', 1, 'D'), (1, 'C', 2, 'D'), (1, 'D', 1, 'D'), (2, 'C', 2, 'C'), (2, 'D', 7, 'C'), (3, 'C', 3, 'C'), (3, 'D', 7, 'D'), (4, 'C', 4, 'D'), (4, 'D', 6, 'C'), (5, 'C', 7, 'D'), (5, 'D', 2, 'C'), (6, 'C', 6, 'D'), (6, 'D', 5, 'C'), (7, 'C', 6, 'D'), (7, 'D', 7, 'D'))
    if action == 'C':
            transition = transitions[cur_state*2]
    else:
        transition = transitions[cur_state*2+1]
    cur_state = transition[2]
    return transition[2],transition[3]

class Final(Player):
    name = 'Final'
    
    def strategy(self, opponent: Player) -> Action:    
        #first move
        if not self.history: return C
        their_history = opponent.history

        cur_state = 3
        for action in their_history:
            cur_state,move = transition_state(cur_state,action)
        if move == 'C': return C
        else: return D
    def transition_state(self,cur_state,action):
        transitions = ((0, 'C', 7, 'C'), (0, 'D', 1, 'D'), (1, 'C', 2, 'D'), (1, 'D', 1, 'D'), (2, 'C', 2, 'C'), (2, 'D', 7, 'C'), (3, 'C', 3, 'C'), (3, 'D', 7, 'D'), (4, 'C', 4, 'D'), (4, 'D', 6, 'C'), (5, 'C', 7, 'D'), (5, 'D', 2, 'C'), (6, 'C', 6, 'D'), (6, 'D', 5, 'C'), (7, 'C', 6, 'D'), (7, 'D', 7, 'D'))
        if action == 'C':
            transition = transitions[cur_state*2]
        else:
            transition = transitions[cur_state*2+1]
        cur_state = transition[2]
        return transition[2],transition[3]


          
