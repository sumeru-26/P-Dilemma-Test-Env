from numpy import random


class Inverse:
    """A player who defects with a probability that diminishes relative to how
    long ago the opponent defected.

    Names:

    - Inverse: Original Name by Karol Langner
    """

    name = "Inverse"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")

        index = next(
            (
                index
                for index, value in enumerate(their_history, start=1)
                if value == "D"
            ),
            None,
        )

        if index == None:
            return "C"

        return "C" if random.random() < (1 - 1 / abs(index)) else "D"
