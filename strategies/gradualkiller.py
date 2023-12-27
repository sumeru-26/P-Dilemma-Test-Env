class GradualKiller:
    """
    It begins by defecting in the first five moves, then cooperates two times.
    It then defects all the time if the opponent has defected in move 6 and 7,
    else cooperates all the time.
    Initially designed to stop Gradual from defeating TitForTat in a 3 Player
    tournament.

    Names

    - Gradual Killer: [Prison1998]_
    """

    # These are various properties for the strategy
    name = "Gradual Killer"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick < 7:
            return "DDDDDCC"[tick]
        if their_history[5:7] == "DD":
            return "D"
        return "C"
