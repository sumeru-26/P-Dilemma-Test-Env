class Handshake:
    """Starts with C, D. If the opponent plays the same way, cooperate forever,
    else defect forever.

    Names:

    - Handshake: [Robson1990]_
    """

    name = "Handshake"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick <= 1:
            return "CD"[tick]
        if my_history[:2] == their_history[:2]:
            return "C"
        return "D"
