"""
@BY: Reem Alghamdi
@DATE: 04-10-2020
"""
import operator

from ch5.code.ch5_17 import topological_ordering


def format_weighted_adjacency_list(text):

    adj_list = {}
    weights = {}
    for line in text.split("\n"):
        node, edge = line.split("->")
        if adj_list.get(node):
            b = edge.split(":")
            adj_list[node].append(b[0])
        else:
            b = edge.split(":")
            adj_list[node] = [b[0]]
        weights[(node, b[0])] = int(b[1])

    return adj_list, weights


def longest_path_in_dag(start_node, end_node, adj_list, weights, is_local=False, is_fitting=False, is_overlap=False):
    ordering = topological_ordering(adj_list)
    # delete start node and everything before it
    ordering = ordering[ordering.index(start_node)+1:]
    print(len(ordering))

    # set weights to node = -infinity (or any other negative number really)
    # s = {node: -float("inf") for node in {t[0] for t in weights.keys()} or {t[1] for t in weights.keys()}}
    s = {}
    s[start_node] = 0
    # backtrack = {node: None for node in ordering}
    backtrack = {}
    # print(backtrack)
    # print(len(ordering))
    indices = (-1, -1)
    max_score = -float("inf")
    for node in ordering:
        # Sb = max[all predessesors a of b(Sa + weight from a to b)
        if not s.get(node):
            s[node] = -float("inf")
            backtrack[node] = None
        for k, v in weights.items():
            if k[1] == node:
                weight = s[k[0]] + v
                if weight > s[node]:
                    s[node] = weight
                    backtrack[node] = k[0]
        # s_a = {k[0]: v for k, v in weights.items() if k[1] == node}
        # s_a = {a: s[a] + w for a, w in s_a.items()}
        # print(s_a)
        # backtrack[node], s[node] = max(s_a.items(), key=lambda k: k[1])
        # print(s[node])

        if is_overlap:  # max last vertical edge
            if node[1] == end_node[1]:
                if s[node] >= max_score:
                    indices = node
                    max_score = s[node]
        if is_local:  # max over everything
            if s[node] > max_score:
                indices = node
                max_score = s[node]

        if is_fitting:  # max last horizontal edge
            if node[0] == end_node[0]:
                if s[node] >= max_score:
                    indices = node
                    max_score = s[node]
    # if is_local:
    #     end_node = max(s.items(), key=operator.itemgetter(1))[0]

    # if is_fitting:
        # print(sorted(s.items()))
        # print(list({k: v for k, v in s.items() if k[0] == end_node[0]}.values()))
        # end_node = max({k: v for k, v in s.items() if k[0] == end_node[0]}.items(), key=operator.itemgetter(1))[0]
        # print(end_node)

    if is_overlap or is_local or is_fitting:
        end_node = indices
    path = [end_node]
    print(path)
    while path[0] != start_node:
        path = [backtrack[path[0]]] + path
    return s[end_node], path


if __name__ == "__main__":
    with open("../data/dataset_369316_7.txt") as file:
        # print(adj_list_string)
        adj_list, weights = format_weighted_adjacency_list(file.read())
        print(adj_list, weights)
        s, path = longest_path_in_dag("0", "49", adj_list, weights)
        print(s)
        print('->'.join(path))
