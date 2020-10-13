"""
@BY: Reem Alghamdi
@DATE: 13-10-2020
"""
import numpy as np

from ch5.code.ch5_10 import blosum62_matrix


def alignment_affine_gap(v, w, score=blosum62_matrix, gap_opening=11, gap_extension=1):
    """

    Input: Two amino acid strings v and w (each of length at most 100).
    Output: The maximum alignment score between v and w, followed by an alignment of v and w achieving this maximum score.
    Use the BLOSUM62 scoring matrix, a gap opening penalty of 11, and a gap extension penalty of 1.

    """
    len_v = len(v)
    len_w = len(w)
    lower = np.zeros((len_v + 1, len_w + 1), dtype=int)
    upper = np.zeros((len_v + 1, len_w + 1), dtype=int)
    middle = np.zeros((len_v + 1, len_w + 1), dtype=int)
    backtrack = [[""] * (len_w + 1) for i in range(len_v + 1)]

    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            match = int(score[v[i - 1]][w[j - 1]])
            lower[i][j] = max(lower[i-1][j] - gap_extension,
                              middle[i-1][j] - gap_opening)
            upper[i][j] = max(upper[i][j-1] - gap_extension,
                              middle[i][j-1] - gap_opening)

            options = [lower[i][j], upper[i][j], middle[i-1][j-1] + match]
            middle[i][j] = max(options)

            if middle[i][j] == options[0]:
                backtrack[i][j] = "↓"
            elif middle[i][j] == options[1]:
                backtrack[i][j] = "→"
            elif middle[i][j] == options[2]:
                backtrack[i][j] = "↘"

    score_max = middle[-1][-1]
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

    return score_max, v, w


if __name__ == "__main__":
    print(alignment_affine_gap("PRTEINS", "PRTWPSEIN"))
    v = "ENHIWTEQTNQAYNEKLHLETALNYSAARQKERTLDIMSMINYQHGFQLLEHLQMAAAQHYEYPCKFQMANCNVASA"
    w = "ENHIWQTNRAYNEKLHLETALNYSAARQKERTLDIMSMINTQHGFQLTEHLKDDTQHYEPPSA"
    s_max, v, w = alignment_affine_gap(v, w)
    print(s_max)
    print(v)
    print(w)