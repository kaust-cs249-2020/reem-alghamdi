"""
@BY: Reem Alghamdi
@DATE: 19-09-2020
"""
import operator

from ch3.code.ch3_02 import compositionk
from ch3.code.ch3_05 import de_bruijn_graph_fromkmer
from ch3.code.ch3_08 import get_balance, format_adjacency_list


def contig_generation(patterns):
    """
    :param patterns: collection of k-mers
    :return: list of contigs in de bruijn graph
    """
    contigs = []
    adj_list = de_bruijn_graph_fromkmer(patterns)
    return branches(adj_list)

def branches(adj_list):
    """
    Paths ← empty list
        for each node v in Graph
            if v is not a 1-in-1-out node
                if out(v) > 0
                    for each outgoing edge (v, w) from v
                        NonBranchingPath ← the path consisting of single edge (v, w)
                        while w is a 1-in-1-out node
                            extend NonBranchingPath by the edge (w, u)
                             w ← u
                        add NonBranchingPath to the set Paths
        for each isolated cycle Cycle in Graph
            add Cycle to Paths
        return Paths
    """
    paths = []
    degrees = graph_degrees(adj_list)
    for node, lists in adj_list.items():
        if degrees[node] != [1, 1]:
            for child in lists:
                non_branching_path = [node]
                next_node = child
                while True:
                    non_branching_path.append(next_node[-1])
                    degree = degrees[next_node]
                    if degree == [1, 1]:
                        next_node = adj_list[next_node][0]
                    else:
                        break
                paths.append(''.join(non_branching_path))
        elif degrees[node] == [1, 1]:
            next_node = lists[0]
            if adj_list.get(next_node) and node == adj_list[next_node][0]:
                isolated = [node]
                while next_node != node:
                    isolated.append(next_node[-1])
                    if adj_list.get(next_node):
                        next_node = adj_list[next_node][0]
                    else:
                        break
                isolated.append(next_node[-1])
                paths.append(''.join(isolated))
    return sorted(paths)


def graph_degrees(graph):
    degrees = {}
    for i in graph.keys():
        ends = graph[i]
        out_degree = len(ends)

        if i in degrees:
            degrees[i][1] = out_degree
        else:
            degrees[i] = [0, out_degree]

        for j in ends:
            if j in degrees:
                degrees[j][0] += 1
            else:
                degrees[j] = [1, 0]

    return degrees


if __name__ == "__main__":
#     print(contig_generation(compositionk("TAATGCCATGGGATGTT", k=3)))
#     print(*generate_contigs_from_reads("""ATG
# ATG
# TGT
# TGG
# CAT
# GGA
# GAT
# AGA""".split()))
    with open("../data/dataset_369275_5.txt") as file:
        # print(*generate_contigs_from_reads(file.read().splitlines()))
        print(*contig_generation(file.read().splitlines()))
    # with open("../data/ch3_14") as file:
    #     for path in branches(format_adjacency_list(file.read())):
    #         print(" -> ".join(path))
