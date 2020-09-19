"""
@BY: Reem Alghamdi
@DATE: 19-09-2020
"""
from ch3.code.ch3_03 import genome_path
from ch3.code.ch3_08 import euler_path


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


def de_bruijn_graph_from_pairs(pairs):
    """
    :param pairs: (k,d)-mer pairs collection
    :return adjacency list of prefix/suffix of pairs
    """
    adj_list = {}
    for pair in pairs:
        from_prefix = (pair[0][:-1], pair[1][:-1])
        to_suffix = (pair[0][1:], pair[1][1:])
        if adj_list.get(from_prefix):
            adj_list[from_prefix].append(to_suffix)
        else:
            adj_list[from_prefix] = [to_suffix]
    return adj_list


def string_spelled_by_gapped_patterns(gapped_patterns, k, d):
    """
    :param gapped_patterns: the sequence of (k, d)-mer pairs such that suffix(ai,bi) = prefix(ai+1,bi+1), 1<= i<= n-1
    :param k: length of k-mers
    :param d: the distance between the pair
    :return: a string of length (2k + d + n -1), such that the i-th (k, d)-mer = (ai,bi) for i between 1 and n
    """
    first = [pattern[0] for pattern in gapped_patterns]
    second = [pattern[1] for pattern in gapped_patterns]
    prefix_string = ''.join([first[0]] + [string[-1] for string in first[1:]])
    suffix_string = ''.join([second[0]] + [string[-1] for string in second[1:]])
    for i in range(k + d + 1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return "there is no string spelled by the gapped patterns"
    return prefix_string + suffix_string[-(k+d):]


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
#     print(string_spelled_by_gapped_patterns(format_pairs("""GACC|GCGC
# ACCG|CGCC
# CCGA|GCCG
# CGAG|CCGG
# GAGC|CGGA"""), 50, 200))
#     with open("../data/dataset_369278_4.txt") as file:
#         print(string_spelled_by_gapped_patterns(format_pairs(file.read()), 50, 200))
#     print(string_reconstruction_from_pairs(4, 2, format_pairs(
# """GAGA|TTGA
# TCGT|GATG
# CGTG|ATGT
# TGGT|TGAG
# GTGA|TGTT
# GTGG|GTGA
# TGAG|GTTG
# GGTC|GAGA
# GTCG|AGAT""")))
    with open("../data/dataset_369274_16.txt") as file:
        print(string_reconstruction_from_pairs(50, 200, format_pairs(file.read())))
