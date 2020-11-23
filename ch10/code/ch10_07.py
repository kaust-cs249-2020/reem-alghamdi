"""
@BY: Reem Alghamdi
@DATE: 23-11-2020
"""
import numpy as np
from ch10.code.ch10_05 import format_to_df


def outcome_likelihood_problem(x, alphabet, states, emission, transition):
    s = np.zeros((len(states), len(x)))
    for k in range(0, s.shape[0]):
        s[k][0] = (1 / len(states)) * emission[x[0]][states[k]]

    for i in range(1, s.shape[1]):
        for k in range(s.shape[0]):
            options = [s[l][i - 1] * transition[states[k]][states[l]] * emission[x[i]][states[k]] for l in range(len(states))]
            s[k][i] = sum(options)
    sink_pos = sum(s[:, -1])
    return sink_pos


if __name__ == "__main__":
    with open("../data/hmm1") as tr:
        with open("../data/hmm2") as em:
            print(outcome_likelihood_problem("zxxyxxxxyxyzzxyyxyzxxxzxzxxzyxyzxzxyyxxzxzxxxzzxyzzyyyxzzyzxxyyzxyzzyxxxyyzzzzzxyzyxyyxxzzyyzyzyxyyy", "x y z".split(), "A B C D".split(), format_to_df(em), format_to_df(tr)))
