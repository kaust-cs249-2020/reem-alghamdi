"""
@BY: Reem Alghamdi
@DATE: 05-09-2020
"""
from collections import OrderedDict
from ch1.code.ch1_11 import neighbors


def motif_enumeration(dna, k, d):
    """
    This function takes a collection of strings dna, and finds a list of k-mer with at most d-mismatches appearing in all strings
    :param dna: A collection of strings Dna
    :param k: length of k-mer
    :param d: hamming distance
    :return: list of (k, d)-motifs in Dna
    """
    patterns = []
    for index in range(len(dna[0]) - k + 1):
        pattern = dna[0][index: index + k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            neighborhood_neighbor = neighbors(neighbor, d)
            appear_all = True
            for string in dna:
                appear = False
                for nn in neighborhood_neighbor:
                    if nn in string:
                        appear = True
                        break
                if not appear:
                    appear_all = False
                    break
            if appear_all:
                patterns.append(neighbor)

    patterns = list(OrderedDict.fromkeys(patterns))
    return patterns


if __name__ == "__main__":
    print(*motif_enumeration([
        "ACGCGATTTGGTGTAACACTTCGAA",
        "CTACGCAGCGACTTCATTCGGCACC",
        "AAGGGGAGACACCGGTACACATTCG",
        "ATTTGCAATCCACCACTTATTTACC",
        "CCTTAGCTGGATACCATTAGATCTT",
        "GTTTCCTTGAAGTCGATTTGCTCTC"
    ], 5, 1))
