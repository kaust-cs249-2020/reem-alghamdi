"""
@BY: Reem Alghamdi
@DATE: 30-10-2020
"""
import numpy as np

from ch8.code.ch8_03 import limb_length, format_matrix
from ch8.code.ch8_extra import Tree


def two_leaves_condition(d, n):
    for i in range(n):
        for k in range(i + 1, n):
            if d[i, k] == d[i, -1] + d[-1, k]:
                return i, k


def additive_phylogeny(inner_start, d, limbs):
    n = np.shape(d)[0]
    if n == 2:
        tree = Tree()
        tree.link(0, inner_start, limbs[0])
        tree.link(1, inner_start, limbs[1])
        return tree
    # print(d)
    limb = limbs[n - 1]
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
    t = additive_phylogeny(inner_start, d, limbs)
    # print("t", t.AdjList())
    # reconstruct the tree back!

    # print(t.nodes, t.edges)
    is_found, path = t.traverse(i, k)
    v = inner_start
    if not is_found:
        w = x - t.edges[i][0][1]
        v += 1
        t.link(t.edges[i][0][0], v, w)
        t.link(v, k, limb)
    else:
        # print(path)
        sum = 0
        for pair in path:
            sum += pair[1]
            if sum == x:
                v = pair[0]
        t.link(v, n - 1, limb)
    return t


def solve_additive_phylogeny(n, string):
    matrix = format_matrix(n, string)
    # print(matrix)
    limb = []
    for i in range(n):
        limb.append(limb_length(n, i, matrix))
    additive_phylogeny(n, matrix, limb).AdjList()


if __name__ == "__main__":
    string = """0	13	21	22
13	0	12	13
21	12	0	13
22	13	13	0"""
    solve_additive_phylogeny(4, string)

    # with open("../data/dataset_369350_6.txt") as file:
    #     solve_additive_phylogeny(27, file.read())