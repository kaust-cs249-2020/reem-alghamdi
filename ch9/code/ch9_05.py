"""
@BY: Reem Alghamdi
@DATE: 13-11-2020
"""
from ch9.code.ch9_15 import modified_suffix_tree_construction
from ch9.code.ch9_16 import tree_coloring


def repeat_depth_first(trie, text, b, pos, count, visited, string, paths):
    if b not in visited:
        visited.append(b)
        if b in trie.edges:  # not leaf node
            string += text[pos:pos + count]
            for n, p, c in trie.edges[b]:
                repeat_depth_first(trie, text, n, p, c, visited, string, paths)
        else:
            paths.append(string)
    return sorted(paths, key=len, reverse=True)


def longest_repeat_problem(text):
    text += "$"
    trie = modified_suffix_tree_construction(text)
    return repeat_depth_first(trie, text, trie.root, 0, 0, [], "", [])[0]


def colored_shared_depth_first(trie, text, b, pos, count, visited, string, paths):
    if b not in visited:
        visited.append(b)
        if b in trie.edges:
            # print(b)
            for n, p, c in trie.edges[b]:
                if n.color in ["purple", "blue"]:
                    colored_shared_depth_first(trie, text, n, pos, count, visited, string, paths)
        elif b.color == "blue":
            # print(b)
            string = text[pos:pos + count]
            paths.append(string)
    return sorted(paths, key=len, reverse=True)


def longest_shared_substring(text1, text2):
    combo = text1 + "#" + text2 + "$"
    colored_tree = modified_suffix_tree_construction(combo, len(text1) + 1)
    tree_coloring(colored_tree)
    return colored_shared_depth_first(colored_tree, combo, colored_tree.root, 0, 0, [], "", [])[0]


def colored_non_shared_breadth_first(trie, text, a):
    # maintain a queue of paths
    # push the first path into the queue
    queue = [(a, "")]
    visited = set()
    paths = []
    while queue:
        vertex, path = queue.pop(0)
        visited.add(vertex)
        for node, pos, count in trie.edges.get(vertex, []):
            if node.color == "blue" and text[pos:pos + 1] != "#":

                paths.append(path + text[pos:pos + 1])
            if node.color in ["purple", "blue"]:
                if node not in visited:
                    visited.add(node)
                    queue.append((node, path + text[pos:pos + count]))
    return sorted(paths, key=len)


def shortest_non_shared_substring(text1, text2):
    combo = text1 + "#" + text2 + "$"
    colored_tree = modified_suffix_tree_construction(combo, len(text1) + 1)
    tree_coloring(colored_tree)
    # colored_tree.print_colors()
    # colored_tree.print()
    return colored_non_shared_breadth_first(colored_tree, combo, colored_tree.root)[0]


