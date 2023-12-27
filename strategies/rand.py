from numpy import random


class Random:
    """A player who randomly chooses between cooperating and defecting.

    This strategy came 15th in Axelrod's original tournament.

    Names:

    - Random: [Axelrod1980]_
    - Lunatic: [Tzafestas2000]_
    """

    name = "Random"
    score = 0
    rounds = 0

    def reponse(self, state):
        return random.choice(["C", "D"])
