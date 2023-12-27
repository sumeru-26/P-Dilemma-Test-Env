from numpy import random


class TitForTat:
    """
    A player starts by cooperating and then mimics the previous action of the
    opponent.

    This strategy was referred to as the *'simplest'* strategy submitted to
    Axelrod's first tournament. It came first.

    Note that the code for this strategy is written in a fairly verbose
    way. This is done so that it can serve as an example strategy for
    those who might be new to Python.

    Names:

    - Rapoport's strategy: [Axelrod1980]_
    - TitForTat: [Axelrod1980]_
    """

    name = "Tit For Tat"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick == 0:
            return "C"
        return their_history[-1]


class TitFor2Tats:
    """A player starts by cooperating and then defects only after two defects by
    opponent.

    Submitted to Axelrod's second tournament by John Maynard Smith; it came in
    24th in that tournament.

    Names:

    - Tit for two Tats: [Axelrod1984]_
    - Slow tit for two tats: Original name by Ranjini Das
    - JMaynardSmith: [Axelrod1980b]_
    """

    name = "Tit For 2 Tats"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)

        return "D" if their_history[-2:] == "DD" else "C"


class TwoTitsForTat:
    """A player starts by cooperating and replies to each defect by two
    defections.

    Names:

    - Two Tits for Tats: [Axelrod1984]_
    """

    name = "Two Tits For Tat"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)

        return "D" if "D" in their_history[-2:] else "C"
