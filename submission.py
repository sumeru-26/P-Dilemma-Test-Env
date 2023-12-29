from axelrod.action import Action
from axelrod.player import Player

C, D = Action.C, Action.D

class Submission(Player):
    name = 'Submission'

    def __init__(self):
        super().__init__()
        self.cur_state = 1

    def transition_state(self,action):
        transitions = (
            (1,C,1,C),
            (1,D,1,D),
        )
        if action == C:
            transition = transitions[self.cur_state*2-2]
        else:
            transition = transitions[self.cur_state*2-1]
        self.cur_state = transition[2]
        return transition[3]



    def strategy(self, opponent: Player) -> Action:
        
        #first move
        if not self.history: return C
        
        move = self.transition_state(opponent.history[-1])
        return move