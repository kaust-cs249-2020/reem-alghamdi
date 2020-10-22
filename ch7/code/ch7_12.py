"""
@BY: Reem Alghamdi
@DATE: 22-10-2020
"""


def format_chromosome(string_chromosome):
    """
    given the string "(+1 -2 -3 +4)", turn it into the array [+1 -2 -3 +4]
    """
    return [int(x) for x in string_chromosome[1:-1].split()]


def format_cycles(all_edges):
    """
    given the edges (2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8), split them to get two edges groups
     (2, 4), (3, 6), (5, 1) and (7, 9), (10, 12), (11, 8) then into their cycles
     1 2 3 4 6 5 and 8 7 9 10 12 11
    """
    split_edges_by_cycle = [[]]
    for edge in all_edges:
        if edge[0] > edge[1]:
            split_edges_by_cycle[-1].append(edge[0])
            split_edges_by_cycle[-1].insert(0, edge[1])
            split_edges_by_cycle.append([])
        else:
            split_edges_by_cycle[-1].extend(edge)
    split_edges_by_cycle = split_edges_by_cycle[:-1]
    return split_edges_by_cycle


def chromosome_to_cycle(chromosome):
    nodes = [0] * len(chromosome) * 2
    for j in range(len(chromosome)):
        i = chromosome[j]
        if i > 0:
            nodes[2*j] = 2 * i - 1
            nodes[2*j + 1] = 2 * i
        else:
            nodes[2*j] = -2 * i
            nodes[2*j + 1] = -2 * i - 1
    return nodes


def cycle_to_chromosome(nodes):
    """for j ← 1 to |Nodes|/2
          if Nodes2j−1 < Nodes2j
               Chromosomej ← Nodes2j /2
          else
               Chromosomej ← −Nodes2j−1/2
     return Chromosome"""
    chromosome = [0] * int(len(nodes) / 2)
    for j in range(int(len(nodes)/2)):
        if nodes[2 * j] < nodes[2 * j + 1]:
            chromosome[j] = int(nodes[2 * j + 1] / 2)
        else:
            chromosome[j] = int(-nodes[2 * j] / 2)
    return chromosome


def colored_edges(p):
    """given a genome p, return the edges colored"""
    edges = []
    for chromosome in p:
        nodes = chromosome_to_cycle(chromosome)
        print(chromosome)
        print(nodes)
        for j in range(0, len(chromosome)):
            try:
                edges.append([nodes[2 * j + 1], nodes[2 * (j + 1)]])
            except:
                edges.append([nodes[2 * j + 1], nodes[0]])
    return edges


def graph_to_genome(genome_graph):
    """
    given the colored edges, return the chromosomes
    """
    p = []
    cycles = format_cycles(genome_graph)
    for nodes in cycles:
        chromosome = cycle_to_chromosome(nodes)
        p.append(chromosome)
    return p


