from numpy import random


class AverageCopier:
    """
    The player will cooperate with probability p if the opponent's cooperation
    ratio is p. Starts with random decision.

    Names:

    - Average Copier: Original name by Geraint Palmer
    """

    name = "Average Copier"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)

        if tick == 0:
            return "C" if random.random() < 0.5 else "D"
        return "C" if random.random() < their_history.count("C") / tick else "D"


class NiceAverageCopier:
    """
    Same as Average Copier, but always starts by cooperating.

    Names:

    - Average Copier: Original name by Owen Campbell
    """

    name = "Nice Average Copier"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)

        if tick == 0:
            return "C"
        return "C" if random.random() < their_history.count("C") / tick else "D"
