"""
@BY: Reem Alghamdi
@DATE: 19-09-2020
"""
from ch3.code.ch3_08 import euler_path
from ch3.code.ch3_13 import de_bruijn_graph_from_pairs, string_spelled_by_gapped_patterns


def print_pairs(pairs):
    for pair in pairs:
        print(f"({pair[0]}|{pair[1]})", end=" ")
    print()


def format_pairs(text):
    pairs = text.split("\n")
    pairs = [tuple(x.split("|")) for x in pairs]
    return pairs


def paired_composition(k, d, text):
    """
    given a text, a length k-mer and the number of letters in between the pairs (d),
    this function returns a collection of pairs with d distance in between
    """
    pairs = []
    for index in range(len(text) - k * 2):
        pattern1 = text[index:index+k]
        pattern2 = text[index+d+k:index+d+k*2]
        pairs.append((pattern1, pattern2))
    print_pairs(pairs)
    return sorted(pairs)


def string_reconstruction_from_pairs(k, d, paired_reads):
    """
    take a list of (k, d) paired reads
    then find de bruijn, then euler path and finally path to genome
    """
    adj_list = de_bruijn_graph_from_pairs(paired_reads)
    path = euler_path(adj_list)
    text = string_spelled_by_gapped_patterns(path, k, d)
    return text


if __name__ == "__main__":
    # print_pairs(paired_composition(3, 1, "TAATGCCATGGGATGTT"))
    with open("../data/dataset_369274_16.txt") as file:
        print(string_reconstruction_from_pairs(50, 200, format_pairs(file.read())))
