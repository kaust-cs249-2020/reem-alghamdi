"""
@BY: Reem Alghamdi
@DATE: 04-10-2020
"""
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


def longest_path_in_dag(start_node, end_node, adj_list_string):
    # print(adj_list_string)
    adj_list, weights = format_weighted_adjacency_list(adj_list_string)
    # print(adj_list)
    # print(weights)
    ordering = topological_ordering(adj_list)
    # print(ordering)
    # delete start node and everything before it
    ordering = ordering[ordering.index(start_node)+1:]

    # set weights to node = -infinity (or any other negative number really)
    s = {node: -1 for node in {t[0] for t in weights.keys()} or {t[1] for t in weights.keys()}}
    s[start_node] = 0
    backtrack = {node: None for node in ordering}
    # print(backtrack)
    for node in ordering:
        # Sb = max[all predessesors a of b(Sa + weight from a to b)
        s_a = {k[0]: v for k, v in weights.items() if k[1] == node}
        s_a = {a: s[a] + w for a, w in s_a.items()}
        # print(s_a)
        backtrack[node], s[node] = max(s_a.items(), key=lambda k: k[1])

    # print(backtrack)
    path = [end_node]
    while path[0] != start_node:
        path = [backtrack[path[0]]] + path

    return s[end_node], path


if __name__ == "__main__":
    with open("../data/dataset_369316_7.txt") as file:
        s, path = longest_path_in_dag("0", "49", file.read())
        print(s)
        print('->'.join(path))
