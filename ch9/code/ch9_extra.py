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
