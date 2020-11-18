"""
@BY: Reem Alghamdi
@DATE: 08-11-2020
"""


class Trie:
    def __init__(self, root=0):
        self.root = root
        self.nodes = [root]
        self.edges = {}

    def leaves(self):
        return [x for x in self.nodes if x not in self.edges]

    def link(self, a, b, v):
        if a in self.edges:
            self.edges[a].append([b, v])
        else:
            self.nodes.append(a)
            self.edges[a] = [[b, v]]
        if b not in self.nodes:
            self.nodes.append(b)

    def are_linked_by_value(self, a, v):
        if a in self.edges:
            for b, s in self.edges[a]:
                if s == v:
                    return b
        return False

    def are_linked_by_node(self, a, b):
        for end, s in self.edges[a]:
            if b == end:
                return s
        return False

    def path_from_root(self, b):
        for edge in self.edges[self.root]:
            p = self.path(edge, b)
            if len(p) > 0:
                return [self.root] + p

    def path(self, root, b):
        if root[0] == b:
            return [root[0]]
        if root[0] in self.edges:
            for edge in self.edges[root[0]]:
                res = self.path(edge, b)
                if res:
                    return [root[0]] + res
        return []

    def print(self):
        for start, edges in self.edges.items():
            for edge in edges:
                print(str(start) + "->" + str(edge[0]) + ":" + edge[1])


class SuffixTrie:
    class Node:
        def __init__(self, text_len):
            self.text_len = text_len
            self.id = hex(id(self))  # ''.join(random.choice(string.ascii_letters) for x in range(self.text_len))
            self.label = None
            self.parent = None
            self.color = "gray"
            self.children = []

        def add_label(self, label):
            self.label = label

        def __repr__(self):
            r = str(self.id)
            r += " " + str(self.color) + " "
            r += str(self.label) if self.label != None else ""
            return r

    def __init__(self, text):
        self.text_len = len(text)
        self.text = text
        self.root = SuffixTrie.Node(self.text_len)
        self.nodes = [self.root]
        self.edges = {}

    def add_node(self, node):
        self.nodes.append(node)

    def link(self, a, b, symbol, position):
        a.children.append(b)
        b.parent = a
        if a in self.edges:
            self.edges[a].append([b, symbol, position])
        else:
            self.edges[a] = [[b, symbol, position]]

    def find_node_connected(self, node, symbol):
        if node in self.edges:
            for end, s, position in self.edges[node]:
                if symbol == s:
                    return end
        return

    def edge_symbols(self):
        edges = []
        for start, ends in self.edges.items():
            for end, pos, count in ends:
                edges.append(self.text[pos:pos+count])
        return edges

    def print_colors(self):
        for node in self.nodes:
            print(f"{node.label}: {node.color}")

    def lexicographical_sort(self):
        edges = {}
        for start, ends in self.edges.items():
            edges[start] = {}
            for end, pos, count in ends:
                edges[start][end] = self.text[pos:pos+count]
            edges[start] = [(k, v) for k, v in sorted(edges[start].items(), key=lambda x: x[1])]
        return edges

    def print(self):
        for start, ends in self.edges.items():
            for end, symbol, position in ends:
                print(start, (symbol, position), end)


def graph_degrees(graph):
    """
    return pairs, first value is the in-degree, the second is out-degree
    """
    degrees = {}
    for i in graph.keys():
        ends = graph[i]
        out_degree = len(ends)

        if i in degrees:
            degrees[i][1] = out_degree
        else:
            degrees[i] = [0, out_degree]

        for j, _, _ in ends:

            if j in degrees:
                degrees[j][0] += 1
            else:
                degrees[j] = [1, 0]
    return degrees


def maximal_non_branching_paths(adj_list):
    paths = []
    degrees = graph_degrees(adj_list)

    visited = []
    for v in degrees.keys():
        if degrees[v] != [1, 1]:
            if degrees[v][1] > 0:
                visited.append(v)
                try:
                    for w in adj_list[v]:
                        non_branching_path = [v, w]
                        while degrees[w[0]] == [1, 1]:
                            visited.append(w[0])
                            u = adj_list[w[0]][0]
                            non_branching_path.append(u)
                            w = u
                        paths.append(non_branching_path)

                except Exception as e:
                    pass
    return paths

