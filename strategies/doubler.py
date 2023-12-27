class Doubler:
    """
    Cooperates except when the opponent has defected and
    the opponent's cooperation count is less than twice their defection count.

    Names:

    - Doubler: [Prison1998]_
    """

    name = "Doubler"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick == 0:
            return "C"
        if (
            their_history[-1] == "D"
            and their_history.count("C") <= their_history.count("D") * 2
        ):
            return "D"

        return "C"
