class Forgiver:
    """
    A player starts by cooperating however will defect if at any point
    the opponent has defected more than 10 percent of the time

    Names:

    - Forgiver: Original name by Thomas Campbell
    """

    name = "Forgiver"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)

        if their_history.count("D") > tick / 10:
            return "D"
        return "C"


class ForgivingTitForTat:
    """
    A player starts by cooperating however will defect if at any point, the
    opponent has defected more than 10 percent of the time, and their most
    recent decision was defect.

    Names:

    - Forgiving Tit For Tat: Original name by Thomas Campbell
    """

    name = "Forgiving Tit For Tat"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)

        if their_history.count("D") > tick / 10:
            return their_history[-1]
        return "C"
