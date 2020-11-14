"""
@BY: Reem Alghamdi
@DATE: 10-11-2020
"""
from copy import deepcopy

from ch8.code.ch8_09 import format_to_tree, solve_full_tree


def a_neighbour(a_, b_, tree, pa, pb):
    nearest = deepcopy(tree)
    # nearest.AdjList(is_string=True, is_weighted=False)
    a = [x for x in nearest.nodes if x.index == a_.index][0]
    b = [x for x in nearest.nodes if x.index == b_.index][0]
    # print(a, b)
    # print(nearest.edges[a], nearest.edges[b])
    old_child_a = [x for x in nearest.edges[a] if x[0] != b][pa]
    old_child_b = [x for x in nearest.edges[b] if x[0] != a][pb]
    nearest.edges[a].remove(old_child_a)
    nearest.edges[b].remove(old_child_b)
    # print(old_child_a, old_child_b)
    # print(nearest.edges[a], nearest.edges[b])
    # print(nearest.edges[old_child_a[0]], nearest.edges[old_child_b[0]])
    nearest.edges[a].insert(pa, old_child_b)
    nearest.edges[b].insert(pb, old_child_a)
    nearest.edges[old_child_a[0]] = [x for x in nearest.edges[old_child_a[0]] if x[0] != a] + [[b, 1]]
    nearest.edges[old_child_b[0]] = [x for x in nearest.edges[old_child_b[0]] if x[0] != b] + [[a, 1]]
    # print(nearest.edges[a], nearest.edges[b])
    # print(nearest.edges[old_child_a[0]], nearest.edges[old_child_b[0]])
    # nearest.AdjList(is_string=True, is_weighted=False)
    return nearest


def nearest_neighbour_tree(a_, b_, tree):
    """
    5: 2, 3, 4
    4: 0, 1, 5
    after 1: 5(1) <-> 4(0)
    5: 0, 2, 4
    4: 1, 3, 5
    after 2: 5(1) <-> 4(1)
    5: 1, 2, 4
    4: 0, 3, 5
    """
    nn1 = a_neighbour(a_, b_, tree, 1, 0)
    nn2 = a_neighbour(a_, b_, tree, 1, 1)
    return nn1, nn2


def nearest_neighbour_interchange(string):
    tree, m, nodes = format_to_tree(string)
    score = float("inf")
    tree.make_root()
    new_tree, new_score = solve_full_tree(tree, m)
    new_tree.unroot()
    while new_score < score:
        score = new_score
        tree = new_tree
        print(str(score) + "\n" + tree.AdjList(is_string=True, to_print=False))
        print()
        for start, edges in tree.edges.items():
            for end in start.children:
                if len(end.children) > 0:
                    for nn in nearest_neighbour_tree(start, end, tree):
                        nn.make_root()
                        nn, scr = solve_full_tree(nn, m)
                        nn.unroot()

                        if scr < new_score:
                            new_score = scr
                            new_tree = nn

    return new_tree


def solve_nn(a, b, input):
    tree, _, nodes = format_to_tree(input)
    # tree.AdjList(is_string=True, is_weighted=False)
    nn1, nn2 = nearest_neighbour_tree(nodes[a], nodes[b], tree)
    nn1.AdjList(is_weighted=False, is_string=True)
    print()
    nn2.AdjList(is_weighted=False, is_string=True)


if __name__ == "__main__":
#     string = """0->4
# 4->0
# 1->4
# 4->1
# 2->5
# 5->2
# 3->5
# 5->3
# 4->5
# 5->4"""
    # solve_nn("5", "4", string)
    # with open("../data/dataset_369356_6_nn.txt") as file:
    #     solve_nn("60", "61", file.read())
#     string = """GCAGGGTA->5
# TTTACGCG->5
# CGACCTGA->6
# GATTCCAC->6
# 5->TTTACGCG
# 5->GCAGGGTA
# 5->7
# TCCGTAGT->7
# 7->5
# 7->6
# 7->TCCGTAGT
# 6->GATTCCAC
# 6->CGACCTGA
# 6->7"""
#     tree = nearest_neighbour_interchange(string)

    # with open("../data/dataset_369356_8_nn2.txt") as file:
    #     tree = nearest_neighbour_interchange(file.read())
    with open("../data/dataset_369356_8(1).txt") as file:
        tree = nearest_neighbour_interchange(file.read())
