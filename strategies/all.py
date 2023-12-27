class Cooperator:
    """A player who only ever cooperates.

    Names:

    - Cooperator: [Axelrod1984]_
    - ALLC: [Press2012]_
    - Always cooperate: [Mittal2009]_
    """

    name = "Cooperator"
    score = 0
    rounds = 0

    def reponse(self, state):
        return "C"


class Defector:
    """A player who only ever defects.

    Names:

    - Defector: [Axelrod1984]_
    - ALLD: [Press2012]_
    - Always defect: [Mittal2009]_
    """

    name = "Defector"
    score = 0
    rounds = 0

    def reponse(self, state):
        return "D"
