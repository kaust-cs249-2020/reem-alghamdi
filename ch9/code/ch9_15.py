"""
@BY: Reem Alghamdi
@DATE: 12-11-2020
"""
from copy import deepcopy, copy

from ch9.code.ch9_extra import SuffixTrie, maximal_non_branching_paths

"""
ModifiedSuffixTreeConstruction(Text)
    Trie ← ModifiedSuffixTrieConstruction
    for each non-branching path Path in Trie
        substitute Path by a single edge e connecting the first and last nodes of Path
        Position(e) ← Position(first edge of Path)
        Length(e) ← number of edges of Path
    return Trie
"""


def modified_suffix_trie_construction(text):
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
    return trie


def dfs_shrinkage(trie, parent, node, edges, visited, pos, count):
    if node not in visited:
        visited.append(node)
        if len(edges) == 1:
            b = edges[0][0]
            trie.edges[parent] = [x for x in trie.edges[parent] if x[0] != node]
            count += 1
            if b in trie.edges:
                dfs_shrinkage(trie, parent, b, trie.edges[b], visited, pos, count)
                del trie.edges[node]
                trie.nodes.remove(node)
            else:
                trie.edges[node] = [x for x in trie.edges[node] if x[0] != b]
                trie.edges[parent].append([b, pos, count])

        else:
            if count > 1:
                trie.nodes.append(node)
                trie.edges[node] = edges
                trie.edges[parent].append([node, pos, count])
                count = 1
            for b, s, p in trie.edges[node]:
                if b in trie.edges:
                    dfs_shrinkage(trie, node, b, trie.edges[b], visited, p, count)

            for i, x in enumerate(trie.edges[node]):
                if not str(x[1]).isnumeric():
                    trie.edges[node][i] = [x[0], x[2], 1]


def modified_suffix_tree_construction(text):
    trie = modified_suffix_trie_construction(text)
    paths = maximal_non_branching_paths(trie.edges)
    new_edges = {}
    new_nodes = []
    for path in paths:
        a = path[0]
        b = path[-1][0]
        new_nodes.append(a)
        new_nodes.append(b)
        p = path[1][2]
        if a in new_edges:
            new_edges[a].append([b, p, len(path) - 1])
        else:
            new_edges[a] = [[b, p, len(path) - 1]]
    # dfs_shrinkage(trie, None, trie.root, trie.edges[trie.root], [], None, 1)
    # trie.print()
    # print()
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
