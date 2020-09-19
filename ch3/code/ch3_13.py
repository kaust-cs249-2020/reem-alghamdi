"""
@BY: Reem Alghamdi
@DATE: 18-09-2020
"""
from ch3.code.ch3_09 import format_pairs


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


if __name__ == "__main__":
#     print(string_spelled_by_gapped_patterns(format_pairs("""GACC|GCGC
# ACCG|CGCC
# CCGA|GCCG
# CGAG|CCGG
# GAGC|CGGA"""), 50, 200))
    with open("../data/dataset_369278_4.txt") as file:
        print(string_spelled_by_gapped_patterns(format_pairs(file.read()), 50, 200))
