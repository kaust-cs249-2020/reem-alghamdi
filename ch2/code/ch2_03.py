"""
@BY: Reem Alghamdi
@DATE: 05-09-2020
"""
import operator
from math import log2


def motifs(matrix):
    """
    this function takes a matrix of t x k motifs where t is the length of each columns and k is the number of columns
    then the following return values are computed
    :param matrix: t x k motif matrix
    :return: consensus, score, count, profile, entropy, entropies
    consensus: an array of length k, representing the most common nucleotide in each column
    score: the sum of unpopular letters in all columns
    count: an array of dictionaries of nucleotides where the value of their count in each column
    profile: count / t
    entropies: the entropy of each column defined by the sum of each nucleotide's profile * log2 of said profile
    entropy: the sum of entropies
    """
    count = []
    score = 0
    profile = []
    consensus = []
    entropies = []
    entropy = 0
    for i, col in enumerate(matrix):
        frequent_n = {"A": 0, "C": 0, "G": 0, "T": 0}
        for nucleotide in col:
            frequent_n[nucleotide] += 1
        most_freq = max(frequent_n.items(), key=operator.itemgetter(1))[0]
        score = score + (len(col) - frequent_n[most_freq])
        count.append(frequent_n)
        profile.append({k: v/len(col) for k, v in frequent_n.items()})
        consensus.append(most_freq)

        log = -((profile[i]["A"]*log2(profile[i]["A"]) if profile[i]["A"] != 0 else 0) +
                (profile[i]["T"]*log2(profile[i]["T"]) if profile[i]["T"] != 0 else 0) +
                (profile[i]["C"]*log2(profile[i]["C"]) if profile[i]["C"] != 0 else 0) +
                (profile[i]["G"]*log2(profile[i]["G"]) if profile[i]["G"] != 0 else 0))

        entropies.append(log)
        entropy += log
    return consensus, score, count, profile, entropy, entropies


if __name__ == "__main__":
    matrix = [
        "TCATATTTTT",
        "CCCTATCCAC",
        "GGGGGGGGGG",
        "GGGGGGGGGG",
        "GTGGGGGGGG",
        "GGGGGGGGGT",
        "GAAAAAAAAA",
        "TCTCCCTTAT",
        "TTTTTTTTCA",
        "TTTTTTCCTA",
        "TATTCCACAC",
        "TCCTCCTTCC"
    ]

    consensus, score, count, profile, entropy, entropies = motifs(matrix)
    print(consensus)
    print(score)
    print(count)
    print(profile)
    print(entropy)
    print(entropies)

