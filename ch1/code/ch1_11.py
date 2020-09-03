"""
@BY: Reem Alghamdi
@DATE: 03-09-2020
"""


def immediate_neighbors(pattern):
    """
    This function takes a pattern, and return ALL patterns where the hamming distance is 1
    :param pattern: the pattern to find its neighbors
    :return: an array of patterns where the hamming distance between them and the pattern is 1
    """
    neighborhood = []
    nucleotides = ["A", "C", "T", "G"]
    for index in range(len(pattern)):
        symbol = pattern[index]
        for nucleotide in nucleotides:
            if symbol != nucleotide:
                neighbor = list(pattern)
                neighbor[index] = nucleotide
                neighbor = "".join(neighbor)
                neighborhood.append(neighbor)
    neighborhood.append(pattern)
    print(*neighborhood)
    return neighborhood


def neighbors(pattern, d):
    """
    This function takes a pattern, and a hamming distance and return ALL patterns where the hamming distance is d
    :param pattern: the pattern to find its neighbors
    :param d: the maximum hamming distance between the pattern and the neighbors
    :return: an array of patterns where the hamming distance between them and the pattern is at most d
    """
    from ch1.code.ch1_08 import hamming_distance

    nucleotides = ["A", "C", "T", "G"]

    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return nucleotides
    neighborhood = []
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(text, pattern[1:]) < d:
            for nucleotide in nucleotides:
                neighborhood.append(nucleotide + text)
        else:
            neighborhood.append(pattern[0] + text)
    return neighborhood


if __name__ == "__main__":
    immediate_neighbors("ACG")
    print(*neighbors("TGTAGATATAA", 3))
    print(len(neighbors("TGTAGATATAA", 3)))