if __name__ == "__main__":
    # print(format_chromosome("(+1 -2 -3 +4)"))
    # string = "(+1 -2 -3 +4)"
    # string = "(+1 -2 -3 +4 +5 -6 +7 -8 +9 +10 +11 -12 +13 +14 +15 +16 +17 +18 -19 +20 -21 -22 -23 +24 +25 -26 -27 -28 -29 +30 -31 -32 +33 -34 +35 -36 +37 -38 +39 -40 +41 +42 -43 -44 -45 +46 -47 -48 -49 +50 +51 +52 +53 -54 -55 +56 +57 -58 +59 -60 +61 +62 -63 -64 -65 +66 +67 +68 +69)"
    # out = chromosome_to_cycle(format_chromosome(string))
    # print("(" + ' '.join(map(str, out)) + ")")

    # string = "(1 2 4 3 6 5 7 8)"
    # string = "(2 1 4 3 5 6 7 8 9 10 11 12 13 14 16 15 17 18 20 19 22 21 24 23 25 26 27 28 29 30 32 31 33 34 36 35 38 37 40 39 42 41 44 43 45 46 47 48 50 49 52 51 54 53 56 55 58 57 59 60 62 61 64 63 65 66 67 68 69 70 71 72 73 74 76 75 77 78 80 79 81 82 83 84 85 86 87 88 90 89 92 91 93 94 95 96 98 97 100 99 102 101 103 104 105 106 108 107 109 110 111 112 113 114 116 115 117 118 120 119 121 122 124 123 126 125)"
    # out = cycle_to_chromosome(format_chromosome(string))
    # print("(" + ' '.join(['{0:+d}'.format(j) for j in out]) + ")")

    # string = "(+1 -2 -3)(+4 +5 -6)"
    # # string = "(+1 -2 +3 +4 +5 +6 +7 +8 -9 +10 -11 -12 -13 -14 -15 -16 -17 +18 -19 -20 +21 +22 +23 +24 -25 -26 +27 +28 -29 -30)(-31 +32 -33 +34 +35 -36 +37 -38 +39 +40 +41 -42 -43 -44 -45 +46 +47 -48 +49 -50 +51 +52 +53 -54 -55 -56)(-57 +58 +59 +60 -61 -62 +63 +64 +65 +66 -67 +68 -69 +70 +71 -72 -73 +74 -75 -76 +77 +78 +79 -80 -81 -82 -83 +84 +85 -86 -87)(+88 -89 -90 +91 -92 -93 -94 +95 +96 -97 -98 -99 +100 -101 -102 -103 -104 +105 +106 +107 +108 +109 +110)(-111 +112 -113 +114 -115 +116 +117 -118 +119 +120 -121 +122 +123 -124 -125 -126 +127 -128 -129 -130 +131 -132 -133 -134 -135 -136 +137)(-138 +139 +140 +141 -142 +143 +144 +145 -146 -147 +148 +149 +150 +151 -152 -153 -154 -155 -156 +157 -158 +159 +160 -161 +162 -163 +164 -165 -166)(+167 -168 +169 -170 -171 -172 -173 +174 -175 +176 -177 +178 +179 -180 -181 -182 -183 +184 -185 +186 -187 -188 +189)(-190 +191 +192 -193 +194 +195 -196 +197 -198 -199 -200 +201 +202 +203 -204 -205 -206 +207 -208 -209 -210 -211 -212 -213 +214)(-215 +216 -217 +218 +219 -220 -221 +222 +223 -224 +225 +226 -227 +228 -229 +230 -231 +232 +233 -234 -235 -236 -237 +238 +239 +240 +241 -242 +243)"
    # chromosome_array = [format_chromosome(x) for x in string.replace(")", ")S").split("S")[:-1]]
    # out = colored_edges(chromosome_array)
    #
    # print(', '.join([str(tuple(x)) for x in out]))

    # string_edges = "(2, 4), (3, 6), (5, 1), (7, 9), (10, 12), (11, 8)"
    string_edges = "(2, 3), (4, 6), (5, 7), (8, 10), (9, 12), (11, 13), (14, 15), (16, 18), (17, 19), (20, 22), (21, 24), (23, 25), (26, 28), (27, 30), (29, 31), (32, 34), (33, 35), (36, 38), (37, 40), (39, 42), (41, 43), (44, 45), (46, 48), (47, 50), (49, 52), (51, 54), (53, 56), (55, 58), (57, 60), (59, 1), (61, 63), (64, 66), (65, 68), (67, 69), (70, 71), (72, 74), (73, 76), (75, 78), (77, 80), (79, 82), (81, 83), (84, 85), (86, 87), (88, 90), (89, 92), (91, 93), (94, 96), (95, 98), (97, 100), (99, 101), (102, 103), (104, 106), (105, 108), (107, 109), (110, 111), (112, 62), (113, 116), (115, 118), (117, 119), (120, 122), (121, 123), (124, 125), (126, 128), (127, 130), (129, 132), (131, 134), (133, 135), (136, 138), (137, 140), (139, 142), (141, 144), (143, 145), (146, 147), (148, 149), (150, 151), (152, 153), (154, 156), (155, 158), (157, 160), (159, 161), (162, 163), (164, 165), (166, 114), (167, 169), (170, 171), (172, 173), (174, 176), (175, 177), (178, 179), (180, 182), (181, 183), (184, 186), (185, 187), (188, 189), (190, 191), (192, 193), (194, 196), (195, 198), (197, 200), (199, 202), (201, 203), (204, 205), (206, 208), (207, 209), (210, 168), (211, 214), (213, 215), (216, 218), (217, 220), (219, 222), (221, 224), (223, 226), (225, 227), (228, 229), (230, 231), (232, 234), (233, 236), (235, 237), (238, 239), (240, 242), (241, 244), (243, 246), (245, 247), (248, 249), (250, 251), (252, 253), (254, 256), (255, 258), (257, 260), (259, 212), (261, 264), (263, 266), (265, 267), (268, 269), (270, 272), (271, 273), (274, 275), (276, 278), (277, 279), (280, 281), (282, 283), (284, 285), (286, 287), (288, 290), (289, 291), (292, 293), (294, 295), (296, 297), (298, 300), (299, 302), (301, 303), (304, 262), (306, 307), (308, 309), (310, 312), (311, 313), (314, 316), (315, 318), (317, 320), (319, 321), (322, 323), (324, 325), (326, 327), (328, 329), (330, 332), (331, 333), (334, 336), (335, 338), (337, 340), (339, 342), (341, 344), (343, 346), (345, 348), (347, 305)"
    all_edges = [list(eval(x)) for x in string_edges.replace("), ", ")S").split("S")]
    # print(format_cycles(all_edges))

    chromosomes = graph_to_genome(all_edges)
    # print(chromosomes)
    oo = ""
    for out in chromosomes:
        oo += "(" + ' '.join(['{0:+d}'.format(j) for j in out]) + ")"
    print(oo)

