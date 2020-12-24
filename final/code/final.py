"""
@BY: Reem Alghamdi
@DATE: 07-12-2020
"""
from ch10.code.ch10_05 import format_to_df, probability_of_emission_given_path
from ch10.code.ch10_06 import viterbi_decoding
from ch8.code.ch8_09 import format_to_tree
from ch8.code.ch8_extra import Tree, Node
from ch9.code.ch9_15 import modified_suffix_tree_construction
from ch9.code.ch9_extra import SuffixTrie


def equal_children(children1, children2):
    l1 = set()
    l2 = set()
    for c1 in children1:
        l1.add(c1.label)
    for c2 in children2:
        l2.add(c2.label)
    return l1 == l2


def depth_first_equal_children(visited, node1, node2):
    if node1 not in visited and node2 not in visited:
        visited.add(node1)
        visited.add(node2)
        if node1.label == node2.label:
            if equal_children(node1.children, node2.children):
                for child1, child2 in zip(sorted(node1.children), sorted(node2.children)):
                    return depth_first_equal_children(visited, child1, child2)
            else:
                return False
        else:
            return False
    return True


def are_isomorphic(tree1, tree2):
    # Check in the two trees are equal in node count
    if len(tree1.nodes) != len(tree2.nodes):
        return False
    else:
        return depth_first_equal_children(set(), tree1.root, tree2.root)


if __name__ == "__main__":
    # with open("../data/hmm1") as tr:
    #     with open("../data/hmm2") as em:
    #         # print(viterbi_decoding("HHTT", "H T".split(), "A B".split(), format_to_df(em), format_to_df(tr)))
    #         print(viterbi_decoding("HTTH", "H T".split(), "A B".split(), format_to_df(em), format_to_df(tr)))
