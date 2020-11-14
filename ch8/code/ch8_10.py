"""
@BY: Reem Alghamdi
@DATE: 10-11-2020
"""
from copy import deepcopy

from ch8.code.ch8_09 import format_to_tree


def nearest_neighbour_tree(a_, b_, string):
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
    nearest_1, _, nodes_1 = format_to_tree(string)
    a = nodes_1[a_]
    b = nodes_1[b_]
    old_child_a = nearest_1.edges[a].pop(1)
    old_child_b = nearest_1.edges[b].pop(0)
    nearest_1.edges[a].insert(0, old_child_b)
    nearest_1.edges[b].insert(1, old_child_a)
    nearest_1.edges[old_child_a[0]] = [x for x in nearest_1.edges[old_child_a[0]] if x[0] != a] + [[b, 1]]
    nearest_1.edges[old_child_b[0]] = [x for x in nearest_1.edges[old_child_b[0]] if x[0] != b] + [[a, 1]]
    nearest_1.reassign_relationships()

    nearest_2, _, nodes_2 = format_to_tree(string)
    a = nodes_2[a_]
    b = nodes_2[b_]
    old_child_a = nearest_2.edges[a].pop(1)
    old_child_b = nearest_2.edges[b].pop(1)
    nearest_2.edges[a].insert(1, old_child_b)
    nearest_2.edges[b].insert(1, old_child_a)
    nearest_2.edges[old_child_a[0]] = [x for x in nearest_2.edges[old_child_a[0]] if x[0] != a] + [[b, 1]]
    nearest_2.edges[old_child_b[0]] = [x for x in nearest_2.edges[old_child_b[0]] if x[0] != b] + [[a, 1]]
    nearest_2.reassign_relationships()
    return nearest_1, nearest_2


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
#     nn1, nn2 = nearest_neighbour_tree("5", "4", string)
#     nn1.AdjList(is_string=True, is_weighted=False)
#     print()
#     nn2.AdjList(is_string=True, is_weighted=False)

    with open("../data/dataset_369356_6_nn.txt") as file:
        nn1, nn2 = nearest_neighbour_tree("61", "60", file.read())
        nn1.AdjList(is_string=True, is_weighted=False)
        print()
        nn2.AdjList(is_string=True, is_weighted=False)
