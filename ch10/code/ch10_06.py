"""
@BY: Reem Alghamdi
@DATE: 22-11-2020
"""
import numpy as np
from ch10.code.ch10_05 import format_to_df


def viterbi_decoding(x, alphabet, states, emission, transition):
    backtrack = np.ones((len(states), (len(x))), dtype=int)
    s = np.zeros((len(states), len(x)))
    for k in range(0, s.shape[0]):
        s[k][0] = (1 / len(states)) * emission[x[0]][states[k]]
        backtrack[k][0] = -1

    for i in range(1, s.shape[1]):
        for k in range(s.shape[0]):
            options = [s[l][i - 1] * transition[states[k]][states[l]] * emission[x[i]][states[k]] for l in range(len(states))]
            s[k][i] = max(options)
            backtrack[k][i] = options.index(s[k][i])
    sink_pos = np.argmax(s[:, -1])
    sink = s[sink_pos, -1]
    # print(sink, sink_pos)
    #
    # print(s)
    pointer = len(x) - 1
    path = ""
    val = sink_pos
    path = states[sink_pos]
    while pointer > 0:
        val = backtrack[val][pointer]
        path = states[val] + path
        pointer -= 1
    # path = ''.join([x for x in backtrack[sink_pos]]) + states[sink_pos]
    return path


if __name__ == "__main__":

    with open("../data/hmm1") as tr:
        with open("../data/hmm2") as em:
            print(viterbi_decoding("xzxyxyxxzxzxzzyyxyxxxyyyxxzyyxxxyzxyyxyyxxxzyxzxxzxyzyxzyyyxxzyyxxxxyzzyyyzyxzzzxxxxzzxxyzxzzyyyxzxy", "x y z".split(), "A B C D".split(), format_to_df(em), format_to_df(tr)))
