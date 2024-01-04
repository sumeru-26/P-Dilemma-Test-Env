from axelrod.action import Action
from axelrod.player import Player
import axelrod as axl
import numpy as np
import joblib
import random


C, D = Action.C, Action.D

class Submission(Player):
    name = 'Submission'

    def __init__(self):
        super().__init__()
        self.cur_state = 5

    '''
    Transitions represented by
    (current state, opponent's last move, new state, our move to play)
    '''

    def transition_state(self,action):
        transitions = (
            (1,C,3,C),
            (1,D,8,C),
            (2,C,1,D),
            (2,D,5,D),
            (3,C,3,D),
            (3,D,8,D),
            (4,C,7,D),
            (4,D,5,C),
            (5,C,5,C),
            (5,D,7,D),
            (6,C,3,D),
            (6,D,8,D),
            (7,C,4,C),
            (7,D,6,D),
            (8,C,3,C),
            (8,D,4,D),
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
    
class TunedSubmission(Player):
    name = 'TunedSubmission'
    

    def __init__(self):
        super().__init__()
        self.cur_state = 3
        self.transitions = ((0, C, 7, C), (0, D, 1, D), (1, C, 2, D), (1, D, 1, D), (2, C, 2, C), (2, D, 7, C), (3, C, 3, C), (3, D, 7, D), (4, C, 4, D), (4, D, 6, C), (5, C, 7, D), (5, D, 2, C), (6, C, 6, D), (6, D, 5, C), (7, C, 6, D), (7, D, 7, D))
    
    def transition_state(self,action):
        if action == C:
            transition = self.transitions[self.cur_state*2]
        else:
            transition = self.transitions[self.cur_state*2+1]
        self.cur_state = transition[2]
        return transition[3]

    def strategy(self, opponent: Player) -> Action:
        
        #first move
        if not self.history: return C
        
        move = self.transition_state(opponent.history[-1])
        return move

class PFSM(Player):
    name = 'PFSM'

    def __init__(self):
        super().__init__()
        self.cur_state = 0

    '''
    Transitions represented by
    (current state, opponent's last move, new state, the probability of us playing C)
    '''

    def transition_state(self,action):
        transitions = (
            (0,C,0,1),
            (0,D,0,0)
        )
        if action == C:
            return transitions[self.cur_state*2][3]
        else:
            return transitions[self.cur_state*2+1][3]

    def strategy(self, opponent: Player) -> Action:
        
        #first move
        if not self.history: return C
        
        c_prob = self.transition_state(opponent.history[-1])
        if random.random() < c_prob:
            return C
        else:
            return D
