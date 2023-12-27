from programs import *
from all import *
from alternator import *
from appeaser import *
from average_copier import *
from betterandbetter import *
from doubler import *
from inverse import *
from rand import *
from submission import *

import numpy as np

score_matrix = [
    [3, 0],
    [5, 1],
]

programs = [
    TFT(),
    TF2T(),
    T2FT(),
    SlowTFT(),
    Pavlov(),
    Punisher(),
    Majority(),
    Majority5(),
    Majority11(),
    LSN(),
    LSC(),
    Mistrust(),
    Prober(),
    JOSS(),
    LSD(),
    Cooperator(),
    Defector(),
    Alternator(),
    Appeaser(),
    AverageCopier(),
    NiceAverageCopier(),
    BetterAndBetter(),
    Doubler(),
    Inverse(),
    Random(),
    Submission(),
]

copies = 5
sessions = 4

num_programs = len(programs)

for i in range(sessions):
    rounds = 100 + round(-np.log(np.random.random()) * 50)

    for i in range(num_programs * copies):
        for j in range(i + 1, num_programs * copies):
            p1 = programs[i // copies]
            p1_history = ""

            p2 = programs[j // copies]
            p2_history = ""

            for k in range(rounds):
                p1.rounds += 1
                p2.rounds += 1

                p1_state = ";".join([str(k), p1_history, p2_history])
                p1_response = p1.reponse(p1_state)

                p2_state = ";".join([str(k), p2_history, p1_history])
                p2_response = p2.reponse(p2_state)

                p1.score += score_matrix[ord(p1_response) - ord("C")][
                    ord(p2_response) - ord("C")
                ]
                p2.score += score_matrix[ord(p2_response) - ord("C")][
                    ord(p1_response) - ord("C")
                ]

                p1_history += p1_response
                p2_history += p2_response


print("-" * 50)
print(" " + "Strategy Name".ljust(25, " ") + "| Avg Score Per Round")

for i in range(num_programs):
    # Sort programs by score
    for j in range(i + 1, num_programs):
        if programs[j].score > programs[i].score:
            programs[i], programs[j] = programs[j], programs[i]

    print("-" * 50)
    print(
        " "
        + programs[i].name.ljust(25, " ")
        + "| "
        + str(round(programs[i].score / programs[i].rounds, 3))
    )

print("-" * 50)
