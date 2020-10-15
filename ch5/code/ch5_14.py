"""
@BY: Reem Alghamdi
@DATE: 15-10-2020
"""
import numpy as np


def multiple_longest_common_subsequence(v, w, u, sigma=0, scoring_matrix=None, matches=1, mismatches=0):
    """
    given two strings and a score matrix,
    return the alignment of the strings with max score
    """
    len_v = len(v)
    len_w = len(w)
    len_u = len(u)
    s = np.zeros((len_v + 1, len_w + 1, len_u + 1), dtype=int)
    backtrack = np.zeros((len_v + 1, len_w + 1, len_u + 1), dtype=int)

    for i in range(1, len_v + 1):
        for j in range(1, len_w + 1):
            for k in range(1, len_u + 1):
                m = int(scoring_matrix[v[i - 1]][w[j - 1]][u[k - 1]]) if scoring_matrix else matches if v[i - 1] == w[j - 1] == u[k - 1] else - mismatches
                options = [s[i-1][j][k]-sigma, s[i][j-1][k]-sigma, s[i][j][k-1]-sigma,
                           s[i-1][j][k-1], s[i][j-1][k-1]-sigma, s[i-1][j-1][k],
                           s[i-1][j-1][k-1] + m]
                backtrack[i][j][k], s[i][j][k] = max(enumerate(options), key=lambda p: p[1])

    score_max = s[-1][-1][-1]
    i = len_v
    j = len_w
    k = len_u
    # print(s, backtrack)
    while i != 0 and j != 0 and k != 0:
        if backtrack[i][j][k] == 0:
            i -= 1
            w = w[:j] + "-" + w[j:]
            u = u[:k] + "-" + u[k:]
        elif backtrack[i][j][k] == 1:
            j -= 1
            v = v[:i] + "-" + v[i:]
            u = u[:k] + "-" + u[k:]
        elif backtrack[i][j][k] == 2:
            k -= 1
            v = v[:i] + "-" + v[i:]
            w = w[:j] + "-" + w[j:]
        elif backtrack[i][j][k] == 3:
            i -= 1
            k -= 1
            w = w[:j] + "-" + w[j:]
        elif backtrack[i][j][k] == 4:
            j -= 1
            k -= 1
            v = v[:i] + "-" + v[i:]
        elif backtrack[i][j][k] == 5:
            i -= 1
            j -= 1
            u = u[:k] + "-" + u[k:]
        else:
            i -= 1
            j -= 1
            k -= 1

    for r in range(i, max(i, j, k)):
        v = v[:0] + "-" + v[0:]

    for r in range(j, max(i, j, k)):
        w = w[:0] + "-" + w[0:]

    for r in range(k, max(i, j, k)):
        u = u[:0] + "-" + u[0:]
    return score_max, v, w, u


if __name__ == "__main__":
    # print(multiple_longest_common_subsequence("ATATCCG", "TCCGA", "ATGTACTG"))
    # print(multiple_longest_common_subsequence("A", "AT", "A"))
    # print(multiple_longest_common_subsequence("AAAAT", "CCCCT", "T"))
    # print(multiple_longest_common_subsequence("AT", "ACCT", "AGGGGT"))
    # print(multiple_longest_common_subsequence("GGAG", "TT", "CCCC"))
    # print(multiple_longest_common_subsequence("T", "T", "T"))

    s, v, w, u = multiple_longest_common_subsequence("ACGGAGCT", "TGACTCAC", "GGTGGTTCC")
    print(s)
    print(v)
    print(w)
    print(u)
