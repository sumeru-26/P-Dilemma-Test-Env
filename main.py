from submission import *

import axelrod as axl

copies = 5
strategies = [
    Submission,
    axl.TitFor2Tats,
    axl.TwoTitsForTat,
    axl.HardTitFor2Tats,
    axl.HardTitForTat,
    axl.SlowTitForTwoTats2,
    axl.RandomTitForTat,
    axl.SneakyTitForTat,
] + axl.basic_strategies

players = []
for s in strategies:
    for _ in range(copies):
        players.append(s())

tournament = axl.Tournament(
    players,
    turns=150,
    repetitions=1,
)
results = tournament.play(progress_bar=True)


print("-" * 50)
print(" " + "Strategy Name".ljust(25, " ") + "| Avg Score Per Round")
print("-" * 50)

summary_data = results.summarise()
for i in range(0, len(players)):
    print(
        " "
        + summary_data[i].Name.ljust(25, " ")
        + "| "
        + str(round(summary_data[i].Median_score, 3))
    )

print("-" * 50)
