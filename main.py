from submission import *

import axelrod as axl

copies = 5

strategies = [
    Submission,
    TunedSubmission,
    axl.TitFor2Tats,
    axl.TwoTitsForTat,
    axl.HardTitFor2Tats,
    axl.HardTitForTat,
    axl.SlowTitForTwoTats2,
    axl.RandomTitForTat,
    axl.SneakyTitForTat,
    axl.SpitefulTitForTat,
    axl.CautiousQLearner,
    axl.ArrogantQLearner,
    axl.Grudger,
    axl.Grumpy,
    axl.Defector,
    axl.Detective,
    axl.Bully,
    axl.AntiTitForTat,
    axl.AdaptiveTitForTat,
    axl.MathConstantHunter,
    axl.OriginalGradual,
    axl.Random,
    axl.OmegaTFT,
    axl.Adaptive,
    axl.APavlov2011,
    axl.AverageCopier,
    axl.GoByMajority5,
    axl.HardGoByMajority10,
    axl.Doubler,
    axl.CyclerDC,
    axl.CyclerCCCCCD,
    axl.Inverse,
    axl.Prober4,
    axl.Retaliate3,
    axl.TrickyCooperator,
    axl.TrickyDefector,
    axl.SecondByEatherley,
    axl.ZDExtort4,
    axl.UsuallyCooperates,
    axl.EvolvedANN
]



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

data_dict = {}
for i in summary_data:
    if i.Name in data_dict:
        data_dict.update({i.Name : (data_dict[i.Name]+i.Median_score)/2})
    else:
        data_dict.update({i.Name : i.Median_score})

data_dict = dict(sorted(data_dict.items(),key= lambda x:x[1], reverse=True))

for name,score in data_dict.items():
    print(
        " "
        + name.ljust(25, " ")
        + "| "
        + str(round(score, 3))
    )

print("-" * 50)
