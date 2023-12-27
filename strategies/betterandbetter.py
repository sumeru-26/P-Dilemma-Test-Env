from numpy import random


class BetterAndBetter:
    """
    Defects with probability of '(1000 - current turn) / 1000'.
    Therefore it is less and less likely to defect as the round goes on.

    Names:
        - Better and Better: [Prison1998]_

    """

    name = "Better and Better"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)

        return "C" if random.random() < (tick + 1) / 1000 else "D"
