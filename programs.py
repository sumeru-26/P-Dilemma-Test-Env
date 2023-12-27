from numpy import random


# Nice Programs
class AllC:
    name = "All C"
    score = 0
    rounds = 0

    def reponse(self, state):
        return "C"


class TFT:
    name = "Tit For Tat"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick == 0:
            return "C"
        else:
            return their_history[-1]


class TF2T:
    name = "Tit For 2 Tats"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick <= 1:
            return "C"
        else:
            if their_history[-1] == "D" and their_history[-2] == "D":
                return "D"
            else:
                return "C"


class T2FT:
    name = "2 Tits For Tat"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick <= 1:
            return "C"
        else:
            if their_history[-1] == "D" or their_history[-2] == "D":
                return "D"
            else:
                return "C"


class SlowTFT:
    name = "Slow Tit For Tat"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick <= 1:
            return "C"
        else:
            if their_history[-1] == "D" and their_history[-2] == "D":
                return "D"
            if their_history[-1] == "C" and their_history[-2] == "C":
                return "C"
            else:
                return my_history[-1]


class Pavlov:
    name = "Pavlov"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick == 0:
            return "C"
        else:
            if their_history[-1] == my_history[-1]:
                return "C"
            else:
                return "D"


class Punisher:
    name = "Punisher"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if their_history.count("D") > 0:
            return "D"
        else:
            return "C"


class Majority:
    name = "Majority"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if their_history.count("D") > their_history.count("C"):
            return "D"
        else:
            return "C"


class Majority5:
    name = "Majority 5"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if their_history[-5:].count("D") > their_history[-5:].count("C"):
            return "D"
        else:
            return "C"


class Majority11:
    name = "Majority 11"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if their_history[-11:].count("D") > their_history[-11:].count("C"):
            return "D"
        else:
            return "C"


class LSN:
    name = "Last Step Neutral"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick == 0:
            return "C"
        else:
            if their_history[-1] == "D":
                if random.random() < 0.5:
                    return "D"
                else:
                    return "C"
            else:
                return "C"


class LSC:
    name = "Last Step Cooperative"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick == 0:
            return "C"
        else:
            if their_history[-1] == "D":
                if my_history[-1] == "D":
                    if random.random() < 0.2:
                        return "D"
                    else:
                        return "C"
                else:
                    if random.random() < 0.8:
                        return "D"
                    else:
                        return "C"
            else:
                return "C"


# Nasty
class AllD:
    name = "All D"
    score = 0
    rounds = 0

    def reponse(self, state):
        return "D"


class Random:
    name = "Random"
    score = 0
    rounds = 0

    def reponse(self, state):
        return random.choice(["C", "D"])


class Mistrust:
    name = "Mistrust"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick == 0:
            return "D"
        else:
            return their_history[-1]


class Prober:
    name = "Prober"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick == 0:
            return "C"
        elif tick <= 2:
            return "D"
        else:
            if their_history[1] == "C" and their_history[2] == "C":
                return "D"
            else:
                return their_history[-1]


class JOSS:
    name = "JOSS"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick == 0:
            return "C"
        else:
            if their_history[-1] == "C":
                if random.random() < 0.9:
                    return "C"
                else:
                    return "D"
            else:
                return "D"


class LSD:
    name = "Last Step Defective"
    score = 0
    rounds = 0

    def reponse(self, state):
        tick, my_history, their_history = state.split(";")
        tick = int(tick)
        if tick == 0:
            return "C"
        else:
            if their_history[-1] == "D":
                if my_history[-1] == "D":
                    if random.random() < 0.8:
                        return "D"
                    else:
                        return "C"
                else:
                    return "D"
            else:
                if random.random() < 0.2:
                    return "D"
                else:
                    return "C"
