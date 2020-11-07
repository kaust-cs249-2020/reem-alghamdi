"""
@BY: Reem Alghamdi
@DATE: 30-10-2020
"""


class Node:
    def __init__(self, val, label=None):
        self.index = val
        self.label = label

    def add_s(self, tbl):
        self.s = tbl

    def __str__(self):
        return self.label if self.label else self.index

    def __repr__(self):
        return self.index if not self.label else str((self.index, self.label))

    def __lt__(self, other):
        return (self.label if self.label else self.index) < \
               (other.label if other.label else other.index)


class Tree(object):

    ## public code for the data structure Tree

    def __init__(self, N=-1, bidirectional=True) -> object:
        self.nodes = list(range(N))
        self.edges = {}
        self.bidirectional = bidirectional
        self.N = N

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
        if not a in self.nodes:
            self.nodes.append(a)
        if a in self.edges:
            self.edges[a] = [(b0, w0) for (b0, w0) in self.edges[a] if b0 != b] + [(b, weight)]
        else:
            self.edges[a] = [(b, weight)]

    def half_unlink(self, a, b):
        links = [(e, w) for (e, w) in self.edges[a] if e != b]
        if len(links) < len(self.edges[a]):
            self.edges[a] = links
        else:
            print('Could not unlink {0} from {1}'.format(a, b))
            self.print()

    def are_linked(self, a, b):
        return len([e for (e, w) in self.edges[a] if e == b]) > 0

    def AdjList(self, includeNodes=False, is_float=False, is_string=False):
        print('AdjList')
        self.nodes.sort()
        if includeNodes:
            print(self.nodes)
        for node in self.nodes:
            if node in self.edges:
                for edge in self.edges[node]:
                    end, weight = edge
                    string = '%s->%s:' if is_string else '%i->%i:'
                    if is_float:
                        string += '%.3f'
                    else:
                        string += '%d'

                    print(string % (node, end, weight))

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