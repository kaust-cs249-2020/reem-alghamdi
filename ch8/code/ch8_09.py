"""
@BY: Reem Alghamdi
@DATE: 31-10-2020
"""
from copy import deepcopy

from ch1.code.ch1_08 import hamming_distance
from ch3.code.ch3_08 import format_adjacency_list
import pandas as pd
import numpy as np

from ch8.code.ch8_extra import Tree, Node

alphabet = ["A", "C", "G", "T"]


def small_parsimony(t):
    """
    given a tree where the leaves are ONE character from each original tree

    """
    visited = []
    s = {}
    for v in t.nodes:
        if len(t.edges[v]) == 1:
            visited.append(v)
            s[v] = {}
            for k in alphabet:
                if v.label == k:
                    s[v][k] = 0
                else:
                    s[v][k] = float("inf")
            v.s = s[v]
    while len(visited) < len(t.nodes):
        for v in [x for x in t.nodes if x not in visited][:]:
            children = []
            for edge in t.edges[v]:
                node = edge[0]
                if node in visited:
                    children.append(node)

            if len(children) < 2:
                continue
            visited.append(v)
            s[v] = {}
            for k in alphabet:
                score = 0
                for node in children:
                    scores = []
                    for i in alphabet:
                        scores.append(s[node][i] + int(i != k))
                    score += min(scores)
                s[v][k] = score
            v.s = s[v]
            v.label = min(v.s, key=v.s.get)

    return t


def solve_small_parsimony(n, string):
    """
    node = (#, label)
    (start, end, weight)
    """
    tree = Tree()
    nodes = {}
    for i, line in enumerate(string.split("\n")):
        pairs = line.split("->")
        a = pairs[0]
        b = pairs[1]
        if a.isnumeric():
            if a in nodes:
                a = nodes[a]
            else:
                a = Node(a)
                nodes[pairs[0]] = a
        else:
            a = Node(i, a)

        if b.isnumeric():
            if b in nodes:
                b = nodes[b]
            else:
                b = Node(b)
                nodes[pairs[1]] = b
        else:
            b = Node(i, b)

        tree.link(a, b)

    tree.AdjList(is_string=True)

    o = small_parsimony(tree)
    for node in o.nodes:
        print(node.label, node.index, node.s)


if __name__ == "__main__":
#     string = """4->CAAATCCC
# 4->ATTGCGAC
# 5->CTGCGCTG
# 5->ATGGACGA
# 6->4
# 6->5"""
#     solve_small_parsimony(4, string)
    string ="""8->C
8->C
9->A
9->C
10->G
10->G
11->T
11->C
12->8
12->9
13->10
13->11
14->12
14->13"""
    solve_small_parsimony(8, string)