if __name__ == "__main__":
    # print(longest_repeat_problem("ATATCGTTTTATCGTT"))
    # print(longest_repeat_problem("ABABABA"))
    # print(longest_repeat_problem("ATCGATCGA"))
    # # print(longest_repeat_problem("AATTTCCGACTTGCATGACGAGTCAGCGTTCCATCTGATCGAGTCTCCGAAGAACAAATACCCCTACTCAGTTGTGAGCCCCTTTACCGTGAGGACAGGGTCCTTGATGTCGTCTCCTAATTTGCGTTGCGGCTCAACATGTTGTACATAGTGGGGCCAGCCCCAGGGATTTTGTAATTTCTACACTCCATATACGGGACAAGGGTGAGCATTTCCGGGCTTGGATAGGGGCTGCAAGAAAATATCTGGACGTAAGAACTTAATGCCATTCCTACATCCTCGATACCTCGTCTGTCAGAGCAATGAGCTGGTTAGAGGACAGTATTGGTCGGTCATCCTCAGATTGGGGACACATCCGTCTCTATGTGCGTTCCGTTGCCTTGTGCTGACCTTGTCGAACGTACCCCATCTTCGAGCCGCACGCTCGACCAGCTAGGTCCCAGCAGTGGCCTGATAGAAAAATTACCTACGGGCCTCCCAATCGTCCTCCCAGGGTGTCGAACTCTCAAAATTCCCGCATGGTCGTGCTTCCGTACGAATTATGCAAACTCCAGAACCCGGATCTATTCCACGCTCAACGAGTCCTTCACGCTTGGTAGAATTTCATGCTCGTCTTTTGTATCCGTGTAAGTAGGAGGCCGCTGTACGGGTATCCCAGCCTTCGCGCTCTGCTGCAGGGACGTTAACACTCCGAACTTTCCATATACGGGACAAGGGTGAGCATTTCCGGGCTTGGATAGGGGCTGCAAGAAAATATCTGGACGTAAGAAGCTCTGAGGGATCCTCACGGAGTTAGATTTATTTTCCATATACGGGACAAGGGTGAGCATTTCCGGGCTTGGATAGGGGCTGCAAGAAAATATCTGGACGTAAGAAGAGTGATGTTTGGAATGCCAACTTCCATGCACGCCAATTGAGCAATCAGGAGAATCGAGTGCTGTTGACCTAGACCTTGTCAGAAGTATGAATTAACCGCGCGTGTAGGTTTGTCGCTCGACCTGCAAGGGTGCACAATCTGGACTGTCGTCGGCGAACGCTTTCATACGCCTACAAACCGCGTTGCTGGTCGAATCGATCTCACCACCGGCCTTGCAGGATTCTAATTATTCTCTCTCGGTGAGACTGCCGGCGGTCCATGGGTCTGTGTTTCGCTTCAAGCAGTGATATACTGGCGTTTTGTGACACATGGCCACGCACGCCTCTCGTTACTCCCAAT"))
    # print(longest_repeat_problem("ATGACATACATGATGCTATTGGTGGCTTAACCTTGCGGTCCTACCCACCCGAAACAAGGTATAGGCAGAACGGGTTTTATTCCGAACATGTATATGCCCCCTTGCCTATAATATTATGGAACGCCTCGGTAAGGCCCGTCAGGGGAAAGGAGTATGCATGCTGCTATATGCCGTAAGGTTCGCCTCTTATGAACTACTAATCGACACCCGTTTCGAGTTACTTGGGTGCCGCGCATGCGCAAATGTGCAGTCCGTACAGATGATTGGACTACAAGGGCCGGTTGAACAGACCGGACAGGACTTTGCTGCATCGGCAGCGGCCGACCTAGTACTGATAAATTGAAGTTTTAAATGAGGGAGCAAGATTGGTGGCTTAACCTTGCGGTCCTACCCACCCGAAACAAGGTATAGGCAGAACGGGTTTTATTCCGAACATGTATATGCCCCCTTGGCTGTTGGTGGCTTAACCTTGCGGTCCTACCCACCCGAAACAAGGTATAGGCAGAACGGGTTTTATTCCGAACATGTATATGCCCCCTTGGTTAAAGGGCTAGGGGGTGCCGATATCAGGTGGCCCATCGCCGCAATTCCTACCTGACGGTCGAAAGGGTCGAGGAAGGTGCCGAACAGGAATTTGCCTGCTGTAGCAGTGCAGGCGTATGAAAAACGATTTTTTAACGGGAGGGCCTCCCAACTGAATGAACTAATGATTTTCATGCGTGAAGAAAGCGTTAGGGAATGGAATTTTTGGGGAGAGTTCTTTACGGATCTGCGATCCAATTTGGGGTTATCACTAATACCTTTAAACCGATCAGTGCTATTCCCCATTATTGCCCCGTGCGGACTATATAGTAGCCCCGTCGATCGGCTGGCACGCGTGTTAGGGGTCGAGCTGGCCTTCTGTTCCCCGGGCTGACCGCGTGTTTGCGTAGCTGAAGGTCGACTTTTGCGACGCACTCGCGTAAGCCTGATTAAACACTTATTCAGGTCACTGCCATTCTGGAGGGACAACCGCTGTCGGTTCGCGGTTATCCATTGATGGCATAAACCATCCTCCACTTAGCTCAACACTAGGTACCGGGCTGGCAGCAGGCAGCAAGACCCAGTATTTTCGCGCCCTTTTTGGGATTATACGTACCGGATGGACGCGTACCATGGCCCGGATGCCGTAGTACCATTAGTGATCTTACGCTCTTTTGAAGCCGCGAATGATTACGGAAGAAGGTATATGGAGCCGGACGTTCGGCCTTTGCGTGAA"))

    # print(longest_shared_substring("panama", "bananas"))
    # print(longest_shared_substring("TCGGTAGATTGCGCCCACTC", "AGGGGCTCGCAGTGTAAGAA"))
    # t1 = "GCAGCTCGTCTAAGAGGGCAAATTTGTACGTATTTTTTACCAATTTCCAGGCGCAGCGTTGAAGTTCCAGCTCCTTTATATACGCACAGCCCCGGCACTTAGAGGCAGGACTGGCGCGGATGTCTCGTAAGCTCGGCTCCTCACGTCACGGATATAGCCTCTACGTAATTATCTCTGGATGGCTAAGTAAGAGCAACCATTACAGCTGGTACCATTGAACGACTGCCGGTTCCGCAAGACTCAAACATCCGGGCGGAGGCAACCCGATGGTCGTTTCTGATCGTGAAATGACCGCGTGTTTAGTACTGTACCCTTAACTGTAGAGTTGGGACCTCTAAGGTCGCGACTGTTTGCTTATAGACTAGGATCGCAACATAAACTATCACCCGAGTGAAAGCCGATCCCCAGACAGATTATTTACAATTTTAGCATCCTGACCTGGGCGAATAAGGAACTCCCCTAGTGTTTTACAGCCTCGCTCCGTACGTGCTCCGGTTCTGCAACACCTTCTAGCAGCATATCTAGTGCACACTAGGCAATAATTGAAAACTATAGATGCTGGTTTACAGGGATCCTAAGCGTGTAAGTAGCAAACGACCCGGAGATCTCATCCTTGAAGGGTCAACTAATCAGCTAAAAGTGTCGAACATGGTCTGCAAAAGTGTCAATGTGAGGATTGGAAGCTCTTAAATGTATTTCAACCCATAAGAATCTGACGTAATCCTTGCGAAGCTCGCAGTCAAGAGGGCGTCACAAACGTTGACGAATCTTGCTGCTTGGCCCATACTTCTGCACTTTGCGAATCATCGTTTATTACGCCTCTTCTGACATGGGTAAGGTCTTAACTTTGGGCCTCGTACGCCCAACCCACCCTTTGACCGCATATGACGTCAAACACGGGGTAAAAGGTATTTCGCACAGTGTGAGTGTTATACCATAATGCAGGTCGCAAGGATCTAGTTCTACCGCATAACTGGAATAAAAAATTACACCCTAAATA"
    # t2 = "CCACGCGCCAGAGCCTAGGAGGGCCGACTACAACGAATTATTCACTCAGACGTAGGAGTTACCCGTATGAGCTGGCTATGGGTCATGGGTCAAAATAGCCCGCTGTGACAGTTCACGAGAGTAACAAGGTACGTAATTCGCTGCTAAACATAAATAAGCCATGTGGCGTCAAGCTCCATAATCCAACGCGCGCCGGTCGACGGAGCATTACTCCTTGCCGCAAAAAGCTTTCGTGCGCAGAGGTGTTGATACTTCTTAAGATCATATTCTATGTGCTGGCACGGTGAGTGCAGATTCGATACGGAAGAACAGGCAGCATCCGGAGAGAGAGAAGATAAGTTTCGCAAAGGGTACCCTTGATAACCATATTTAATGTTACCAGGCGGTGTACTAATTTCCGTGGCCGGTCGAAGCTTGCTGAACCTATGACTCCGCCCCGTTCATTTCGGTGGGCTGTGTAACGCTAATACTATCTATGACTAGTAATACTTTCTAGTCTCCTCTAGGCGTGCTCAGTATGCTGGCCGTGAGAGTAGCTCACCTCTTACCCTTATGTATTATTTATTAATGCGCCTTAATGCGTAATTCTCAGTCGTCCAACCCATCTCAAGCACTAGACAAAAAGGAAGGGTGAATCTAGTGCCAACGCACGCGCAAGATGACAGTGCCAGCAAGCAGAAGAATATGTTCGATTAGGATTACTTGGCACCCGGCACTCGGCTGTTGTCGTAATGATACGTCGTGTAGTATCGTATCCTGTAAACACAAGGGAATTCGACAATAAAGTCTACAAGCACTTGATCTGATCGGGACAGACCTTAAGTACACCAGCCTGTGGCAATGCGTTCTCTACAATACACTAGTACAGGATATCGCAGGCGACCACAAGGTCGTGATTAGTATGCTAGACTAGCACCCATATGCAGTTTCCACTTCTCTCCTGTTAACACAAGCTTTGTGGGAAATTCTGCTGCTTAAAACTATCAAGAGAGATGAGATC"
    # print(longest_shared_substring(t1, t2))

    # print(shortest_non_shared_substring("panama", "bananas"))
    # print(shortest_non_shared_substring("CCAAGCTGCTAGAGG", "CATGCTGGGCTGGCT"))
    print(shortest_non_shared_substring("AAAATAAACAAAGAATTAATCAATGAACTAACCAACGAAGTAAGCAAGGATATACATAGATTTATTCATTGATCTATCCATCGATGTATGCATGGACACAGACTTACTCACTGACCTACCCACCGACGTACGCACGGAGAGTTAGTCAGTGAGCTAGCCAGCGAGGTAGGCAGGGTTTTCTTTGTTCCTTCGTTGCTTGGTCTCTGTCCCTCCGTCGCTCGGTGTGCCTGCGTGGCTGGGCCCCGCCGGCGCGGGGAAAGCGGCGGAACATGGTATAGGGAATATTTACCGAGCGTAACAGACCAAGTGTCTCAGAAAAACCCTAGTTATTTGTCACTCGCCAAGCGCGACCACACTGGGAATGGGATTTACAGTGCCGCCAAGGGTTTACTGCACAGAAAATAGCAAGTAGATGCTGATGATTACCACAATGTGTAGACGGAATATCTACACTACTCCGTCCAATTCGGTGTCAAGAACCGGTCACCATTTCTACGGTGCCCTCGTATCCGTTCAGGGCTTGGGCAGCAAAGCTTCTTGAGAAACAATGTGTTCGTGTTCTGTCGAAGTAGTTCGCTGGGTCAAGTGGTTGTTATGGAGACAGGACCCATAAGTCAAGGGATCTACAAATAGATACAGTGGAAGGACGGAGTGTTAGT", "AAAATAAACAAAGAATTAATCAATGAACTAACCAACGAAGTAAGCAAGGATATACATAGATTTATTCATTGATCTATCCATCGATGTATGCATGGACACAGACTTACTCACTGACCTACCCACCGACGTACGCACGGAGAGTTAGTCAGTGAGCTAGCCAGCGAGGTAGGCAGGGTTTTCTTTGTTCCTTCGTTGCTTGGTCTCTGTCCCTCCGTCGCTCGGTGTGCCTGCGTGGCTGGGCCCCGCCGGCGCGGGGAAA"))