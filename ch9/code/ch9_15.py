"""
@BY: Reem Alghamdi
@DATE: 12-11-2020
"""
from copy import deepcopy, copy

from ch9.code.ch9_extra import SuffixTrie, maximal_non_branching_paths


def modified_suffix_trie_construction(text, sep_i=None):
    text_len = len(text)
    trie = SuffixTrie(text)
    for i in range(text_len):
        current_node = trie.root
        for j in range(i, text_len):
            current_symbol = text[j]
            # print(current_symbol)
            node = trie.find_node_connected(current_node, current_symbol)
            if node:
                current_node = node
            else:
                new_node = SuffixTrie.Node(text_len)
                trie.add_node(new_node)
                trie.link(current_node, new_node, current_symbol, j)
                current_node = new_node
        if current_node not in trie.edges:
            current_node.label = i
            if sep_i:
                if i < sep_i:
                    current_node.color = "blue"
                else:
                    current_node.color = "red"

    return trie


def modified_suffix_tree_construction(text, sep_i=None):
    trie = modified_suffix_trie_construction(text, sep_i)
    paths = maximal_non_branching_paths(trie.edges)
    new_edges = {}
    new_nodes = []
    for path in paths:
        a = path[0]
        b = path[-1][0]
        if a not in new_nodes:
            new_nodes.append(a)
        if b not in new_nodes:
            new_nodes.append(b)
        p = path[1][2]
        b.parent = a
        if a in new_edges:
            a.children.append(b)
            new_edges[a].append([b, p, len(path) - 1])
        else:
            a.children = [b]
            new_edges[a] = [[b, p, len(path) - 1]]
    # dfs_shrinkage(trie, None, trie.root, trie.edges[trie.root], [], None, 1)
    # trie.print()
    trie.edges = new_edges
    trie.nodes = new_nodes
    return trie


if __name__ == "__main__":
    # modified_suffix_trie_construction("panamabananas$")

    print(modified_suffix_tree_construction("ATAAATG$").edge_symbols())
    # modified_suffix_tree_construction("panamabananas$")
    # modified_suffix_tree_construction("ATCTACCAGCAGTGAACATGGGAGGACCAGTAAGGAAGGCTTACCCTCGATGTGTTACAGACTCGTTCGTAGGGTGTATAACGCCGCCGCTGG$")
    # t = modified_suffix_tree_construction("TCGAATGGGCAGATAGTAGCCTGAATGACCCGATGGTCGTGTTCCTCGATCCGGGACACCCAGGGTAAGAGGTTCGCACGAGGCATGGAAAAACCTTCACAGAATTAATCCCAGGCCCCTCTTAAGGGACCTCGCCCTACGGGGGAACATGGACCGTAACACGTTTGCTACTAGCAACGACCCGCCTAAATACCATGACCCTCGTTCATACTATAAGCATTTTGGTCCGGTGTGCCTACGAGGTGTCTATTAGCGGTTAGAGGCAGAACGACCCAATTGCGCTTTTCAACGAATCGCTCGCGTCCATGTGGAGCAGAGCCGTCACCGGCAGTCCACTGGCTTAAGGAGTTTCAAGAAGGGACAATGACTCGTTTTTCGATCTGCGATCTAACCTACGATGCAATCGAAGCGGCCTCGGCATGTTTTTTAGCGGGTAAGGAATTGCCGGCTTGTACAAAGGGGGCGACTGTACTGGTCCGTTCTTAATGGAAATACTGCGGTATGACTATTCACGAGTTTCTTAGTCCGCGCCAGAAGGAGTTGGGAATGTTCCGGATACTTCGAGCCGAGTTCCGTCTGCGATCACACAGGACATAATGGACCGGCGATTCATAACGAGAACACCCACCTCAACGAGGCACCAGATGTGGGTGTATCCGAGTGAACTAGGGACCCGAATCTGGCTATAAGAGGTGGCAAGCTGATGGCTACCTATGTTCGGCACTTTGCATCAGTACCCATCCATAAGCGAACTTGCATCGGGCGTCTTTTAACTTCGTGGGGATTGCCTCTTTCGACGGGAGTGAGACTCTTATTTCCTGTTAGTGTATAGTAGCAGCGGGCTACAAGCCTAGGAGCTCACCTGTGTTAGAT$")
    # print("\n".join(t.edge_symbols()))
