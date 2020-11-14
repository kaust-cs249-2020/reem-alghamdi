"""
@BY: Reem Alghamdi
@DATE: 10-11-2020
"""
from copy import deepcopy

from ch1.code.ch1_08 import hamming_distance


from ch8.code.ch8_extra import Tree, Node


alphabet = ["A", "C", "G", "T"]


def small_parsimony(t):
    """
    given a tree where the leaves are ONE character from each original tree
    """
    queue = []
    visited = []
    for v in t.nodes:
        if len(v.children) == 0:
            queue.append(v.parent)
            visited.append(v)
            v.s = {}
            for k in alphabet:
                if v.label == k:
                    v.s[k] = 0
                else:
                    v.s[k] = float("inf")
            v.b = {}

    while len(visited) < len(t.nodes):
        v = queue.pop(0)
        while (v in visited and len(queue) > 0) or (not set(v.children).issubset(visited)):
            v = queue.pop(0)
            queue.extend(v.children)
        visited.append(v)
        if v.parent:
            queue.append(v.parent)
        v.s = {}
        for k in alphabet:
            score = 0
            v.b[k] = {}
            for node in v.children:
                minimum = float("inf")
                c_i = 0
                for i in alphabet:
                    if node.s[i] + int(i != k) < minimum:
                        minimum = node.s[i] + int(i != k)
                        c_i = i
                score += minimum
                v.b[k][node] = c_i
            v.s[k] = score
    t.root.label = min(t.root.s, key=t.root.s.get)
    backtrack([], t.root)
    return t


def backtrack(visited, current):
    if current not in visited:
        visited.append(current)
        if not current.label:
           current.label = current.parent.b[current.parent.label][current]
        for n in current.children:
            backtrack(visited, n)


def solve_small_parsimony(string):
    tree, _, _ = format_to_tree(string)
    tree.AdjList(is_string=True)

    o = small_parsimony(tree)
    for node in o.nodes:
        print(node.label, node.index, node.s, node.b)


def solve_full_tree(string):
    tree, m, _ = format_to_tree(string)

    sub_trees = []
    for i in range(m):
        sub_trees.append(deepcopy(tree))
        for node in sub_trees[-1].nodes:
            if node.label:
                node.label = node.label[i]
        small_parsimony(sub_trees[-1])

    final_tree = deepcopy(tree)
    for node in final_tree.nodes:
        node.label = ""
        for i in range(m):
            node.label += [x for x in sub_trees[i].nodes if x.index == node.index][0].label

    total = 0
    for start, w_edges in final_tree.edges.items():
        for edge in w_edges:
            end, weight = edge
            edge[1] = hamming_distance(start.label, end.label)
            total += edge[1]
    print(total // 2)
    final_tree.AdjList(is_string=True)


def format_to_tree(string):
    m = 0
    tree = Tree()
    nodes = {}
    i = 0
    for line in string.split("\n"):
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
            if m == 0:
                m = len(a)
            if a in nodes:
                a = nodes[a]
            else:
                a = Node(i, a)
                i += 1
                nodes[pairs[0]] = a

        if b.isnumeric():
            if b in nodes:
                b = nodes[b]
            else:
                b = Node(b)
                nodes[pairs[1]] = b
        else:
            if m == 0:
                m = len(b)
            if b in nodes:
                b = nodes[b]
            else:
                b = Node(i, b)
                i += 1
                nodes[pairs[1]] = b
        # if not tree.are_linked(a, b):
        a.children.append(b)
        b.parent = a
        tree.link(a, b)
    tree.make_root()
    # print("ROOT ", tree.root)
    # for node in tree.nodes:
    #     print(node.parent, node, node.children)
    # tree.AdjList(is_string=True)
    return tree, m, nodes


if __name__ == "__main__":
    string = """8->C
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
    solve_small_parsimony(string)
    string = """4->CAAATCCC
4->ATTGCGAC
5->CTGCGCTG
5->ATGGACGA
6->4
6->5"""
    solve_full_tree(string)
    # with open("../data/dataset_369355_10.txt") as file:
    #     solve_full_tree(file.read())
    string = """TCGGCCAA->4
4->TCGGCCAA
CCTGGCTG->4
4->CCTGGCTG
CACAGGAT->5
5->CACAGGAT
TGAGTACC->5
5->TGAGTACC
4->5
5->4"""
    solve_full_tree(string)
#     with open("../data/dataset_369355_12.txt") as file:
#         solve_full_tree(file.read())
