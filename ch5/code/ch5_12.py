"""
@BY: Reem Alghamdi
@DATE: 13-10-2020
"""

import numpy as np

from ch5.code.ch5_10 import blosum62_matrix


def alignment_affine_gap(v, w, sigma=1, scoring_matrix=None, matches=1, mismatches=1, epsilon=1):
    """

    Input: Two amino acid strings v and w (each of length at most 100).
    Output: The maximum alignment score between v and w, followed by an alignment of v and w achieving this maximum score.
    Use the BLOSUM62 scoring matrix, a gap opening penalty of 11, and a gap extension penalty of 1.

    """
    len_v = len(v)
    len_w = len(w)
    lower = np.zeros((len_v + 1, len_w + 1), dtype=float)
    upper = np.zeros((len_v + 1, len_w + 1), dtype=float)
    middle = np.zeros((len_v + 1, len_w + 1), dtype=float)
    backtrack = [[""] * (len_w + 1) for i in range(len_v + 1)]

    for i in range(1, len(v)+1):
        lower[i][0] = -(sigma + (i-1)*epsilon)
        middle[i][0] = -(sigma + (i-1)*epsilon)
        upper[i][0] = -float("inf")
    for j in range(1, len(w)+1):
        upper[0][j] = -(sigma + (j-1)*epsilon)
        middle[0][j] = -(sigma + (j-1)*epsilon)
        lower[0][j] = -float("inf")

    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            match = int(scoring_matrix[v[i - 1]][w[j - 1]]) if scoring_matrix else matches if v[i - 1] == w[
                j - 1] else -mismatches

            lower[i][j] = max(lower[i-1][j] - epsilon,
                              middle[i-1][j] - sigma)
            upper[i][j] = max(upper[i][j-1] - epsilon,
                              middle[i][j-1] - sigma)

            options = [lower[i][j], middle[i-1][j-1] + match, upper[i][j]]
            middle[i][j] = max(options)

            if middle[i][j] == options[0]:
                backtrack[i][j] = "↓"
            elif middle[i][j] == options[1]:
                backtrack[i][j] = "↘"
            elif middle[i][j] == options[2]:
                backtrack[i][j] = "→"

    score_max = int(middle[-1][-1])
    i = len_v
    j = len_w
    # print(s, backtrack)
    while i != 0 and j != 0:
        if backtrack[i][j] == "↓":  # first option lower
            i -= 1
            w = w[:j] + "-" + w[j:]
        elif backtrack[i][j] == "→":  # second option upper
            j -= 1
            v = v[:i] + "-" + v[i:]
        else:  # third option middle
            i -= 1
            j -= 1

    for i in range(i):
        w = w[:0] + "-" + w[0:]

    for i in range(j):
        v = v[:0] + "-" + v[0:]

    return score_max, v, w


if __name__ == "__main__":
    print(alignment_affine_gap("PRTEINS", "PRTWPSEIN", epsilon=1, sigma=11, scoring_matrix=blosum62_matrix))
    # v = "ENHIWTEQTNQAYNEKLHLETALNYSAARQKERTLDIMSMINYQHGFQLLEHLQMAAAQHYEYPCKFQMANCNVASA"
    # w = "ENHIWQTNRAYNEKLHLETALNYSAARQKERTLDIMSMINTQHGFQLTEHLKDDTQHYEPPSA"
    # s_max, v, w = alignment_affine_gap(v, w)
    # print(s_max)
    # print(v)
    # print(w)
    # print(alignment_affine_gap("GA", "GTTA", matches=1, mismatches=3, sigma=2, epsilon=1))
    # print(alignment_affine_gap("TTT", "TT", matches=1, mismatches=5, sigma=3, epsilon=1))
    # print(alignment_affine_gap("GAT", "AT", matches=1, mismatches=5, sigma=5, epsilon=1))
    # print(alignment_affine_gap("CCAT", "GAT", matches=1, mismatches=5, sigma=2, epsilon=1))
    # print(alignment_affine_gap("CAGGT", "TAC", matches=1, mismatches=2, sigma=3, epsilon=2))
    # print(alignment_affine_gap("GTTCCAGGTA", "CAGTAGTCGT", matches=2, mismatches=3, sigma=3, epsilon=2))
    # print(alignment_affine_gap("AGCTAGCCTAG", "GT", matches=1, mismatches=3, sigma=1, epsilon=1))
    # print(alignment_affine_gap("AA", "CAGTGTCAGTA", matches=2, mismatches=1, sigma=2, epsilon=1))
    # print(alignment_affine_gap("ACGTA", "ACT", matches=5, mismatches=2, sigma=15, epsilon=5))
    # print(alignment_affine_gap("YHFDVPDCWAHRYWVENPQAIAQMEQICFNWFPSMMMKQPHVFKVDHHMSCRWLPIRGKKCSSCCTRMRVRTVWE", "YHEDVAHEDAIAQMVNTFGFVWQICLNQFPSMMMKIYWIAVLSAHVADRKTWSKHMSCRWLPIISATCARMRVRTVWE", scoring_matrix=blosum62_matrix, sigma=11, epsilon=1))
