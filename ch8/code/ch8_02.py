"""
@BY: Reem Alghamdi
@DATE: 30-10-2020
"""
from ch3.code.ch3_10 import graph_degrees
from ch5.code.ch5_08_2 import format_weighted_adjacency_list
from ch5.code.ch5_17 import topological_ordering
import numpy as np


def depth_first(adj_list, weights, leaves, current, next_node, visited, cost, paths):
    if next_node not in visited:
        visited.append(next_node)
        cost[(current, next_node)] = weights[(current, next_node)]
        if next_node in leaves:
            paths.append((next_node, visited.copy()[1:], sum(cost.values())))
        for n in adj_list[next_node]:
            depth_first(adj_list, weights, leaves, next_node, n, visited, cost, paths)
        visited.remove(next_node)
        cost[(current, next_node)] = 0
    return sorted(paths)


def distance_between_leaves(n, adj_list, weights):
    paths = {}  # {0: {2: [(4, 11), (5, 4), (2, 6)], 1:[]}, 1: [], 2: [], 3: []}
    d = np.zeros((n,n), dtype=int)
    degrees = graph_degrees(adj_list)
    # print(degrees)
    leaves = sorted([k for k, v in degrees.items() if v == [1, 1]])
    # print(leaves)
    for i, leaf in enumerate(leaves):  # first: 0->[1, 2, 3], 1->[2, 3]
        visited = leaves[0: i + 1]
        leaf_paths = depth_first(adj_list, weights, leaves, leaf, adj_list[leaf][0], visited, {}, [])
        paths[leaf] = [(leaf, [], 0)] + leaf_paths
        for path in paths[leaf]:
            d[int(leaf), int(path[0])] = int(path[2])
            d[int(path[0]), int(leaf)] = int(path[2])

    # print(paths)
    return d, paths


if __name__ == "__main__":
#     adj_list, weights = format_weighted_adjacency_list(
#         """0->4:11
# 1->4:2
# 2->5:6
# 3->5:7
# 4->0:11
# 4->1:2
# 4->5:4
# 5->4:4
# 5->3:7
# 5->2:6"""
#     )
    # print(adj_list)
    # print(weights)
    # d = distance_between_leaves(4, adj_list, weights)[0]
    # for line in d:
    #     print('\t'.join(map(str, line)))

    with open("../data/dataset_369348_12.txt") as file:
        adj_list, weights = format_weighted_adjacency_list(file.read())
        d = distance_between_leaves(32, adj_list, weights)[0]
        for line in d:
            print('\t'.join(map(str, line)))
