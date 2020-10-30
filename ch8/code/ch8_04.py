"""
@BY: Reem Alghamdi
@DATE: 30-10-2020
"""
import numpy as np

from ch8.code.ch8_03 import limb_length, format_matrix
from ch8.code.ch8_extra import Tree


def breadth_first(t, x, i, k):
    # find the two nodes in the path from i to k with cost x to break
    # ex: 0->1:13, make it 0->x:11 and 1->x:2, find 0, 1, 11, and 2

    queue = [[i]]
    visited = set([i])
    actual_path = []
    while len(queue) > 0:
        path = queue.pop()
        node = path[-1]
        visited.add(node)
        if node == k:
            actual_path = path
            break
        for next_node in t.edges[node]:
            if next_node[0] not in visited:
                queue.append(path + [next_node[0]])

    cost = 0
    for k in range(len(actual_path) - 1):
        i, j = actual_path[k], actual_path[k + 1]
        w = [x for x in t.edges[i] if x[0] == j][0][1]
        if cost + w > x:
            return (i, j, x - cost, cost + w - x)
        cost += w


def two_leaves_condition(d, n):
    for i in range(n):
        for k in range(i + 1, n):
            if d[i, k] == d[i, -1] + d[-1, k]:
                return i, k


def additive_phylogeny(inner_start, d):
    n = np.shape(d)[0]
    if n == 2:
        tree = Tree()
        tree.link(0, 1, d[0, 1])
        return tree, inner_start
    # print(d)
    limb = limb_length(n, n - 1, d)
    # print(limb)
    for j in range(n-1):
        d[j, -1] -= limb
        d[-1, j] = d[j, -1]
    # print(d)
    i, k = two_leaves_condition(d, n)
    x = d[i, - 1]
    # print(i, k, x)
    # print(d)
    d = d[:-1, :-1]

    # print(d)
    t, inner_start = additive_phylogeny(inner_start, d)
    # print("t", t.AdjList())
    # reconstruct the tree back!

    # print(t.nodes, t.edges)
    # is_found, path = t.traverse(i, k)
    # print(is_found, path)
    i_near, k_near, i_x, n_x = breadth_first(t, x, i, k)
    v = i_near

    if i_x != 0:
        v = inner_start
        inner_start += 1
        t.link(k_near, v, n_x)
        t.link(i_near, v, i_x)
        t.unlink(i_near, k_near)

    t.link(v, n - 1, limb)
    return t, inner_start


def solve_additive_phylogeny(n, string):
    matrix = format_matrix(n, string)
    # print(matrix)
    additive_phylogeny(n, matrix)[0].AdjList()


if __name__ == "__main__":
#     string = """0	13	21	22
# 13	0	12	13
# 21	12	0	13
# 22	13	13	0"""
#     solve_additive_phylogeny(4, string)

    with open("../data/dataset_369350_6.txt") as file:
        solve_additive_phylogeny(20, file.read())