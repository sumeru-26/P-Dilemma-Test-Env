class Grudger:
    """
    A player starts by cooperating however will defect if at any point the
    opponent has defected.

    This strategy came 7th in Axelrod's original tournament.

    Names:

    - Friedman's strategy: [Axelrod1980]_
    - Grudger: [Li2011]_
    - Grim: [Berg2015]_
    - Grim Trigger: [Banks1990]_
    - Spite: [Beaufils1997]_
    - Spiteful: [Mathieu2015]_
    - Vengeful: [Ashlock2009]_
    """

    name = "Grudger"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if "D" in their_history:
            return "D"
        return "C"
