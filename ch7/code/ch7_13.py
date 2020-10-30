"""
@BY: Reem Alghamdi
@DATE: 22-10-2020
"""
from ch7.code.ch7_12 import colored_edges, graph_to_genome, chromosome_array_to_string, string_to_chromosome_array


def _2_break_on_genome_graph(genome_graph, i1, i2, i3, i4):
    """
    (2, 4), (3, 8), (7, 5), (6, 1)
    1, 6, 3, 8

    Sample Output:

    (2, 4), (3, 1), (7, 5), (6, 8)
    """

    try:
        genome_graph.remove([i1, i2])
    except:
        genome_graph.remove([i2, i1])

    try:
        genome_graph.remove([i3, i4])
    except:
        genome_graph.remove([i4, i3])

    genome_graph.append([i1, i3])
    genome_graph.append([i2, i4])

    return genome_graph


def _2_break_on_genome(p, i1, i2, i3, i4):
    graph = colored_edges(p)
    graph = _2_break_on_genome_graph(graph, i1, i2, i3, i4)
    p = graph_to_genome(graph)
    return p


if __name__ == "__main__":
    # string = "(2, 4), (3, 8), (7, 5), (6, 1)"
    # string = "(2, 3), (4, 5), (6, 7), (8, 10), (9, 12), (11, 14), (13, 15), (16, 18), (17, 20), (19, 22), (21, 23), (24, 26), (25, 28), (27, 30), (29, 32), (31, 34), (33, 35), (36, 37), (38, 39), (40, 42), (41, 43), (44, 46), (45, 48), (47, 49), (50, 51), (52, 53), (54, 56), (55, 58), (57, 60), (59, 61), (62, 63), (64, 66), (65, 68), (67, 69), (70, 71), (72, 73), (74, 75), (76, 77), (78, 79), (80, 82), (81, 83), (84, 85), (86, 87), (88, 90), (89, 92), (91, 94), (93, 96), (95, 98), (97, 99), (100, 101), (102, 104), (103, 106), (105, 107), (108, 110), (109, 112), (111, 114), (113, 115), (116, 118), (117, 119), (120, 121), (122, 1)"
    # genome = string_to_edges(string)
    # print(edges_to_string(_2_break_on_genome_graph(genome, 1, 6, 3, 8)))
    # print(edges_to_string(_2_break_on_genome_graph(genome, 116, 118, 2, 3)))
    string = "(+1 -2 -4 +3)"
    # string = "(-45 -58 -44 -3 -27 +2 +35 -43 +62 -19 +37 -61 -9 -6 +40 -36 +10 -25 +28 -42 -32 -49 +20 -26 -57 -11 +56 +50 +59 -46 +30 -22 -5 +4 -41 +16 -1 -54 -51 +8 -48 -29 -55 +38 +15 -7 -17 -18 -53 -14 +47 +33 +21 +31 +23 +13 +24 -39 +12 -60 -34 +63 +52)"
    genome = string_to_chromosome_array(string)
    genome_graph = _2_break_on_genome(genome, 1, 6, 3, 8)
    # genome_graph = _2_break_on_genome(genome, 70, 86, 29, 76)
    print(chromosome_array_to_string(genome_graph))
