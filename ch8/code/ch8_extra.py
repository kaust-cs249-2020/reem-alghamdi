"""
@BY: Reem Alghamdi
@DATE: 30-10-2020
"""
from random import choice


class Node:
    def __init__(self, val, label=None):
        self.index = val
        self.label = label
        self.parent = None
        self.children = []
        self.s = {}
        self.b = {}

    def __str__(self):
        return self.label if self.label else self.index

    def __repr__(self):
        return self.index if not self.label else str((self.index, self.label))

    def __lt__(self, other):
        return (self.label if self.label else self.index) < \
               (other.label if other.label else other.index)


class Tree:
    def reassign_depth_first(self, parent, node, visited):
        if node not in visited:
            visited.append(node)
            # print(node.parent, node, node.children)
            if node in self.edges:  # not leaf node
                node.children = [x[0] for x in self.edges[node] if x[0] != parent]
                self.edges[node] = [x for x in self.edges[node] if x[0] != parent]
                if len(self.edges[node]) == 0:
                    del self.edges[node]
                node.parent = parent
                for child in node.children:
                    self.reassign_depth_first(node, child, visited)
            else:
                node.parent = parent

    def reassign_relationships(self):
        self.reassign_depth_first(None, self.root, [])

    def make_root(self):
        self.root = None
        temp = None
        for node in self.nodes:
            if not temp and node in self.edges and len(self.edges[node]) > 2:
                temp = node
            if not node.parent:
                self.root = node
        if not self.root:
            self.root = temp
        self.reassign_relationships()
        # print()
        # for node in self.nodes:
        #     print(node.parent, node, node.children, self.edges.get(node))

    def __init__(self, bidirectional=True):
        self.root = None
        self.nodes = []
        self.edges = {}
        self.bidirectional = bidirectional

    def link(self, start, end, weight=1):
        self.half_link(start, end, weight)
        if self.bidirectional:
            self.half_link(end, start, weight)

    def unlink(self, i, k):
        try:
            self.half_unlink(i, k)
            if self.bidirectional:
                self.half_unlink(k, i)
        except KeyError:
            print('Could not unlink {0} from {1}'.format(i, k))
            self.print()

    def half_link(self, a, b, weight=1):

        if a not in self.nodes:
            self.nodes.append(a)
        if b not in self.nodes:
            self.nodes.append(b)
        if a in self.edges:
            self.edges[a] = [[b0, w0] for [b0, w0] in self.edges[a] if b0 != b] + [[b, weight]]
        else:
            self.edges[a] = [[b, weight]]

    def half_unlink(self, a, b):
        links = [[e, w] for [e, w] in self.edges[a] if e != b]
        if len(links) < len(self.edges[a]):
            self.edges[a] = links
        else:
            print('Could not unlink {0} from {1}'.format(a, b))
            self.print()

    def are_linked(self, a, b):
        a_b = []
        if a in self.edges:
            a_b += [e for e in self.edges.get(a) if e[0] == b]
        if b in self.edges:
            a_b += [e for e in self.edges.get(b) if e[0] == a]
        return len(a_b) > 0

    def edges_string(self):
        string = []
        for start, edges in self.edges.items():
            for end, weight in edges:
                string.append(f"{start.label if start.label else start.index}->{end.label if end.label else end.index}")
        return string

    def unroot(self):
        for node in self.nodes:
            if node not in self.edges:
                self.edges[node] = []
        for start, edges in self.edges.items():
            for end, w in edges:
                if [start, w] not in self.edges[end]:
                    self.edges[end].append([start, w])




    def AdjList(self, includeNodes=False, is_float=False, is_string=False, is_weighted=True):
        self.nodes.sort()
        if includeNodes:
            print(self.nodes)
        for node in self.nodes:
            if node in self.edges:
                for edge in self.edges[node]:
                    end, weight = edge
                    string = '%s->%s' if is_string else '%i->%i'
                    if is_weighted:
                        string += ':'
                    if is_float:
                        string += '%.3f'
                    if is_weighted:
                        string += '%d'
                        print(string % (node, end, weight))
                    else:
                        print(string % (node, end))

    def num_nodes(self):
        return len(self.nodes)

    def traverse(self, i, k, path=[], weights=[]):
        # if not i in self.edges: return (False, [])
        if len(path) == 0:
            path = [i]
            weights = [0]

        for j, w in self.edges[i]:
            print(j, w)
            if j in path: continue
            path1 = path + [j]
            weights1 = weights + [w]
            if j == k:
                return (True, list(zip(path1, weights1)))
            else:
                found_k, test = self.traverse(j, k, path1, weights1)
                return (found_k, test)
        return (False, list(zip(path, weights)))

    def get_nodes(self):
        for node in self.nodes:
            yield (node)

    def initialize_from(self, T):
        for node in T.nodes:
            if not node in self.nodes:
                self.nodes.append(node)
                if node in T.edges:
                    for a, w in T.edges[node]:
                        self.link(node, a, w)

    def get_links(self):
        return [(a, b, w) for a in self.nodes for (b, w) in self.edges[a] if a in self.edges]

    def remove_backward_links(self, root):
        self.bidirectional = False
        for (child, _) in self.edges[root]:
            self.half_unlink(child, root)
            self.remove_backward_links(child)