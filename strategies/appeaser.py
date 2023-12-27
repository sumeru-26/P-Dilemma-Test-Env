class Appeaser:
    """A player who tries to guess what the opponent wants.

    Switch the classifier every time the opponent plays D.
    Start with C, switch between C and D when opponent plays D.

    Names:

    - Appeaser: Original Name by Jochen Müller
    """

    name = "Appeaser"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)

        if tick == 0:
            return "C"
        else:
            if their_history[-1] == "D":
                if my_history[-1] == "C":
                    return "D"
                else:
                    return "C"
        return my_history[-1]
