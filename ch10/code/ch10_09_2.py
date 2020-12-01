"""
@BY: Reem Alghamdi
@DATE: 25-11-2020
"""
from ch10.code.ch10_09 import profile_hmm_pseudocount
import numpy as np


def sequence_alignment_with_profile_hmm(x, threshold, pseudocount, alphabet, alignments):
    states, paths, transition, transition_square_pair, emission, emission_square_pair = profile_hmm_pseudocount(threshold, pseudocount, alphabet, alignments)
    states.remove("S")
    states.remove("E")
    # print(paths)
    # print(transition)
    # print(emission)

    col_len = len(x) if "-" not in x else len(x.replace("-", ""))
    # print(col_len)
    s_0 = np.zeros(col_len + 1)
    s = np.zeros((len(states), col_len))
    backtrack = [np.ones((len(states), col_len), dtype=int)]
    # print(s)
    for i in range(len(s_0)):
        if i == 0:
            s_0[0] = transition["S"]["D1"]
        else:
            s_0[i] = transition[f"D{i + 1}"][f"D{i}"]
    # print(s_0)
    # print(transition_square_pair)
    # print(emission_square_pair)

    for i in range(s.shape[1]):
        for k in range(s.shape[0]):
            # print(i, k)
            if i == 0:
                print(states[k])
                print(transition_square_pair[states[k]])
                print(emission[x[i]][states[k]])

                # options = [s_0[l] * transition[states[k]][l] * emission[x[i]][states[k]] for l in transition_square_pair[states[k]]]
                # print(options)
            # else:
            #     options = [s[l][i - 1] * transition[states[k]][l] * emission[x[i]][states[k]] for l in transition_square_pair[states[k]]]
            #
            # s[k][i] = max(options)
            # backtrack[k][i] = options.index(s[k][i])
    # print(s)


if __name__ == "__main__":
        al = """ACDEFACADF
AFDA---CCF
A--EFD-FDC
ACAEF--A-C
ADDEFAAADF"""
        sequence_alignment_with_profile_hmm("AEFDFDC", 0.4, 0.01, "A B C D E F".split(), al.split())
