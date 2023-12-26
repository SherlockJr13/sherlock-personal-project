#Simple Game Theory

import pandas as pd
import numpy as np

def gametheory1(i, score):
    chance = np.random.rand()
    if i == 1 and chance > 0.8:
        return True
    elif i > 1:
        if score[i-1] == [3,3]:
            return True
        else:
            return False
    else:
        return False

def gametheory2(i):
    chance = np.random.rand()
    if i == 1:
        return True
    elif i > 1:
        if chance > 0.5:
            return True
        else:
            return False
    else:
        return False


def game_sim(theory1, theory2, rounds):
    score = []
    for i in range(rounds):
        decision1 = theory1(i, score)
        decision2 = theory2(i)
        if decision1 and decision2:
            score.append([3, 3])
        elif decision1 and not decision2:
            score.append([0, 5])
        elif not decision1 and decision2:
            score.append([5, 0])
        elif not decision1 and not decision2:
            score.append([1, 1])
        else:
            break
    return score

result = game_sim(gametheory1, gametheory2, 10)
print(result)