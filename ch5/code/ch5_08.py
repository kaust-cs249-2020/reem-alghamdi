"""
@BY: Reem Alghamdi
@DATE: 02-10-2020
"""
import numpy as np
import sys
sys.setrecursionlimit(1500)


def lcs_backtrack(v, w):
    backtrack = [[""] * (len(w)) for i in range(len(v))]
    s = np.zeros((len(v) + 1, len(w) + 1), dtype=int)
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            match = 0
            if v[i - 1] == w[j - 1]:
                match = 1
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + match)
            if s[i][j] == s[i - 1][j]:
                backtrack[i-1][j-1] = "↓"
            elif s[i][j] == s[i][j - 1]:
                backtrack[i-1][j-1] = "→"
            elif s[i][j] == s[i - 1][j - 1] + match:
                backtrack[i-1][j-1] = "↘"
    # print(s)
    # print(backtrack)
    return backtrack


def output_lcs(backtrack, v, i, j):
    if i == 0 or j == 0:
        return ""
    if backtrack[i-1][j-1] == "↓":
        return output_lcs(backtrack, v, i - 1, j)
    elif backtrack[i-1][j-1] == "→":
        return output_lcs(backtrack, v, i, j - 1)
    else:
        return output_lcs(backtrack, v, i - 1, j - 1) + v[i - 1]


def longest_common_subsequence(s, t):
    backtrack = lcs_backtrack(s, t)
    return output_lcs(backtrack, s, len(s), len(t))


if __name__ == "__main__":
    # print(longest_common_subsequence("AACCTTGG", "ACACTGTGA"))
    # s = "ATTCAATTAACGGGGGCCTTGGTACTGTTAACTAGTGAGTCTAGACCCAAATAAGTTGCTAGTGAGCTTCGCAGCGCTCTCCGCTTGAACCATCCTCGCGACAGCCGCCTTCGTTCAACTCAGGACACACATGTAGTGCATCTCCTGGGATACATCCAATTTACTCTTGGATGATCGCTTCGTAACTAAGTGACTGTACCCAGTACGCTGGAGCGGAACATGAGTACCAGTTGATCAAGTGTGGACGTGGGGGCGTGTGCAGTTGTCCGGCTGTCCATCGCTAAGCAGCTTTGATTCCAAGATGGACCGTTGGGTTTAACGTTCCAGAATCTATGCAGTCTCTATAAAAGTGCAGGGTATATCCTTCTAGATGCAACGAATTATGGACGAGGCGCGCGCTCTTGTTATCCTTTCCGCAAGAATGCGCTCGCAAAGTGGTAGTTAATTAATCGCTACTCGCCTAACTGTGCGTCATTTTGAATGCATTTTCATCCGGTATAACCGGTCATAACGTGGATCGCCAGAAGCCGGGAAAGTTAACACGTGGAAGATGTGTAGTTAATATGACAACGTAGCCCCAAACAACGGATAATCCTTTGGGGGCCTTCCTAATGGCTTGAGGTGCGTGGCAAGATTGGCGTTGCACCCCTGTTCTCAATAACAGCCAGCTATTACAGGCCAAGGCAGCTTGGCTCATACGACAACACCAAGAAACACCCAATCTGCTTGGTCAGACTATGGGGGACAGCGTATTCCACTGCCTTCAAGCGAAGACCGTTAAAGGACCTGACTGCTACCCCAGCCAACAAGTACCCGAATCTTAACCCTCACAGGTCCTGTGTGGACCACCGCCGGGCACGTATAATGGTCGCAGTATGGTCTCGCCTGGGCGCCTCTG"
    # t = "GTGGTTTCGGCTCTGCGGTCATGCCCGGGTAATTGAACTGCCGTGCGCTTGACTAGGAGATCTAGCCTGTATGTCTTCGACATGAACCCATTTATCGGAGTGCATCTCACCGGTGACACGAAGTTCTCCTCCGGGAGCACTATGTTCGCTTTGAGACTGACGCACTTTATAACCGTTGTATCCTGTTGCCACGTGGGATATTCAACAGTCTCGTACAAATAGGGTGAGCTCTCGCACTTTCTATTTTCCTACATACGTGTATTAAGTCAGGCCAGGCCACTCGAGAACGGAGATCCCCACTTACGCACAACTCACACGCGGCCAGCACGATGAGTCGCACGGTACGTTAGTGCCCTTGCGGGCGTCAAGCCTCGTCATACTATCTAAAGAAAGTTTAGAGTATGCCCGACAAAGACGATGTGTGCCCACCGCCAGGTTAGTTATAGTTCGCTTGCTAGGTCATTGGCTAGTGGCTTGTTAGTGCCGATGCGGCTAAGATTCAGTTCATTTATAGGATCGATCAAAAACAAGCGCCGACGGCGAGCCGTCGAATCCTCTTAAGTGCACTTTCATAAGAGGGTTCCGGTAACTTCAATCTGTGTTGAATCCCATACGCAAAAGAGAAACCCACTCAATACCCCTCCTCTCGTTGTTCAGCGCATTGATCCGCGTATCACTTGGAACAGTAACCATATCGCTCAAATAGCGGTGGCTAAACGTCTCGCTGTTCCACTCTTTAGCTAGAACCGGTCCAAGTGCGAACTTAGTAAGGCGAGTATTCTGAAGCAATCGCCTCACCCGCCGCACGTTCAGAGACACCCTGAGCCCCCAATGCGTAGAACCTCTATCGGGAGCCGTACACCAACTGGTATTGATTACAGCTAGCTTTCTGCACACTGATCTCCGGGGTCTGCCTGTTATGCTATCGACTAAAGTTGTCCTGGCGCCGCCCGAGCTCTAGT"
    # print(longest_common_subsequence(s, t))
    print(longest_common_subsequence("GACT", "ATG"))
    print(longest_common_subsequence("ACTGAG", "GACTGG"))
    print(longest_common_subsequence("AC", "AC"))
    print(longest_common_subsequence("GGGGT", "CCCCT"))
    print(longest_common_subsequence("TCCCC", "TGGGG"))
    print(longest_common_subsequence("AA", "CGTGGAT"))
    print(longest_common_subsequence("GGTGACGT", "CT"))

