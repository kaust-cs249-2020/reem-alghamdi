"""
@BY: Reem Alghamdi
@DATE: 22-11-2020
"""
import numpy as np
from ch10.code.ch10_05 import format_to_df


def viterbi_decoding_problem(x, alphabet, states, emission, transition):
    """
    * make DAG with start and sink nodes and  |States| rows and n columns (n is the length of emitted x)
    * S + backtrack
    * return longest path
    """
    backtrack = np.ones((len(states), (len(x) - 1)), dtype=str)
    s = np.zeros((len(states), len(x)), dtype=float)
    for k in range(0, s.shape[0]):
        s[k][0] = (1 / len(states)) * emission[x[0]][states[k]]

    for k in range(0, s.shape[0]):
        for i in range(1, s.shape[1]):
            options = [s[l][i-1] * transition[states[l]][states[k]] * emission[x[i - 1]][states[l]] for l in range(len(states))]
            s[k][i] = max(options)
            backtrack[k][i - 1] = states[options.index(s[k][i])]
    sink_pos = np.argmax(s[:, -1])
    sink = s[sink_pos, -1]
    print(s)
    print(backtrack, sink, sink_pos)
    path = ''.join([x for x in backtrack[sink_pos]]) + states[sink_pos]
    return path


if __name__ == "__main__":
    with open("../data/hmm1") as tr:
        with open("../data/hmm2") as em:
            print(viterbi_decoding_problem("xyxzzxyxyy", "x y z".split(), "A B".split(), format_to_df(em), format_to_df(tr)))
