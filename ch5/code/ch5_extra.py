"""
REDO USING 5.8_2
format graph using the score format
"""
from ch5.code.ch5_08_2 import longest_path_in_dag


def two_strings_to_weighted_graph(v, w, scoring_matrix=None, sigma=None):
    len_v = len(v)
    len_w = len(w)
    # total_nodes = (len_v + 1) * (len_w + 1)
    # total_edges = len_v * (len_w+1) + len_w * (len_v + 1) + len_w * len_v
    nodes = {}
    weights = {}
    sink = (0, 0)
    # initialize the nodes
    for j, b in enumerate(w + "-"):
        for i, a in enumerate(v + "-"):
            nodes[(j, i)] = []
            if i == len(v) and j == len(w):
                sink = (j, i)

    # make edges
    for node, edges in nodes.items():
        if (node[0], node[1] + 1) in nodes.keys():
            weight = -1
            nodes[node].append((node[0], node[1] + 1))
            weights[(node, (node[0], node[1] + 1))] = weight

        if (node[0] + 1, node[1]) in nodes.keys():
            weight = -1
            nodes[node].append((node[0] + 1, node[1]))
            weights[(node, (node[0] + 1, node[1]))] = weight

        if (node[0] + 1, node[1] + 1) in nodes.keys():
            weight = 1 if w[node[0]] == v[node[1]] else -1
            nodes[node].append((node[0] + 1, node[1] + 1))
            weights[(node, (node[0] + 1, node[1] + 1))] = weight

    return nodes, weights, sink


def longest_common_sequence_v2(v, w):
    # first, build the graph string
    # print("start")
    adj_list, weights, sink = two_strings_to_weighted_graph(v, w)
    # print("got adj string")
    path = longest_path_in_dag((0, 0), sink, adj_list, weights)[1]
    # print("got path")
    sequence = ""
    for index, n in enumerate(path):
        i = n[0]
        j = n[1]
        if index < len(path) - 1:  # if the next node is diagonal
            next = path[index + 1]
            k = next[0]
            l = next[1]
            if k == (i + 1) and l == (j + 1) and weights[(i, j), (k, l)] == 1:
                sequence += v[j]
    return sequence


if __name__ == "__main__":
    print(longest_common_sequence_v2("GACT", "ATG"))
    print(longest_common_sequence_v2("ACTGAG", "GACTGG"))
    print(longest_common_sequence_v2("AC", "AC"))
    print(longest_common_sequence_v2("GGGGT", "CCCCT"))
    print(longest_common_sequence_v2("TCCCC", "TGGGG"))
    print(longest_common_sequence_v2("AA", "CGTGGAT"))
    print(longest_common_sequence_v2("GGTGACGT", "CT"))
    # v = "ACCGTCTTAGCGATCAACACATTTAACAACGCGCCGCACCCCCCGTCAAACGAGCTTTTGGGCTCTTGTCCTTTTACAAGCTTCACGACGCATACAGCCTTGATCAACGGTTTGATCTGTCTCCCTTCAGCTGGCTTTAAAGGACATACATATGAAGGCCTTAATAAGGTCCGGGAACTCCACATATTCGGTACTGGGCAAACCCCATGAACCACCTCAACATGAAGAGTCCGAGGACTCTCACGATCCACCAATGCAGATCGGAACTGTGCGATCGCGTAATGAGCCGAGTACTTGGTTTGTGTTTAGGTTATGGGGGCCGGGAGCCGGTTCAATATAAGGAAGTAGTTGCAGATTAGTTGTTGCGAACGGTCATAAATTTGATGGGTAAACGTGAACTTAACAAACCGTGATAGCTAATCCTATGCATCCCTTACGTGGATCGACTCGAGTACCCAGGTGAACCGACTACTTGATAACCGGAAATCGCGGTATAAAAGCGCTCACGGTCAGGAGATATACCTCCAAGCAGTAGTCTTTCTGAGCCTAGAGTAGTAAATTACAGGGACGATGTCTTTTACCGAGGCAACATTTTATTGAGAATCACATGAGGCACAGGTAAAGGCGACATCACGATCGAGATCAACCCCTACTTGTTCAAAACATTGAGAACCAGCTCTGTTTTGGAACCTAGAAAGATAACGCATCCGCTTGATATTCCACGGCTTGTCCCTCTTGTGCGGTCCATCTATCGGAGTTTCCTCCGATACGACCCGCAATGTTTCCAGGCGTACGGTACTTTATGAATACACTCGCGCTGTAACCTGTTATGTGAAACACACACGACAGAGCTTCGCGTGGGCCCAGCGACCCGGTAATACTACATCACCGCACACGACCTCGAGCAGTCTTTGCCGGCGTCCGTAAGTAGTCTAAAGTTGTGTTGATGCTTGGGGTTAAAGCTAAATCGTCCGCAGAATACGACTCTCATCCCAAT"
    # w = "ACCCGCACGCGCTTTGGTCTAGATTCTAGCTCCAACTTGCCTGCTAGATACTCTGTTAAAAGATGGTTTTACAACCCCCTCCTCTGTCCCTGGGGTATTATATAATACGTCGGATAGTCAGGTACAAATACAAGTGGGTGGGAATACTTTTCCTCGGATCCTAGACCACGGATTACTGCGTGGTTGACAAGAGTCGGCCCGGAGGGAAACGTGAAGGTTAGTGCAATTAAAGTCTCTAATGTGAAGCCTCCGCGAAGCGAGGAGTTTCTGAGATCGAGTACTATTTAGAGTTCGAAATCACGGCTTAACCTCACTGCCACGCATAACTTGCCGGCAATCCAGTTTTGCAACGATACTTAATTTGTGCAGCTCATCTTTGCTGTCCAGAAATAGAGCTAGTCGATCTCATCTTGCGGGTAGCCAGAAGTCCTACCGTCTCCTCCATGTAGCTTAAAAATTTCGGTGAGGATCAAAAATGATAAACGTGACAGGTAAGCTCCTACGTCTATCCTATGACCCCCGCGGCAGAATAGGTTGGTAGTGTTAGTGCGTGAGCTGGTAGAATAGAGCACACTTAGGGAAACGGGAACCGTTATGTAGGGCTGCGACACACAAAAAAGTGTTCGTTGGTAAGCTGCCTCTCCACTAAACAGGATTTCTCTGGATGATCCCATCGAAGCAAGTTACGCACCACGCCGAGGCGGACCCTGGTACTAGCTGCCCCCCCCTTTATGGGGCGCTCGTACATCAAGATGATCGCGGACTCAACCTGATTACGAGTTGTCCAAGTAGTCCAGGGTAAGAGAAACTGGAGAGA"
    # print(longest_common_sequence_v2(v, w))
