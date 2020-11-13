"""
@BY: Reem Alghamdi
@DATE: 13-11-2020
"""


class ColoredNode:
    def __init__(self, value, color="gray"):
        self.label = value
        self.color = color
        self.parent = None
        self.children = []

    def __repr__(self):
        return f"{self.label}: {self.color}"


class ColoredTree:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, node):
        self.nodes.append(node)

    def link(self, a, b):
        a.children.append(b)
        b.parent = a
        if a in self.edges:
            self.edges[a].append(b)
        else:
            self.edges[a] = [b]

        if a not in self.nodes:
            self.nodes.append(a)
        if b not in self.nodes:
            self.nodes.append(b)

    def print_colors(self):
        for node in self.nodes:
            print(f"{node.label}: {node.color}")


def format_adj_list_colored(s_adj_list, s_colors):
    adj_list = {}
    colors = {}
    for line in s_adj_list.split("\n"):
        s = line.split(" -> ")
        node = s[0]
        edges = s[1]
        adj_list[node] = []
        colors[node] = "gray"
        if edges != "{}":
            adj_list[node] = edges.split(",")
    for line in s_colors.split("\n"):
        s = line.split(": ")
        node = s[0]
        color = s[1]
        colors[node] = color
    return adj_list_colors_to_colored_tree(adj_list, colors)


def adj_list_colors_to_colored_tree(adj_list, colors):
    tree = ColoredTree()
    nodes = {}
    for start, ends in adj_list.items():
        if start not in nodes:
            nodes[start] = ColoredNode(start, colors[start])
        for end in ends:
            if end not in nodes:
                nodes[end] = ColoredNode(end, colors[end])
            tree.link(nodes[start], nodes[end])
    return tree

"""
    TreeColoring(ColoredTree)
        while ColoredTree has ripe nodes
            for each ripe node v in ColoredTree
                if there exist differently colored children of v
                    Color(v) ← "purple"
                else
                    Color(v) ← color of all children of v
        return ColoredTree"""


def tree_coloring(colored_tree):
    queue = set([node.parent for node in colored_tree.nodes if node.color != "gray"])
    print(queue)
    while queue:
        node = queue.pop()
        children_colors = set([x.color for x in node.children])
        if len(children_colors) == 1:
            node.color = children_colors.pop()
        else:
            node.color = 'purple'
        if node.parent:
            queue.add(node.parent)


if __name__ == "__main__":
#     adj = """0 -> {}
# 1 -> {}
# 2 -> 0,1
# 3 -> {}
# 4 -> {}
# 5 -> 3,2
# 6 -> {}
# 7 -> 4,5,6"""
#     cols = """0: red
# 1: red
# 3: blue
# 4: blue
# 6: red"""
    adj = """0 -> 1,2,3
1 -> 4,5
2 -> 6,7
3 -> 14,15
4 -> 8,9,10
5 -> {}
6 -> 41,42,43
7 -> {}
8 -> {}
9 -> 11,12,13
10 -> {}
11 -> {}
12 -> 28,29
13 -> 16,17
14 -> {}
15 -> 47,48
16 -> 18,19
17 -> 25,26,27
18 -> {}
19 -> 20,21,22
20 -> 23,24
21 -> 30,31,32
22 -> {}
23 -> {}
24 -> 44,45,46
25 -> 39,40
26 -> {}
27 -> {}
28 -> {}
29 -> 35,36
30 -> 33,34
31 -> {}
32 -> 37,38
33 -> {}
34 -> {}
35 -> {}
36 -> {}
37 -> {}
38 -> {}
39 -> {}
40 -> {}
41 -> {}
42 -> {}
43 -> {}
44 -> {}
45 -> {}
46 -> {}
47 -> {}
48 -> {}"""
    cols = """5: red
7: red
8: red
10: blue
11: blue
14: red
18: blue
22: blue
23: red
26: red
27: blue
28: blue
31: blue
33: red
34: red
35: blue
36: blue
37: red
38: red
39: red
40: blue
41: blue
42: blue
43: blue
44: blue
45: red
46: red
47: red
48: red"""
    tree = format_adj_list_colored(adj, cols)
    # tree.print_colors()
    tree_coloring(tree)
    tree.print_colors()
