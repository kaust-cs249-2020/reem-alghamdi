"""
@BY: Reem Alghamdi
@DATE: 02-10-2020
"""
from random import choice
from ch3.code.ch3_08 import format_adjacency_list
from ch3.code.ch3_10 import graph_degrees


def topological_ordering(adj_list):
    _list = []
    degrees = graph_degrees(adj_list)
    candidates = [x for x in adj_list if degrees[x][0] == 0]
    while candidates:
        candidate = choice(candidates)
        _list.append(candidate)
        candidates.remove(candidate)
        if adj_list.get(candidate):
            for node in adj_list.get(candidate)[:]:
                adj_list[candidate].remove(node)
                degrees = graph_degrees(adj_list)
                if not degrees.get(node) or degrees[node][0] == 0:
                    candidates.append(node)

    for key, val in adj_list.items():
        if len(val) > 0:
            return "the input graph is not a DAG"
    return _list


if __name__ == "__main__":
    adj = """0 -> 1
1 -> 2
3 -> 1
4 -> 2"""
    print(', '.join(topological_ordering(format_adjacency_list(adj))))
    with open("../data/dataset_369325_3.txt") as file:
        print(', '.join(topological_ordering(format_adjacency_list(file.read()))))
