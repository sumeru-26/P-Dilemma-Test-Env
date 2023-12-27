from numpy import random


class Alternator:
    """
    A player who alternates between cooperating and defecting.

    Names

    - Alternator: [Axelrod1984]_
    - Periodic player CD: [Mittal2009]_
    """

    name = "Alternator"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)

        if tick == 0:
            return "C"
        if my_history[-1] == "C":
            return "C"
        return "D"
